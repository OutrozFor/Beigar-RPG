import interface as itf
import time

#Mensagem inicial e pequeno tutorial

def msg_inicial():
    print(f'''
    Olá, {itf.nome_jog}! Seja bem-vindo(a) ao mundo de Beigar, um reino que esconde uma longa e
    interessante aventura baseada em um mito centenário. Acomode-se em seu assento e venha
    conosco em uma aventura repleta de mistérios, aprendizados e emoções.
    ''')
    time.sleep(3)
    print('''
    Antes de embarcarmos nessa história, preciso deixar algumas coisas claras, jovem!
    Seu status aparecerá a cada início de batalha, sendo parametrizado por 4 principais status:
    ''')
    time.sleep(2)
    print('\n')
    print('    Vida (HP): Pontos de vida do jogador;')
    time.sleep(1)
    print('''
    Energia (EP): Pontos utilizados para a execução de ataques mais poderosos, que exigem
    esforço do jogador;
    ''')
    time.sleep(2)
    print('''
    Força (ATK): Pontos, variando entre a força mínima e máxima de acordo com o armamento
    utilizado, para gerar dano ao inimigo;
    ''')
    time.sleep(2)
    print('''
    Defesa (DF): Pontos subtraídos do ataque do inimigo. Tem o valor inicial 2 e pode subir
    de acordo com os upgrades conquistados.
    ''')
    time.sleep(2)
    print('''
    Algumas escolhas podem fazer diferença no desenrolar da trama da nossa história,
    portanto escolha com sabedoria...
    ''')
    time.sleep(2)
    print('''
    Outra coisa: para evitar erros, espere a caixa de escolha aparecer na tela antes de digitar
    alguma coisa. Também, tome cuidado para não digitar letras quando a escolha pedir números ou vice-versa!
    ''')

#Prefácio da história

def prefacio():
    print('''
    Em uma terra longínqua, por volta do século XVI, um homem achou que poderia ser Deus. Vindo de
    uma dinastia de cavaleiros, nunca pensou, sequer nas mais profundas reflexões, que poderia chegar
    ao trono nessa vida. Mas aconteceu.
    ''')
    time.sleep(2)
    print('''
    Nosso pequeno senhor das batalhas voltou-se contra o governante abusivo que criava batalhas
    vazias por puro ego. Os ganhos dessas guerras jamais chegaram ao povo, não houve nem a mais remota melhora para
    ninguém a não ser sua corte de aproveitadores e, claro, o próprio rei Escarlian.
    ''')
    time.sleep(2)
    print('''
    Sua revolta foi acolhida pelos demais soldados, que forneceram todo o suporte para a deposição
    nada pacífica do rei autoritário. Em uma noite de baile, perante todos os demais governantes convidados para
    mais um dos eventos esbanjadores de Escarlian, o exército do reino de Beigar invadiu o salão principal
    e fez todos os presentes de reféns enquanto o cavaleiro se dirigia ao trono no centro do palco.
    Lá estavam: a rainha Sherxia, o filho mais velho Teemont, a filha caçula Jiorci e, o foco do cavaleiro,
    o rei Escarlian.
    ''')
    time.sleep(4)
    print('''
    Não houve tempo para grandes discursos, em poucos segundos o rosto confuso do governante tornou-se
    sem expressão e vazio ao ter sua cabeça arrancada. A família do rei gritava em desespero ao ver o corpo do
    “escolhido por Deus” estirado sem vida, jorrando sangue pelo pescoço, onde deveria haver uma cabeça.
    ''')
    time.sleep(2)
    print('''
    O discurso que se seguiu evidenciava que o povo estava descontente e não toleraria mais ser
    menosprezado e desvalorizado por uma elite que não via ninguém além daqueles que possuíam dotes, que mediam as
    pessoas por suas posses e conquistas- sem mérito algum, diga-se de passagem.
    ''')
    time.sleep(2)
    print('''
    Kolmairt: Eu preferiria morrer ao lado dos meus companheiros de batalha do que viver mais um dia servindo um
    parasita como esse monstro!
    ''')
    time.sleep(1)
    print('''
    Disse nosso herói ao empunhar a cabeça do ex-rei para o público. Como líder
    de uma grande revolução em Beigar, acima do que diziam ser a vontade de Deus, Kolmairt assume a nova era
    das terras distantes onde habitava: um governo do povo para o povo...
    ''')
    time.sleep(3)
    print(f'''
    Taberneiro: E é agora, {itf.nome_jog}, nessa taberna escura e mal frequentada, que te digo: você precisa ajudar o
    líder Kolmairt na consolidação da soberania de um governante popular perante os demais reinos. Para isso, há um
    caminho mágico conhecido apenas por aquele que conquistar o mapa escondido por alguma parte do mercado . Esse mapa
    te mostrará o caminho a percorrer para que encontre o cetro milenar, um objeto que concederá poder e
    sabedoria infinita ao que manuseá-lo, sendo assim o responsável por firmar o reinado justo de Kolmairt.
    Então, gostaria lutar ao lado de nosso revolucionário para ir em busca desse tesouro?
    ''')
    time.sleep(5)
    print('1. Sim')
    time.sleep(1)
    print('2. Não')

