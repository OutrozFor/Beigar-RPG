from entrada_segura import ler_inteiro, ler_texto_nao_vazio
#Status do jogador
nome_jog = ''
vida_max_jog = 50
vida_jog = 50
forca_min_jog = 0
forca_max_jog = 0
energia_jog = 10
energia_max_jog = 10
defesa_jog = 2
usou_cristal = False
usou_orbe = False
curupira_vive = True
jogador_vive = True

#Dicionário dos inventários do jogador

#O int é a quantidade do item no inventário
inventario = {'Veste Simplória': 1}
equipamento = {'Arma': '', 'Especial': '', 'Armadura': 'Veste Simplória'}

#Escolha de nome

def escolher_nome():
    global nome_jog
    
    nome_jog = ler_texto_nao_vazio('Digite seu nome: ', 'O nome não pode ficar vazio. Digite novamente.')
    print(f'Saudações, {nome_jog}!')
    
    return None


#Status do jogador
def status_jog():
    
    print(
    f'''
    Status do Jogador
         
    HP: {vida_jog}/{vida_max_jog}
    EP: {energia_jog}/{energia_max_jog}
    ATK: {forca_max_jog}
    DF: {defesa_jog}
    ''')
    
    return None

#Status dos iminigos
def status_inmg():
    import combate as cbt
    vida = cbt.inmg_atv[1]
    defesa = cbt.inmg_atv[4]
    print(
    f'''
    Status do Inimigo

    HP: {vida}
    EP: ???
    ATK: ???
    DF: {defesa}
    ''')
    
    return None

#Interface do inventário

def ver_inventario():
    import itens as its
    sair = False

    while sair == False:
        n = 0
        selecao = [0]

        print('\n')
        print('        Inventário')
    
        for item in inventario.keys():
        
            n += 1
            if item in its.armas:
                print(f'''
    {n}. {item} - Qntd: {inventario[item]}
    Descrição: {its.descricao[item][2]}
    Ataque Especial: {its.descricao[item][3][1]}
        ''')

            else:
                print(f'''
    {n}. {item} - Qntd: {inventario[item]}
    Descrição: {its.descricao[item][1]}
        ''')

            selecao += [item]

        print('''
    Este é o seu inventário. Se deseja equipar ou usar algum item, digite o número ao seu lado.
    Se quiser fechar o inventário, digite 0.
    ''')

        escolha = ler_inteiro(
            'Equipar/consumir: ',
            range(len(selecao)),
            'Escolha inválida! Digite o número de um item ou 0 para sair.'
        )

        item = selecao[escolha]

        if item in its.armas or item in its.armaduras:
            equipar(item)

        elif item in its.pocao_hp:
            its.pocao_vida(item)
            
        elif item in its.pocao_ep:
            its.pocao_energia(item)

        elif item == 'Cristal de Vida':
            its.cristal_de_vida()

        elif item == 'Orbe':
            its.orbe()

        elif escolha == 0:
            sair = True

        else:
            print('Este item não pode ser equipado nem consumido!')

    return None

#Função para equipar armas e armaduras

def equipar(item):
    import itens as its
    global forca_min_jog
    global forca_max_jog
    global defesa_jog

    qntd = inventario[item]
    
    if item in its.armas and qntd > 0:
        equipamento['Arma'] = item
        equipamento['Especial'] = its.descricao[item][3]
        forca_min_jog = its.descricao[item][0]
        forca_max_jog = its.descricao[item][1]
        print(f'Arma [{item}] equipada!')
        
    elif item in its.armaduras and qntd > 0:
        equipamento['Armadura'] = item
        defesa_jog = its.descricao[item][0]
        print(f'Armadura [{item}] equipada!')
        
    else:
        print('Este item não pode ser equipado!')

    return None
