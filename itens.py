import combate as cbt
import interface as itf

#Dicionários e listas de itens do jogo
missao = ['Mapa do Cetro Milenar', 'Cetro Milenar', 'Bolsa sem Fundo', 'Orbe Desativada', 'Orbe', 'Cristal de Vida']
consumivel = ['Poção de Cura','Poção de Energia']
armas = ['Espada Enferrujada', 'Espada de Prata', 'Arco e Flecha', 'Cajado Mágico', 'Machado de Guerra', 'Excalibur', 'Braço de Tupã', 'Cólera Celestial', 'Leviatã']
armaduras = ['Veste Simplória', 'Elmo de Gladiador', 'Capa de Plumas de Pássaro-Trovão', 'Capa de Plumas de Fênix']
descricao = {
            'Mapa do Cetro Milenar': (None, 'Um mapa mágico único, capaz de guiar seu portador até o lendário Cetro Milenar.'),
            'Cetro Milenar': (None, '''O artefato das lendas é real... Feito de um metal dourado desconhecido, que brilha mais que mil sóis.
    Ele emana uma aura mágica incomensuravelmente poderosa.'''),
            
            'Orbe Desativada': (None, '''O poder contido nessa relíquia seria o suficiente para empoderar sua arma, desde que você tivesse a ajuda de um xamã poderoso...
    Ou se você roubasse o poder de um...'''),
            
            'Orbe': (None, 'Uma relíqua pronta para empoderar suas armas! Basta consumí-la!'),
            
            'Bolsa sem Fundo': (None, 'Uma bolsa com espaço aparentemente infinito... Como isso é possível? Eu sei lá, só sei que será útil na sua jornada!'),
            
            'Cristal de Vida': (None, 'Um cristal vermelho mágico em forma de coração. Capaz de dobrar a vida de quem o possui.'),
            
            'Poção de Cura': (25,'Cura 25 de HP.'),
            
            'Poção de Energia': (10,'Restaura 10 de EP.'),
            
            'Espada Enferrujada': (0, 8, 'Dá até 8 de dano nos inimigos. Tétano Blade!',
                                   ('Rajada de Tétano', 'Dá 15 de dano, ignorando a defesa do inimigo!', cbt.rajada_de_tetano) ),
            
            'Espada de Prata': (10, 20, 'Dá de 10 a 20 de dano nos inimigos. Uma arma elegante para tempos mais civilizados.',
                                ('Corte Rápido', 'Gasta 2 de energia. Dá 20 de dano ignorando a defesa dos inimigos! Patrocínio da Tramontina pendente...', cbt.corte_rapido) ),

            'Excalibur': (45, 55, 'Dá 45 a 55 de dano nos inimigos. Pelos poderes de Grayskull!',
                          ('Corte Letal', 'Gasta 2 de energia. Dá 55 de dano ignorando a defesa dos inimigos! Patrocínio da Tramontina pendente...', cbt.corte_rapido) ), 

            'Arco e Flecha': (10, 10, 'Dá exatamente 10 de dano nos inimigos. O terror de Aquiles...',
                              ('Flechada no Joelho', 'Gasta 2 de energia. O joelho é um alvo pequeno, mas sensível. Dá 0 a 40 de dano. Um tiro certeiro e o inimigo desiste da vida de aventureiro...', cbt.flechada_no_joelho) ),

            'Braço de Tupã': (45, 45, 'Dá exatamente 45 de dano nos inimigos. Digno de um herói da floresta.',
                              ('Seta Dilaceradora de Joelhos', 'Gasta 2 de energia. O joelho é um alvo pequeno, mas sensível. Dá 35 a 75 de dano. Um tiro certeiro e o inimigo desiste da vida de aventureiro...', cbt.flechada_no_joelho) ),
            
            'Cajado Mágico': (8, 8, f'Dá exatamente 8 de dano nos inimigos. Você é um bruxo, jogador!',
                              ('Esfera de Energia', 'Gasta 5 de energia, use com sabedoria... Dá 40 de dano ignorando a defesa do inimigo! Você não vai passar!', cbt.esfera_de_energia) ),

            'Cólera Celestial': (43, 43, f'Dá exatamente 43 de dano nos inimigos. Poder ilimitado!',
                               ('Kamehameha', 'Gasta 5 de energia, use com sabedoria... Dá 75 de dano ignorando a defesa do inimigo! Você não vai passar!', cbt.esfera_de_energia) ),
            
            'Machado de Guerra': (5, 30, 'O machado é uma arma lenta e pesada, com grande risco e recompensa de dano, dá de 5 a 30 de dano... Here´s Johnny!',
                                  ('Mire na Cabeça', 'Gasta 5 de energia. Dá 15 a 50 de dano! Um ataque certeiro no momento exato salvaria até o universo da ira de um titã louco...', cbt.mire_na_cabeca) ),

            'Leviatã': (40, 65, 'Dá de 40 a 65 de dano. Garoto...',
                        ('Arremesso Devastador', 'Gasta 5 de energia. Dá 50 a 85 de dano! Força o suficiente para decapitar um deus nórdico...', cbt.mire_na_cabeca) ),
            
            'Veste Simplória': (2, 'Uma veste normal, condizente com a moda atual em Beigar. Oferece apenas 2 de defesa.'),
            
            'Elmo de Gladiador': (20, 'Um antigo elmo pertencente a um gladiador caído. Já não tem mais sua antiga glória, mas oferece 20 de defesa.'),
            
            'Capa de Plumas de Pássaro-Trovão': (40, 'Uma bela capa feita das plumas de um pássaro-trovão usada pelo lendário Curupira. O sangue que você derramou desagrada os deuses...'),
            
            'Capa de Plumas de Fênix': (40, 'Uma bela capa feita das plumas de uma fênix. Um belo presente do lendário Curupira. Sua humildade agrada os deuses.')
            }