#Final Piada

def final_piada():
    print('''
    Taberneiro: Oh... Uma pena ver um jovem negando para si seu lado revolucionário. Sinto muito mesmo que cuidar de seu
    reino não seja seu interesse... Não o perturbarei mais com essa ideia. Mais uma caneca de hidromel, então?''')

#Desenrolar da história

#Capítulo 1
def capitulo_1_parte_1():
    print('''
    Taberneiro: Esse é o espírito! Fico contente que queira ajudar o governo dos justos. Venha, posso te mostrar como começar.
    Essa caneca é por minha conta!
    ''')
    time.sleep(2)
    print('''
    O jogador bebe mais uma caneca e segue o taberneiro pelo vilarejo até chegar ao mercado local.
    Chegando lá, é possível ver diversas tendas ofertando os mais variados produtos, desde tartarugas vivas, a mudas
    de araucária, a armas letais. Ambos caminham e analisam cada tenda, passeando com os olhos por cima dos produtos,
    até que o taberneiro verbaliza:
    ''')
    time.sleep(2)
    print(f'''
    Taberneiro: Bem, {itf.nome_jog}, minha jornada com você acaba por aqui. Sabe como é, não é mesmo? Tenho
    uma taberna para cuidar e bêbados para ouvir. Minha última dica será: procure nas defesas mais fortes o prêmio mais alto.
    ''')
    time.sleep(2)
    print(f'''
    {itf.nome_jog} logo se deu conta do que se tratava. O taberneiro estava falando da tenda com armas.
    Afinal, que lugar melhor defendido do que a fonte das armas? Ambos se despedem com um aperto de mãos e um
    sorriso confiante.
    ''')
    time.sleep(2)
    print(f'''
    Ao chegar à tenda de armamentos, {itf.nome_jog} avista uma pilha de papéis, contendo bilhetes, jornais
    recém manuscritos, um cantil aberto e, nos cantos da tenda, é avistado papéis aparentemente preenchendo as
    lacunas entre a lona e os canos de suporte.''')
    time.sleep(2)
    print('''
    Enquanto o responsável pela tenda atendia outros clientes, o jovem mexeu disfarçadamente
    nos cantos e, desamassando os pedaços, pôde encontrar o que parecia um mapa, porém possuía um borrão onde deveria
    estar o objeto ou pessoa alvo.
    ''')
    time.sleep(2)
    print(f'''
    Não houve muito tempo para pensar muito sobre o motivo do borrão, pois um saqueador, o Caçador de
    Tesouros, pulou em cima de {itf.nome_jog}, vindo de cima da tenda e rasgando a lona. Não poderia haver lugar melhor
    para estar do que a tenda de armamentos, não é mesmo?!
    ''')
    time.sleep(2)
    print(f'''
    Dando tempo apenas de guardar os papéis recém descobertos no bolso, {itf.nome_jog} escolhe rapidamente
    a arma que mais se adequa às suas habilidades. Haviam disponíveis: um machado, uma espada de prata, um cajado
    mágico e um arco e flecha. O jogador escolheu:
    ''')
    time.sleep(2)
    print('1. A espada')
    time.sleep(0.5)
    print('2. O machado')
    time.sleep(0.5)
    print('3. O cajado')
    time.sleep(0.5)
    print('4. O arco')


