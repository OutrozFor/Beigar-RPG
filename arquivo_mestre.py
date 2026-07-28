import combate as cbt
import itens as its
import interface as itf
import dialogo as dlg
import time

#Função para iniciar o jogo

def jogar():
    global curupira_vive
    
    itf.escolher_nome()
    dlg.msg_inicial()
    
    time.sleep(3)

    print('Capítulo 1: Começa a Jornada')
    time.sleep(1)

    dlg.prefacio()

    escolha = input('Escolha: ')
                  
    while escolha not in ('1', '2'):
        print('Taberneiro: Desculpe, eu não te ouvi... Poderia Repetir?')
        escolha = input('Escolha: ')

    if escolha == '2':
        return dlg.final_piada()
    elif escolha == '1':
        
        dlg.capitulo_1_parte_1()
        escolha = input('Escolha: ')

        while escolha not in ('1', '2', '3', '4'):
            print('Escolha inválida, tente novamente.')
            escolha = input('Escolha: ')

        if escolha == '1':
            its.obter_item('Espada de Prata')
            itf.equipar('Espada de Prata')

        if escolha == '2':
            its.obter_item('Machado de Guerra')
            itf.equipar('Machado de Guerra')

        if escolha == '3':
            its.obter_item('Cajado Mágico')
            itf.equipar('Cajado Mágico')

        if escolha == '4':
            its.obter_item('Arco e Flecha')
            itf.equipar('Arco e Flecha')

        cbt.inicia_combate('Caçador de Tesouros')

        if itf.vida_jog == 0:
            return None
        
        else:
            dlg.capitulo_1_parte_2()

        leu_texto = []

        escolha = input('Escolha: ')

        while 'mt' not in leu_texto or 'pt' not in leu_texto or 'cv' not in leu_texto:

            while escolha not in ('1', '2', '3'):
                print('Vendedor: Não entendi... Poderia repetir?')
                escolha = input('Escolha: ')

            if escolha == '1':
                dlg.monte_do_coliseu()
                leu_texto.append('mt')

            if escolha == '2':
                dlg.pantanal()
                leu_texto.append('pt')

            if escolha == '3':
                dlg.caverna()
                leu_texto.append('cv')
                
            if 'mt' not in leu_texto or 'pt' not in leu_texto or 'cv' not in leu_texto:
                escolha = input('Escolha: ')

        time.sleep(2)
        print('Boa sorte, jovem! Liberte o reino dos predadores que o cercam.')
        print('\n')
        print('Fim do Capítulo 1')
        time.sleep(2)

        print('Ótimo! Agora que você já sabe mais sobre os próximos passos da jornada, vamos falar da sua nova Bolsa sem Fundo...')
        time.sleep(1)
        print('\n')
        print('''Toda vez que você estiver num momento que você deve escolher a partir de agora, você também pode tirar um
tempo para dar uma espiada no seu inventário, ler a descrição dos seus itens, talvez até beber uma poção ou outra se necessário...''')
        time.sleep(2)
        print('\n')
        print('''Para fazer isso, basta digitar 'inventario' (sem acento) a qualquer momento que você precise fazer uma escolha!
Você também terá a opção de checar sua bolsa ao fim de cada capítulo da história!''')
        time.sleep(1)
        print('\n')
        print('Experimente fazer isso agora...')

        escolha = input('Escolha: ')

        while escolha.lower() != 'inventario':
            print('Tente mais uma vez...')
            escolha = input('Escolha: ')

        if escolha.lower() == 'inventario':
            itf.ver_inventario()

        print('Viu como é fácil? Agora voltemos à nossa história...')
        time.sleep(2)
        
        print('Capítulo 2: O Primeiro Desafio')
        dlg.capitulo_2_parte_1()
        cbt.inicia_combate('Gladiador Fantasma')

        if itf.vida_jog == 0:
            return None

        else:
            dlg.capitulo_2_parte_2()

        print('Fim do Capítulo 2')
        time.sleep(1)
        print('Você quer dar uma olhada no seu inventário e checar seus novos itens? Diga que sim, por favor :´(')
        time.sleep(1)
        print('1. Sim!')
        time.sleep(0.5)
        print('2. Claro!')
        time.sleep(0.5)
        print('3. Sem dúvidas!')

        escolha = input('Escolha: ')

        while escolha not in ('1','2','3'):
            print('Por favor escolha uma das 3 opções, não que elas façam muita diferença, hehe...')
            escolha = input('Escolha: ')

        if escolha in ('1','2','3'):
            itf.ver_inventario()

        print('Capítulo 3: A Escolha')

        dlg.capitulo_3_parte_1()

        escolha = input('Escolha: ')

        while escolha not in ('1','2'):
            if escolha == 'inventario':
                
                itf.ver_inventario()
                
                print('1. Desafiar o Curupira')
                time.sleep(1)
                print('2. Desculpar-se pelo mal-entendido')
                
                escolha = input('Escolha: ')
                
            else:
                print('Curupira: Anda. Me diga. Eu não tenho o dia todo...')

                print('1. Desafiar o Curupira')
                time.sleep(1)
                print('2. Desculpar-se pelo mal-entendido')
                
                escolha = input('Escolha: ')

        if escolha == '1':
            dlg.o_desafio()
            cbt.inicia_combate('Curupira')
        
            if itf.vida_jog == 0:
                return None
            else:
                itf.curupira_vive = False
                dlg.capitulo_3_parte_2_desafio()
                del itf.inventario['Orbe Desativada']
                its.obter_item('Orbe')

        elif escolha == '2':
            dlg.capitulo_3_parte_2_perdao()
            del itf.inventario['Orbe Desativada']
            its.obter_item('Orbe')
            its.obter_item('Cristal de Vida')
            its.obter_item('Capa de Plumas de Fênix')
            its.obter_item('Poção de Cura', 2)
            its.obter_item('Poção de Energia', 2)

        print('Fim do Capítulo 3')
        
        time.sleep(2)
        print('''E aí? Vamos dar uma olhadinha no inventário? Tá na hora de equipar a capa e usar o Orbe e o Cristal de Vida...
Acredite, você vai precisar...''')
        time.sleep(2)
        print('1. Sim')
        time.sleep(1)
        print('2. Vamos')
        
        escolha = input('Escolha: ')
        
        while escolha not in ('1','2'):
            print('É para o seu bem, você não quer que tudo que te trouxe até aqui tenha sido em vão, certo?')
            escolha = input('Escolha: ')
        
        if escolha in ('1', '2'):
            itf.ver_inventario()

        print('Capítulo 4: O Poder Corrompe')

        dlg.capitulo_4()
        cbt.inicia_combate('Guardião do Cetro')

        if itf.vida_jog == 0:
            return None
        else:
            dlg.vitoria()
            print('Fim do Capítulo 4')
        time.sleep(2)
        print('''Agora, antes de vermos o epílogo dessa história, dê uma olhadinha no inventário! Aprecie cada item que você adiquiriu
na sua jornada! (Sério, deu trabalho pra caramba pra pensar em cada item, dá uma olhadinha aí, por favor hahahaha)''')
        time.sleep(3)
        print('1. Ok')
        time.sleep(1)
        print('2. Não')

        escolha = input('Escolha: ')

        while escolha not in ('1','2'):
            print('Você escreveu errado, mas vamos, você não vai se arrepender :)')
            escolha = input('Escolha: ')

        if escolha == '1':
            print('Isso! Vamos, tome seu tempo...')
            time.sleep(2)
            itf.ver_inventario()

        elif escolha == '2':
            print('Ahh, achou que ia escapar, né? Como é bom dar ilusão de escolha para vocês humanos hehehe...')
            time.sleep(2)
            itf.ver_inventario()

        if itf.curupira_vive == True:
            dlg.final_bom()
            print('Final: Bom')
        elif itf.curupira_vive == False:
            dlg.final_ruim()
            print('Final: Ruim')
            
        print('Fim! Obrigado por jogar!')
        return None
            

if __name__ == "__main__":
    from rpg_gui import launch
    launch(jogar)