itens = missao + consumivel + armas + armaduras

#Função de obtenção de itens
def obter_item(item,qntd=1):
    
    if item in itens and item not in itf.inventario:
        itf.inventario[item] = qntd
        print(f'Obteve {qntd} [{item}].')
    elif item in itens and item in itf.inventario:
        itf.inventario[item] += qntd
        print(f'Obteve {qntd} [{item}].')
    else:
        print('Item inválido!')

    return None

#Consumíveis e funções de consumo

pocao_hp = ['Poção de Cura']
pocao_ep = ['Poção de Energia']

def pocao_vida(nome):
    global vida_max_jog
    global vida_jog
    global inventario
    qntd = itf.inventario[nome]
    cura = descricao[nome][0]
    if qntd > 0:
        if itf.vida_jog == itf.vida_max_jog:
            print(f'Sua vida já está cheia! HP: {itf.vida_jog}/{itf.vida_max_jog}')
        elif itf.vida_jog + cura <= itf.vida_max_jog:
            itf.vida_jog += cura
            itf.inventario[nome] -= 1
            print(f'Vida curada! HP: {itf.vida_jog}/{itf.vida_max_jog}')
        else:
            itf.vida_jog = itf.vida_max_jog
            itf.inventario[nome] -= 1
            print(f'Vida curada! HP: {itf.vida_jog}/{itf.vida_max_jog}')
    else:
        print('Você não tem poções de cura!')

    return None

def pocao_energia(nome):
    global energia_max_jog
    global energia_jog
    global inventario
    qntd = itf.inventario[nome]
    boost = descricao[nome][0]
    if qntd > 0:
        if itf.energia_jog == itf.energia_max_jog:
            print(f'Sua energia já está cheia! EP: {itf.energia_jog}/{itf.energia_max_jog}')
        elif itf.energia_jog + boost <= itf.energia_max_jog:
            itf.energia_jog += boost
            itf.inventario[nome] -= 1
            print(f'Energia recuperada! EP: {itf.energia_jog}/{itf.energia_max_jog}')
        else:
            itf.energia_jog = itf.energia_max_jog
            itf.inventario[nome] -= 1
            print(f'Energia recuperada! EP: {itf.energia_jog}/{itf.energia_max_jog}')
    else:
        print('Você não tem poções de energia!')

    return None

#Itens especiais

def cristal_de_vida():
    global vida_jog
    global vida_max_jog
    global usou_cristal
    
    itf.vida_jog = 100
    itf.vida_max_jog = 100
    itf.usou_cristal = True
    print(f'Você usou o Cristal de Vida! Vida dobrada! HP: {itf.vida_jog}/{itf.vida_max_jog}')
    del itf.inventario['Cristal de Vida']

    return None

def orbe():
    global forca_min_jog
    global forca_max_jog
    global usou_orbe

    itf.equipamento['Arma'] = ''
    itf.equipamento['Especial'] = ''

    for item in armas:
        
        if item in itf.inventario.keys():
            
            if item == 'Espada de Prata':
                obter_item('Excalibur')
                del itf.inventario[item]
            
            elif item == 'Arco e Flecha':
                obter_item('Braço de Tupã')
                del itf.inventario[item]
            
            elif item == 'Cajado Mágico':
                obter_item('Cólera Celestial')
                del itf.inventario[item]
            
            elif item == 'Machado de Guerra':
                obter_item('Leviatã')
                del itf.inventario[item]

    itf.usou_orbe = True
    print('Você empoderou sua arma! Não esqueça de equipar sua nova arma...')
    del itf.inventario['Orbe']

    return None