def capitulo_1_parte_2():
    print('''
    O Caçador de Tesouros deixa um item importante: a Bolsa sem Fundo! Agora você terá acesso a uma interface
    de inventário! Mas nós podemos discutir isso daqui a pouco. Primeiro, pergunte sobre os lugares mais perigosos da terra
    de Beigar e veja o que o vendedor de armas tem a lhe dizer sobre eles.
    ''')
    time.sleep(3)
    print('''
    Vendedor: Meu jovem, muito obrigado pelo auxílio, por pouco não levaram toda a minha mercadoria... Como posso
    agradecer-lhe?
    ''')
    time.sleep(2)
    print('Já sei! fique com essa arma, você já provou ter muita habilidade com ela. Mais alguma coisa com que eu possa te ajudar?')
    print('\n')
    time.sleep(1)
    print('1. Perguntar do Monte do Coliseu')
    time.sleep(1)
    print('2. Perguntar do Pantanal')
    time.sleep(1)
    print('3. Perguntar das Cavernas')

def monte_do_coliseu():
    print('''
    Bem... É um local conhecido pelas almas que ainda o assombram. As almas dos guerreiros ceifados por lá
    permanecem apavorando os que se atrevem a perambular por lá. Mas há uma lenda de que, em um local escondido da
    carcaça do coliseu, há um artefato poderoso: o Orbe! Dizem que quem o possui consegue encantar sua arma, deixando-a
    muito mais forte! Bem, é o que dizem por aí e acredito ser um bom começo na sua jornada pelo Cetro Milenar.
    ''')

def pantanal():
    print('''
    Ah, o Pantanal... Coração da nossa fauna e flora! Protegido há milhares de anos por povos que nem sabemos
    dizer quando chegaram aqui. Lá, você terá um pouco mais de dificuldade, pois o protetor lendário de lá não costuma deixar
    curiosos explorarem as terras sagradas. Acredito que talvez consiga dialogar com ele e explicar suas reais intenções ao
    caminhar por suas terras, mas não é garantido.
    ''')
    time.sleep(3)
    print('''
    Diga que precisa do poder místico dele para uma grande batalha e que conseguir a vitória garantiria
    prosperidade ao povo de Beigar.  Uma batalha seria desastrosa de todo modo. Se morrer, o reino perde a chance de
    reafirmar seu poderio sobre os demais e, assim, poderemos perder o governo dos justos. Se ganhar e ceifar a vida
    do lendário protetor, será o fim de tudo para ti.
    Kolmairt jamais o perdoaria por isso e, ainda que conseguisse o cetro, certamente perderia a vida posteriormente.
    Aconselho que faça o que tem que ser feito, priorizando seus interesses ou o interesse de todo o povo.
    ''')
    time.sleep(4)
    print('''
    Ah, tem mais uma coisa. Se as lendas contam a verdade, somente o sangue de um xamã muito poderoso
    seria capaz de fazer o Orbe funcionar, um xamã como o que protege o Pantanal.
    ''')


def caverna():
    print('''
    Acredito que com esse mapa que tens já percebeu que esse é seu ponto final. Como é de conhecimento
    popular, não basta apenas conseguir o mapa, você precisa ser merecedor da tentativa...
    ''')
    time.sleep(1)
    print('''
    Não poderia qualquer sortudo que achou o mapa conquistar o prêmio mais cobiçado das últimas 47
    gerações monárquicas do nosso reino. Assim que se deparar com a entrada da caverna, haverá uma troca a ser feita.
    Para conseguir a dica final, deve deixar de garantia um item que seja importante para ti... Caso consiga cumprir o
    requerimento, será a batalha que decidirá o futuro do mundo todo. A cada tentativa falha, a cada guerreiro que perde
    a batalha, o local muda e todo o progresso feito é permanentemente perdido.
    ''')

#Capítulo 2
    
def capitulo_2_parte_1():
    print(f'''
    O jogador então segue pela opção mais inteligente, que é começar pelo coliseu. Chegando no coliseu, {itf.nome_jog}
    caminha pelos destroços das arenas de batalha e um brilho gélido, quase uma poeira espiritual, passa ao fundo de um corredor
    a frente de si. O brilho atrai a atenção tal qual uma vela atrai insetos.
    ''')
    time.sleep(2)
    print('''
    Ao final desse corredor, já mais visível ao ponto de machucar os olhos do humano observador, um ser fantasmagórico surge,
    empunhando uma espada quebradiça e um escudo completamente amassado.
    ''')
    time.sleep(2)
    print('''
    ???: Eu notei sua presença a quilômetros daqui, jovem tolo. Acha mesmo que iria chegar às terras do Gladiador Fantasma e
    desrespeitar seu templo com barbaridade e desordem? Vai conhecer todo o poderio da minha era de ouro e aprender a não
    profanar com sua presença um templo ungido!!!
    ''')

