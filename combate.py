import random
import time
import interface as itf
from entrada_segura import ler_inteiro

#Funções de ataque especial das armas

def rajada_de_tetano():
    global energia_jog
    if itf.energia_jog >= 5:
        print('Rajada de Tétano! Você deu 15 de dano!')
        itf.energia_jog -= 5
        return dano_ao_inmg(15)
    else:
        print('Você não tem energia suficiente!')
        return None

def corte_rapido():
    global energia_jog
    dano = 20
    if itf.energia_jog >= 2:
        if itf.usou_orbe == False:
            print(f'Corte Rápido! Você deu {dano} de dano!')
        elif itf.usou_orbe == True:
            dano += 35
            print(f'Corte letal! Você deu {dano} de dano!')
        itf.energia_jog -= 2
        return dano_ao_inmg(dano)
    else:
        print('Você não tem energia suficiente!')
        return None

def flechada_no_joelho():
    global energia_jog
    dano = random.randint(0,40) - inmg_atv[4]
    if itf.usou_orbe == True:
        dano += 35
    if dano < 0:
        dano = 0
    if itf.energia_jog >= 2:
        itf.energia_jog -= 2
        if dano > 30:
            print(f'Flechada no Joelho! Você deu {dano} de dano! {nome_inmg} já quer desistir da vida de aventura!')
        if 20 <= dano <= 30:
            print(f'Quase! Você deu {dano} de dano!')
        if 10 < dano < 20:
            print(f'Um pouco decepcionante, mas melhor que nada... Deu {dano} de dano.')
        if dano <= 10:
            print(f'Patético... Na próxima usa o ataque normal mesmo... Deu {dano} de dano...')
        return dano_ao_inmg(dano)
    else:
        print('Você não tem energia suficiente!')
        return None

def esfera_de_energia():
    global energia_jog
    dano = 40
    if itf.energia_jog >= 5:
        if itf.usou_orbe == False:
            print(f'Esfera de Energia! Você deu {dano} de dano! Você não vai passar, {nome_inmg}!')
        if itf.usou_orbe == True:
            dano += 35
            print(f'Kamehameha! Você deu {dano} de dano! Você não vai passar, {nome_inmg}!')
        itf.energia_jog -= 5
        return dano_ao_inmg(dano)
    else:
        print('Você não tem energia suficiente!')
        return None

def mire_na_cabeca():
    global energia_jog
    dano = random.randint(15,50) - inmg_atv[4]
    if itf.usou_orbe == True:
        dano += 35
    if dano < 0:
        dano = 0
    if itf.energia_jog >= 5:
        itf.energia_jog -= 5
        if dano > 40:
            print(f'Acertou na cabeça e deu {dano} de dano! Thor estaria orgulhoso!')
        if 25 <= dano <= 35:
            print(f'Quase acertou e deu {dano} de dano! Bom, mas não impediria o estalo...')
        if  18 <= dano < 25:
            print(f'Não acertou, mas tentou e deu {dano} de dano... Poderia melhorar.')
        if dano < 18:
            print(f'Ai, ai ai... Na próxima pega o cajado mágico, que nunca erra ou algo assim... Deu {dano} de dano.')
        return dano_ao_inmg(dano)
    else:
        print('Você não energia suficiente!')
        return None

#Satus inimigos
#Ordem dos status na tupla: (inmg_atv[1]: vida_inmg, inmg_atv[2]: forca_min_inmg, inmg_atv[3]: forca_max_inmg, inmg_atv[4]: defesa_inmg, inmg_atv[5]: energia_inmg, inmg_atv[6]: ( (loot_1, qntd_1), ... (loot_n, qntd_n) ))
inmg = {'exemplo':(50, 5, 8, 0, 20, ( ('Poção de Cura', 2), ('Espada Enferrujada', 1) )),
        'Caçador de Tesouros': (40, 0, 10, 0, 0, ( ('Bolsa sem Fundo', 1), ('Poção de Cura', 2), ('Poção de Energia', 1) )),
        'Gladiador Fantasma': (60, 3, 15, 2, 10, ( ('Elmo de Gladiador', 1), ('Orbe Desativada', 1), ('Poção de Cura', 2), ('Poção de Energia', 2) )),
        'Curupira': (150, 25, 35, 10, 100, ( ('Capa de Plumas de Pássaro-Trovão', 1), ('Cristal de Vida', 1), ('Poção de Cura', 3), ('Poção de Energia', 3) )),
        'Guardião do Cetro': (500, 45, 60, 35, 100, (('Cetro Milenar', 1), ))}

#Função de loot dos inimigos

def loot():
    loot_table = inmg_atv[6]
    import itens as its
    for item in loot_table:
        its.obter_item(item[0], item[1])
    return None

#Função de ativação de um inimigo
def seleciona_inmg(nome):
    global inmg_atv
    global nome_inmg
    
    inmg_atv = [nome] + list(inmg[nome][:])
    nome_inmg = inmg_atv[0]
    return None

