"""Funções de entrada resistentes a erros para preservar o fluxo do jogo."""


def ler_inteiro(prompt='Escolha: ', opcoes=None, mensagem='Escolha inválida! Tente novamente.'):
    """Lê um número inteiro e repete a mesma pergunta até receber uma opção válida."""
    while True:
        valor = input(prompt).strip()
        try:
            numero = int(valor)
        except (TypeError, ValueError):
            print(mensagem)
            continue

        if opcoes is not None and numero not in opcoes:
            print(mensagem)
            continue

        return numero


def ler_texto_nao_vazio(prompt='Digite: ', mensagem='Digite alguma coisa para continuar.'):
    """Evita nomes ou respostas vazias quando um texto é obrigatório."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print(mensagem)