def capitulo_2_parte_2():
    print('''
    Gladiador Fantasma: Não é possível! Eu, o maior campeão desse coliseu, perdi para um jovem insolente e patético, portando apenas
    uma arma mundana. Que Marte perdoe o desrespeito que cometestes, mas acompanhe suas próximas batalhas...
    ''')
    time.sleep(2)
    print('''
    O espectro desapareceu como poeira, dando lugar a dois frascos do tamanho de um pequeno perfume de bolsa,
    quase uma amostra, um Elmo e uma esfera de luz fraca de coloração roxa. Era o Orbe, a joia do poder. Junto do Orbe,
    um bilhete amarrado por uma fita vermelha dizia: força aos que precisam, glória eterna aos que lutam.
    ''')
    time.sleep(2)
    print('''
    Ao vencer a batalha, o jovem guarda seus novos itens na Bolsa sem Fundo e, antes de sair do coliseu, já na porta,
    desce de joelhos e murmura.
    ''')
    time.sleep(1)
    print(f'''
    {itf.nome_jog}: Sua força não será esquecida, sua história será contada para as futuras gerações. Gratidão pelos
    objetos encantados. Não perecerei.
    ''')
    time.sleep(1)
    print('E fez um símbolo sagrado na areia.')
    
def capitulo_3_parte_1():
    print(f'''
    Seguindo seu caminho, {itf.nome_jog} passa por uma mata densa com terreno plano e o ar cada vez mais pesado.
    O chão era lamacento e até afundava algumas vezes. Tendo que usar sua arma de apoio para não escorregar,foi uma missão
    por si só chegar até o coração do Pantanal. Parecia que quanto mais perto estava, mais claro o mapa parecia.
    ''')
    time.sleep(3)
    print('''
    Já chegando a exaustão, andou por mais algumas centenas de metros até avistar o que parecia um oásis naquele
    matagal todo: uma pequena cabana acima do nível do alagamento, com iluminação e um cavalo amarrado por uma corda.
    Vendo como uma possibilidade de meio de transporte, checa no mapa e confirma o óbvio: o ponto que buscava ficava
    justamente naquela cabana.
    ''')
    time.sleep(4)
    print(f'''
    Adentrando a morada, logo deparou-se com um homem alto, de físico bem definido, usando uma longa e colorida capa coberta
    de penas e pinturas que cobria todo o corpo. O homem, que estava de costas para {itf.nome_jog}, vira de frente e encara de cima a
    figura pequena e franzina perante ele.
    ''')
    time.sleep(3)
    print('''
    Curupira: Me avisaram que viria. O povo da mata nunca errou uma previsão sequer... Mas admito que me confundi por um mero
    segundo. Esperava que o guia dessa libertação seria Kolmairt, assim como o aventureiro responsável por encontrar o que pode finalmente
    libertar o reino das ameaças exteriores. Gostaria de saber o que busca por essas bandas e se eu quero que consiga isso.
    ''')
    time.sleep(3)
    print(f'''
    {itf.nome_jog}: Eu consegui o mapa, ele me levou até o coliseu e então até aqui. Vim em busca de algo
    que me ajude na busca pelo Cetro Milenar. E, perdão, “se quer que eu consiga”? Eu tenho uma missão clara aqui,
    boa sorte tentando entrar no meu caminho.
    ''')
    time.sleep(3)
    print('Curupira: Isso por acaso é um desafio, ou eu compreendi errado seu tom de arrogância?')
    print('\n')
    time.sleep(2)
    print('1. Desafiar o Curupira')
    time.sleep(1)
    print('2. Desculpar-se pelo mal-entendido')

def o_desafio():
    print('''
    Curupira: Criança tola... Você que sabe. Não ouse se arrepender de seu destino daqui pra frente. Espero mesmo que me
    mate com toda certeza, pois se restar uma gota de vida em mim, será seu fim da forma mais monstruosa que eu puder fazê-lo.
    ''')