#Funções de dano ao jogador e ao inimigo
def dano_ao_jog(dano):
    global vida_jog

    itf.vida_jog -= dano
    
    if itf.vida_jog <= 0:
        itf.vida_jog = 0
        print('Fim de jogo. Você morreu!')
    return None

def dano_ao_inmg(dano):
    global inmg_atv

    inmg_atv[1] -= dano
    
    if inmg_atv[1] <= 0:
        inmg_atv[1] = 0
        print(f'{nome_inmg} derrotado!')
    return None

#Funções de ataque básico do jogador e inimigos
def atk_do_jog():
    global forca_min_jog
    global forca_max_jog
    global inmg_atv
    
    roll = random.randint(itf.forca_min_jog, itf.forca_max_jog)
    defesa = inmg_atv[4]
    dano = roll - defesa
    if dano < 0:
        dano = 0
    print(f'Você deu {dano} de dano!')
    return dano_ao_inmg(dano)

def atk_do_inmg():
    global inmg_atv
    forca_min_inmg = inmg_atv[2]
    forca_max_inmg = inmg_atv[3]
    roll = random.randint(forca_min_inmg, forca_max_inmg)
    dano = roll - itf.defesa_jog
    if dano < 0:
        dano = 0
    print(f'{nome_inmg} deu {dano} de dano em você!')
    return dano_ao_jog(dano)

#Função controladora do combate

def inicia_combate(inmg):
    import itens as its
    global vida_jog
    global inmg_atv
    seleciona_inmg(inmg)
    print(f'{nome_inmg} te desafia para um duelo!')
    time.sleep(0.5)

    while itf.vida_jog > 0 and inmg_atv[1] > 0:
        itf.status_jog()
        itf.status_inmg()
        time.sleep(0.5)
        print(f'O que você deseja fazer?')
        print(f'''
    1. Lutar
    2. Usar Poção
    3. Fugir
        ''')

        escolha = ler_inteiro('Escolha: ', (0, 1, 2, 3))

        if escolha == 1:
            print(f'''
    1. Ataque Básico: {itf.forca_min_jog} - {itf.forca_max_jog} de dano
    2. {itf.equipamento['Especial'][0]}: {itf.equipamento['Especial'][1]}
    Para voltar ao menu anterior, escolha 0.''')
            
            escolha = ler_inteiro('Escolha: ', (0, 1, 2))
                
            if escolha == 1:
                atk_do_jog()
                
            elif escolha == 2:
                itf.equipamento['Especial'][2]()

        elif escolha == 2:
            n = 0
            selecao = [0]
            for i in itf.inventario.keys():
                if 'poção' in i.lower():
                    n += 1
                    print(f'''
    {n}. {i} - Qntd: {itf.inventario[i]}
    {its.descricao[i][1]}''')
                    
                    selecao += [i]
                    
            print('    Para voltar para o menu anterior, escolha 0')

            if len(selecao) == 1:
                print('Você não tem poções!')
                escolha = 0

            escolha = ler_inteiro(
                'Escolha: ',
                range(len(selecao)),
                'Escolha inválida! Digite o número de uma poção ou 0 para voltar.'
            )

            pocao = selecao[escolha]

            if pocao in its.pocao_hp:
                its.pocao_vida(pocao)
                        
            elif pocao in its.pocao_ep:
                its.pocao_energia(pocao)
                        
        elif escolha == 3:
            if nome_inmg == 'Caçador de Tesouros':
                time.sleep(0.5)
                print('Caçador de Tesouros: Mate-me ou morra! Só um de nós sairá daqui com o mapa e com vida, isso eu te garanto!')
            elif nome_inmg == 'Gladiador Fantasma':
                time.sleep(0.5)
                print('Gladiador Fantasma: Aqui não há lugar para covardes! Luta com honra ou morre tentando!')
            elif nome_inmg == 'Curupira':
                time.sleep(0.5)
                print('Curupira: Saiba que essa luta não precisava acontecer, mas agora você me obrigou a defender a honra do meu povo!')
            elif nome_inmg == 'Guardião do Cetro':
                time.sleep(0.5)
                print('Guardião do Cetro: É o seu fim. Seu destino é inevitável, não prolonga teu sofrimento.')
            print('Acho que não adianta muito tentar fugir...')
                
        else:
            print('Escolha Inválida!')
                    
        if inmg_atv[1] > 0 and escolha != 0:
            atk_do_inmg()
        if itf.vida_jog > 0 and inmg_atv[1] > 0 and escolha != 0 and itf.energia_jog < itf.energia_max_jog:
            itf.energia_jog += 1
            time.sleep(0.5)
            print('Você regenerou 1 EP.')

    if itf.vida_jog > 0 and inmg_atv[1] == 0:
        itf.vida_jog = itf.vida_max_jog
        itf.energia_jog = itf.energia_max_jog
        time.sleep(0.5)
        print('Vida e energia restauradas!')
        return loot()
