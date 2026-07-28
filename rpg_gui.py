"""Interface gráfica medieval para o jogo Beigar.

Mantém compatibilidade com o código antigo baseado em print/input.
"""
from __future__ import annotations

import builtins
import queue
import sys
import threading
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable


class RPGConsole:
    def __init__(self, root: tk.Tk, game_function: Callable[[], None]) -> None:
        self.root = root
        self.game_function = game_function
        self.answer_queue: queue.Queue[str] = queue.Queue()
        self.ui_queue: queue.Queue[tuple[str, object]] = queue.Queue()
        self.waiting_input = False
        self.original_print = builtins.print
        self.original_input = builtins.input

        self.root.title("BEIGAR — O Cetro Milenar")
        self.root.geometry("1180x760")
        self.root.minsize(960, 640)
        self.root.configure(bg="#120f0c")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self._configure_style()
        self._build_layout()
        self.root.after(50, self._process_ui_queue)
        self.root.after(300, self._refresh_status)

    def _configure_style(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("HP.Horizontal.TProgressbar", troughcolor="#30251d", background="#9e2a2b", borderwidth=0)
        style.configure("EP.Horizontal.TProgressbar", troughcolor="#30251d", background="#315f9e", borderwidth=0)

    def _build_layout(self) -> None:
        header = tk.Frame(self.root, bg="#1c1510", height=82, highlightbackground="#8a6a32", highlightthickness=1)
        header.pack(fill="x", padx=12, pady=(12, 8))
        header.pack_propagate(False)

        tk.Label(header, text="⚔  BEIGAR", font=("Georgia", 25, "bold"), fg="#e9ce8b", bg="#1c1510").pack(side="left", padx=22)
        tk.Label(header, text="A Jornada pelo Cetro Milenar", font=("Georgia", 13, "italic"), fg="#bfae8e", bg="#1c1510").pack(side="left", pady=(10, 0))

        body = tk.Frame(self.root, bg="#120f0c")
        body.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        body.grid_columnconfigure(0, weight=4)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        story_frame = tk.Frame(body, bg="#211a14", highlightbackground="#8a6a32", highlightthickness=1)
        story_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 8))

        tk.Label(story_frame, text="CRÔNICAS DE BEIGAR", font=("Georgia", 12, "bold"), fg="#d9bd78", bg="#211a14", pady=10).pack(fill="x")
        self.story = tk.Text(
            story_frame, wrap="word", state="disabled", bg="#17120e", fg="#eadfca",
            insertbackground="#eadfca", selectbackground="#70552d", relief="flat",
            font=("Georgia", 12), padx=20, pady=16, spacing1=3, spacing3=8,
        )
        scrollbar = ttk.Scrollbar(story_frame, command=self.story.yview)
        self.story.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.story.pack(fill="both", expand=True)
        self.story.tag_configure("chapter", font=("Georgia", 17, "bold"), foreground="#f0c75e", spacing1=16, spacing3=10)
        self.story.tag_configure("system", font=("Consolas", 10, "italic"), foreground="#9cc5a1")
        self.story.tag_configure("combat", font=("Georgia", 12, "bold"), foreground="#e48761")

        side = tk.Frame(body, bg="#1c1510", highlightbackground="#8a6a32", highlightthickness=1)
        side.grid(row=0, column=1, sticky="nsew")

        tk.Label(side, text="AVENTUREIRO", font=("Georgia", 13, "bold"), fg="#e9ce8b", bg="#1c1510", pady=13).pack(fill="x")
        self.name_label = tk.Label(side, text="Sem nome", font=("Georgia", 15, "bold"), fg="#f1e4ca", bg="#1c1510")
        self.name_label.pack(pady=(2, 16))

        self.hp_label = self._stat_block(side, "VIDA", "50 / 50")
        self.hp_bar = ttk.Progressbar(side, style="HP.Horizontal.TProgressbar", maximum=50, value=50)
        self.hp_bar.pack(fill="x", padx=18, pady=(0, 12))
        self.ep_label = self._stat_block(side, "ENERGIA", "10 / 10")
        self.ep_bar = ttk.Progressbar(side, style="EP.Horizontal.TProgressbar", maximum=10, value=10)
        self.ep_bar.pack(fill="x", padx=18, pady=(0, 14))

        self.atk_label = self._info_line(side, "ATK", "0–0")
        self.def_label = self._info_line(side, "DEF", "2")
        self.weapon_label = self._info_line(side, "ARMA", "Nenhuma")
        self.armor_label = self._info_line(side, "ARMADURA", "Veste Simplória")

        tk.Frame(side, height=1, bg="#6f552d").pack(fill="x", padx=16, pady=16)
        tk.Button(side, text="🎒  INVENTÁRIO", command=lambda: self._submit("inventario"), bg="#5c4526", fg="#fff0cf", activebackground="#7b6036", activeforeground="white", relief="flat", font=("Georgia", 11, "bold"), pady=9, cursor="hand2").pack(fill="x", padx=16)

        controls = tk.Frame(self.root, bg="#1c1510", highlightbackground="#8a6a32", highlightthickness=1)
        controls.pack(fill="x", padx=12, pady=(0, 12))
        self.prompt_label = tk.Label(controls, text="A aventura está começando...", bg="#1c1510", fg="#d9bd78", font=("Georgia", 11, "italic"), anchor="w")
        self.prompt_label.pack(fill="x", padx=15, pady=(10, 5))

        button_row = tk.Frame(controls, bg="#1c1510")
        button_row.pack(fill="x", padx=12, pady=(0, 8))
        self.choice_buttons: list[tk.Button] = []
        for number in range(5):
            btn = tk.Button(button_row, text=str(number), command=lambda n=number: self._submit(str(n)), width=6, bg="#33271d", fg="#e9ce8b", activebackground="#8a6a32", activeforeground="white", relief="flat", font=("Georgia", 11, "bold"), cursor="hand2", state="disabled")
            btn.pack(side="left", padx=3)
            self.choice_buttons.append(btn)

        self.entry = tk.Entry(button_row, bg="#120f0c", fg="#f1e4ca", insertbackground="#f1e4ca", relief="flat", font=("Georgia", 11))
        self.entry.pack(side="left", fill="x", expand=True, padx=(14, 5), ipady=8)
        self.entry.bind("<Return>", lambda _event: self._submit_entry())
        self.send_button = tk.Button(button_row, text="CONFIRMAR", command=self._submit_entry, bg="#70552d", fg="white", relief="flat", font=("Georgia", 10, "bold"), padx=14, cursor="hand2", state="disabled")
        self.send_button.pack(side="right")

    def _stat_block(self, parent: tk.Widget, title: str, value: str) -> tk.Label:
        row = tk.Frame(parent, bg="#1c1510")
        row.pack(fill="x", padx=18)
        tk.Label(row, text=title, bg="#1c1510", fg="#a9997c", font=("Georgia", 9, "bold")).pack(side="left")
        label = tk.Label(row, text=value, bg="#1c1510", fg="#f1e4ca", font=("Consolas", 10, "bold"))
        label.pack(side="right")
        return label

    def _info_line(self, parent: tk.Widget, title: str, value: str) -> tk.Label:
        row = tk.Frame(parent, bg="#1c1510")
        row.pack(fill="x", padx=18, pady=4)
        tk.Label(row, text=title, bg="#1c1510", fg="#a9997c", font=("Georgia", 9, "bold")).pack(side="left")
        label = tk.Label(row, text=value, bg="#1c1510", fg="#f1e4ca", font=("Georgia", 9), wraplength=135, justify="right")
        label.pack(side="right")
        return label

    def start(self) -> None:
        builtins.print = self.gui_print
        builtins.input = self.gui_input
        threading.Thread(target=self._run_game, daemon=True).start()

    def _run_game(self) -> None:
        try:
            self.game_function()
        except Exception as exc:
            self.ui_queue.put(("error", exc))
        finally:
            self.ui_queue.put(("finished", None))

    def gui_print(self, *args: object, sep: str = " ", end: str = "\n", **_: object) -> None:
        text = sep.join(str(arg) for arg in args) + end
        self.ui_queue.put(("text", text))

    def gui_input(self, prompt: str = "") -> str:
        self.ui_queue.put(("prompt", prompt or "Escolha sua ação:"))
        return self.answer_queue.get()

    def _submit_entry(self) -> None:
        value = self.entry.get().strip()
        if value:
            self.entry.delete(0, "end")
            self._submit(value)
        elif self.waiting_input:
            self.prompt_label.configure(text="Digite uma opção antes de confirmar.")
            self.entry.focus_set()

    def _submit(self, value: str) -> None:
        if not self.waiting_input:
            return
        self.waiting_input = False
        self._set_controls(False)
        self.prompt_label.configure(text=f"Você escolheu: {value}")
        self._append_text(f"\n› {value}\n", "system")
        self.answer_queue.put(value)

    def _set_controls(self, enabled: bool) -> None:
        state = "normal" if enabled else "disabled"
        for btn in self.choice_buttons:
            btn.configure(state=state)
        self.send_button.configure(state=state)
        self.entry.configure(state=state)
        if enabled:
            self.entry.focus_set()

    def _append_text(self, text: str, tag: str | None = None) -> None:
        self.story.configure(state="normal")
        selected_tag = tag
        stripped = text.strip()
        if stripped.startswith("Capítulo") or stripped.startswith("Fim do Capítulo") or stripped.startswith("Final:"):
            selected_tag = "chapter"
        elif "de dano" in text or "derrotado" in text or "te desafia" in text:
            selected_tag = "combat"
        if selected_tag:
            self.story.insert("end", text, selected_tag)
        else:
            self.story.insert("end", text)
        self.story.configure(state="disabled")
        self.story.see("end")

    def _process_ui_queue(self) -> None:
        try:
            while True:
                event, payload = self.ui_queue.get_nowait()
                if event == "text":
                    self._append_text(str(payload))
                elif event == "prompt":
                    self.waiting_input = True
                    self.prompt_label.configure(text=str(payload))
                    self._set_controls(True)
                elif event == "error":
                    self._append_text(f"\n[Erro] {payload}\n", "combat")
                    messagebox.showerror("Erro no jogo", str(payload))
                elif event == "finished":
                    self.waiting_input = False
                    self._set_controls(False)
                    self.prompt_label.configure(text="Fim da aventura.")
        except queue.Empty:
            pass
        self.root.after(50, self._process_ui_queue)

    def _refresh_status(self) -> None:
        try:
            import interface as itf
            self.name_label.configure(text=itf.nome_jog or "Sem nome")
            self.hp_label.configure(text=f"{itf.vida_jog} / {itf.vida_max_jog}")
            self.hp_bar.configure(maximum=max(1, itf.vida_max_jog), value=itf.vida_jog)
            self.ep_label.configure(text=f"{itf.energia_jog} / {itf.energia_max_jog}")
            self.ep_bar.configure(maximum=max(1, itf.energia_max_jog), value=itf.energia_jog)
            self.atk_label.configure(text=f"{itf.forca_min_jog}–{itf.forca_max_jog}")
            self.def_label.configure(text=str(itf.defesa_jog))
            self.weapon_label.configure(text=itf.equipamento.get("Arma") or "Nenhuma")
            self.armor_label.configure(text=itf.equipamento.get("Armadura") or "Nenhuma")
        except Exception:
            pass
        self.root.after(300, self._refresh_status)

    def close(self) -> None:
        builtins.print = self.original_print
        builtins.input = self.original_input
        self.root.destroy()


def launch(game_function: Callable[[], None]) -> None:
    root = tk.Tk()
    app = RPGConsole(root, game_function)
    app.start()
    root.mainloop()