def capitulo_3_parte_2_desafio():
    print('O Curupira cai sangrando muito e o amaldiçoa.')
    print('\n')
    time.sleep(1)
    print('Curupira: HAHAHA *cospe sangue* VOCÊ ESTÁ FADADO AGORA HAHAHAHA É O SEU FIM!')
    print('\n')
    time.sleep(2)
    print('''
    Muito sangue escorria e se apoçava pelo chão. O Curupira, já praticamente sem vida, tosse o líquido
    avermelhado algumas vezes antes de abandonar esse plano de vez. {itf.nome_jog} então passa os dedos pelo fluido no chão e
    suja o cristal, que adquire um brilho reluzente e flutua na sua mão. A joia emana uma áurea poderosa, mas a que custo...?
    ''')
    time.sleep(3)
    print('''
    No lugar que o corpo do guardião ocupava, fica apenas um cristal em forma de coração e uma capa manchada
    de sangue. A capa do próprio Curupira... A Capa de Plumas de Pássaro-Trovão.
    ''')

def capitulo_3_parte_2_perdao():
    print('''
    Curupira: Imaginei que a sabedoria não havia se esvaído por completo de ti, que iria conseguir pesar melhor suas escolhas.
    Pode explicar sua missão e o que acha necessário para chegar lá. Se eu considerar justo, concedo-lhe minha ajuda.
    ''')
    time.sleep(2)
    print(f'''
    {itf.nome_jog} explica que precisa do sangue dele, do xamã poderoso das matas, para ativar o cristal que recebera
    na batalha anterior. Explica também que suas intenções são unicamente direcionadas ao propósito do líder Kolmairt de libertar
    o reino das amarras com os demais povos aproveitadores.
    ''')
    time.sleep(3)
    print('''
    Curupira: Bem... Isso soa justamente com o que um peão de Kolmar falaria. Eu compartilho dessa meta com o líder e
    jamais me oporia à sua vontade. Apesar de nosso desentendimento à priori, compreendendo sua posição defensiva para proteger
    a integridade de sua missão. Muito honroso de sua parte firmar um compromisso com o que foi depositado sob sua confiança,
    me convenceu de suas intenções.
    ''')
    time.sleep(3)
    print('''
    Sem dar tempo de resposta, o ser lendário saca um punhal e abre um corte na mão direita, que rapidamente começa
    a pingar sangue.
    ''')
    time.sleep(1)
    print('Curupira: Venha, traga sua joia até aqui e banhe-a em meu fluido vital.')
    time.sleep(1)
    print('''
    Sem hesitar, a pessoa aventureira pega sua pedra e a põe sob as gotas que caíam da mão
    do ser a sua frente.
    ''')
    time.sleep(2)
    print('''
    Curupira: Não caia no engano de que apenas muita força de ataque será o suficiente contra o que vem a seguir.
    Não será. Você precisa garantir que os ataques do Anjo não te destruirão para que consiga ao menos utilizar o poder que está
    recebendo. Por esse motivo, darei-lhe a Capa de Plumas de Fênix, para que aumente seu nível de defesa contra o monstro que
    enfrentará, e este cristal de vida te dará o dobro de vigor em batalha... Leve também algumas poções e este alazão, ele será
    útil para que chegue em seu destino mais rapidamente. Não há tempo a perder, jovem!
    ''')
    time.sleep(4)
    print(f'''
    {itf.nome_jog}: Gratidão por compartilhar sua sabedoria comigo. Juro me fazer ter a dignidade de utilizar
    esses itens e trazer paz aos dias tenebrosos.
    ''')
    time.sleep(2)
    print(f'{itf.nome_jog} fez então uma reverência à figura de respeito que estava a sua frente.')

def capitulo_4():
    print(f'''
    Se a caminhada do Monte Coliseu havia sido exaustiva, essa seria o triplo. Graças ao cavalo que conseguira,
    poupou maiores esforços cavalgando até a entrada das cavernas. Em seu trajeto, passou por pequenos povoados hostis, que o
    atacaram mas não houvera grandes danos. Após dias e noites terríveis, finalmente chega ao portal subterrâneo e logo que adentra
    o local, nota uma certa viscosidade no chão, que , devido a penumbra no local, era difícil de definir. Era suficientemente
    escorregadia para fazer {itf.nome_jog} se desequilibrar e deslizar pelo solo adentrando a caverna.
    ''')
    time.sleep(5)
    print(f'''
    Após alguns segundos sem conseguir ver sequer um palmo à sua frente, chega a uma gruta onde havia uma intensa luz, tão reluzente
    que perdera a visão por alguns instantes até que os olhos se acostumaram com a claridade. Na gruta se viu perante uma criatura
    jamais vista antes, um olho colossal envolto por anéis repletos de olhos que orbitavam-no em movimentos circulares, ela emanava
    uma aura de serenidade e sabedoria e, apesar de não possuir uma boca, de alguma forma aquilo se comunicou com {itf.nome_jog}.
    ''')
    time.sleep(4)
    print(f'''
    ???: Saudações, {itf.nome_jog}. Estive esperando sua chegada. Você conseguiu superar minhas expectativas vindo até
    aqui : derrotando Bohyung, o caçador de tesouros, exterminando Percival, o Gladiador Fantasma e por fim conseguindo o sangue
    do Curupira, o grandioso xamã. Tudo isso só para chegar aqui e perecer como muitos antes de você. Se em algum momento sequer
    cogitou a possibilidade de me vencer, esqueça-a agora mesmo.
    ''')
    time.sleep(4)
    print('''
    Guardião do Cetro: Eu sou conhecido por muitos nomes, Guardião do Cetro, Anjo de Olho,
    Manto de Marfim... Sou um ser de grande sabedoria e através do meu olhar penetrante de sabedoria divina, posso transgredir o espaço-tempo
    e ver tudo, saber de tudo. Eu sou a figura que viu o primeiro alvorecer verá o último pôr do sol.
    ''')
    time.sleep(3)
    print(f'''
    {itf.nome_jog}: Acho que então deveria rever em toda a sua sabedoria o que realmente acontecerá, pois te garanto que já está entardecendo.
    Não cheguei aqui com a força e a confiança de tantos que acreditaram em mim para morrer agora numa caverna imunda para um bicho nojento.
    ''')
    time.sleep(3)
    print('Guardião do Cetro: Veremos.')

def vitoria():
    print('Guardião do Cetro: NÃO, EU ME RECUSO A MORRER!')
    time.sleep(1)
    print('Em um flash de luz e um zumbido ensurdecedor, a forma física do Guardião se despedaça e toda a caverna começa a tremer.')
    time.sleep(2)
    print(f'''
    O guardião em pedaços atinge o chão e sua luz se esvai conforme os seus fragmentos desaparecem.
    Sua forma se desfaz dando lugar a um reles mortal despido, que em seu último suspiro ainda encarava o cetro,
    que flutuava em direção as mãos de {itf.nome_jog}. Estava feito.
    ''')

#Epílogo

def final_bom():
    print('''
    O salão do palácio estava iluminado por tochas, criando uma atmosfera solene enquanto o guerreiro se
    aproximava do líder da revolução, Kolmairt. Com passos firmes e determinados, o guerreiro carregava o cetro milenarem suas mãos,
    um objeto de poder incomparável que representava a soberania e a esperança para o reino de Beigar.
    ''')
    time.sleep(2)
    print('''
    Kolmairt, agora reconhecido como líder justo e corajoso, aguardava com olhos brilhantes, sua postura imponente transmitindo a
    confiança que o povo depositava nele. Ele estendeu as mãos, ansioso para receber o cetro e os segredos que ele guardava.
    ''')
    time.sleep(2)
    print('''
    O guerreiro, consciente da responsabilidade que estava prestes a passar, aproximou-se e entregou o cetro a Kolmairt com respeito
    e solenidade. Uma energia pulsante e misteriosa envolvia o objeto, como se sussurrasse segredos antigos ao líder revolucionário.
    ''')
    time.sleep(2)
    print('''
    Kolmairt segurou o Cetro com reverência, sentindo a força do poder que emanava dele. Seus olhos brilharam com determinação enquanto
    ele erguia o cetro acima de sua cabeça, apresentando-o para a multidão que o observava com admiração.
    ''')
    time.sleep(2)
    print('    Kolmairt: Com o Cetro Milenar, firmaremos nossa soberania e protegeremos a liberdade conquistada com tanto sacrifício!')
    time.sleep(1)
    print('''
    Um murmúrio de assombro e apreensão percorreu o salão, pois os demais reinos sabiam que aquele objeto poderoso representava uma
    ameaça para suas ambições de conquista. O governo instaurado por Kolmairt era um governo justo, que valorizava a igualdade de todos
    os seres humanos, o que incomodava as potências vizinhas que preferiam a opressão e a tirania.
    ''')
    time.sleep(4)
    print('''
    Os ataques e invasões dos reinos vizinhos se intensificaram, revelando a ameaça que sentiam diante do exemplo de Beigar. Porém, liderados
    por Kolmairt e com o Cetro Milenar como sua fonte de poder infinito, o exército do reino resistiu bravamente. Eles defenderam suas
    terras, suas ideias de liberdade e justiça, inspirando outros a se juntarem à sua causa.
    ''')
    time.sleep(4)
    print('''
    Enquanto a batalha se desenrolava, Kolmairt usava o Cetro para invocar a energia ancestral que fluía em seu interior. Raios poderosos
    atingiam os invasores, desfazendo suas formações e abalando sua confiança. A visão do líder revolucionário, com o Cetro em suas mãos,
    espalhava o medo nos corações daqueles que desejavam dominar Beigar.
    ''')
    time.sleep(4)
    print('''
    E assim, sob a liderança corajosa de Kolmairt e com o poder do Cetro Milenar a seu lado, o reino de Beigar resistiu aos ataques,
    recuperando sua independência e firmando-se como um exemplo de justiça e liberdade para todo o continente. Os outros reinos, enfurecidos
    pela derrota e ameaçados pelos ideais de igualdade, aprenderam que a força de um povo unido em prol da liberdade é invencível.
    ''')
    time.sleep(3)
    print('''
    O reino de Beigar continuou seu caminho, mas a sombra da tragédia permaneceu, lembrando a todos que o poder e a glória podem vir
    acompanhados de responsabilidade e consequências graves.
    ''')


def final_ruim():
    print('''
    O salão real ecoava com celebrações enquanto os súditos festejavam a conquista do Cetro, o objeto poderoso que firmaria
    a soberania do reino de Beigar. O guerreiro, exaltado pela vitória, recebeu os aplausos e olhares de admiração da multidão.
    O rei, no entanto, tinha uma expressão séria e perturbada em seu rosto.
    ''')
    time.sleep(2)
    print('''
    Após a euforia inicial, o rei convocou o guerreiro para uma audiência privada em seus aposentos. A atmosfera era tensa enquanto
    o guerreiro se ajoelhava perante o monarca, aguardando suas palavras.
    ''')
    time.sleep(2)
    print('''
    Kolmairt: Você trouxe grande glória para nosso reino, guerreiro. Mas durante a batalha, você cometeu um ato imperdoável.
    Você matou meu amigo, o Curupira, o Protetor das Matas.
    ''')
    time.sleep(2)
    print('''
    O guerreiro abaixou a cabeça, consciente de sua transgressão. A tristeza se misturava à sua expressão, percebendo a gravidade
    de seu ato. O rei prosseguiu, sua voz carregada de decepção e raiva.
    ''')
    time.sleep(2)
    print('''
    Como rei, é minha responsabilidade proteger todas as criaturas que habitam nossas terras.
    O Curupira era uma entidade mágica, um guardião essencial para o equilíbrio da natureza. Sua morte é uma perda irreparável.
    ''')
    time.sleep(2)
    print('O guerreiro se levantou, buscando as palavras certas para se redimir, mas antes que pudesse falar, o rei sentenciou.')
    time.sleep(1)
    print('Kolmairt: Pelas leis do reino de Beigar, por seu ato imprudente e desrespeitoso, você será condenado à morte.')
    time.sleep(1)
    print('''
    O guerreiro olhou chocado para o rei, tentando encontrar qualquer sinal de misericórdia em seu olhar. Mas o rosto do monarca
    permanecia inabalável em sua decisão.
    ''')
    time.sleep(2)
    print('''
    A sentença foi executada, e o guerreiro enfrentou seu destino com coragem, aceitando a punição por sua falha trágica.
    A notícia se espalhou pelo reino, deixando muitos surpresos e lamentando a perda do guerreiro corajoso, mesmo em meio
    às controvérsias de suas ações.
    ''')
    time.sleep(3)
    print('''
    O rei, apesar de ter assegurado a soberania do reino de Beigar com o Cetro, carregou o peso de sua decisão para sempre.
    A perda do amigo querido e a necessidade de justiça pesavam sobre seus ombros, uma lembrança constante de como uma vitória pode
    ser manchada por um ato imprudente.
    ''')
    time.sleep(3)
    print('''
    O reino de Beigar continuou seu caminho, mas a sombra da tragédia permaneceu, lembrando a todos que o poder e a glória podem
    vir acompanhados de responsabilidade e consequências graves.
    ''')
