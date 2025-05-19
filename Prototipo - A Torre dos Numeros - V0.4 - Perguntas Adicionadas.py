from random import randint
from random import choice
from random import shuffle

from sys import exit

from time import sleep


vidas = 3


       
# introdução

print("=" * 200)
sleep(2)
print("Há muitos séculos atrás... Havia um humano considerado o maior enigmático de sua era. Ele conquistou fama resolvendo problemas que ninguém mais conseguia.")
print()
sleep(3)
print("Durante sua jornada, cruzou o caminho de pessoas invejosas, que tramaram uma emboscada. Conseguiram atordoá-lo e o aprisionaram em uma torre misteriosa — uma estrutura tão complexa que apenas os mais sábios conseguiram escapar.")
print()
sleep(3)
print("Entrar nela é fácil. Mas, uma vez lá dentro, encontrar a saída é praticamente impossível.")
sleep(3)

# base da torre

print("=" * 200)
sleep(2)
print("1 dia depois...")
print()
sleep(3)
print("O guerreiro desperta, ainda desorientado, em um lugar úmido e sombrio. Sem saber onde está, começa a avançar pela torre. Após alguns passos, ele encontra uma porta.")
print()
sleep(3)
print("Na porta, está escrito:")


formB=['⚪','🟫','📐','🪙','🪙🪙🪙','🪙🪙'] 
selform3=choice(formB[3:5])
selform2=choice(choice(formB[0:2])) 
selP=randint(1,5)
selR=randint(1,3)
pgtsB=[f'Um Sábio druida tem o dever de criar poções para pessoas doentes! Sendo {selR} doentes quantas poções precisam ser feita? ',
       f'Um Feiticeiro pediu para que seus servos buscassem um item para amaldiçoar, sendo ele {selform2}, Qual formato do objeto escolhido',
       f'Um temido rei perdeu suas miseras moedas que são {selform3} , quantas moedas ele precisa encontrar ?',
       f'Em um vilarejo havia 4 crianças brincando, pórem veio uma bruxa e levou {selR} delas ! Quantas Crianças restaram?',
       f'Um Guerreiro encontrou uma caverna com {selR} goblins, os derrotando , qual o total de Goblins derrotados?']
resp=[1,2,3]
while True:
    if selP==1:
        rB=selR
        if choice(resp)==rB:
            print(pgtsB[0])
            shuffle(resp)
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='B'or ins=='b' and resp[1]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='C'or ins=='c' and resp[2]==rB:
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP==2:
        rB=selform2 
        shuffle(formB[0:2])
        if choice(formB[0:2])==rB:
            print(pgtsB[1])
            print('='*100)
            print(f'A:{formB[0]}  B:{formB[1]} C:{formB[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and formB[0]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='B'or ins=='b' and formB[1]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='C'or ins=='c' and formB[2]==rB:
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP==3:
        shuffle(formB[3:5])
        rB=selform3
        if formB[3]==rB or formB[4]==rB or formB[5]==rB:
            print(pgtsB[2])
            print('='*100)
            print(f'A:{formB[3]}  B:{formB[4]} C:{formB[5]}  | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and formB[3]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='B'or ins=='b' and formB[4]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='C'or ins=='c' and formB[5]==rB:
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            else: 
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break      
    elif selP==4:
        rB=4-selR
        shuffle(resp)
        if choice(resp)==rB:
            print(pgtsB[3])
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='B'or ins=='b' and resp[1]==rB :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='C'or ins=='c' and resp[2]==rB:
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP==5:
        rB=selR
        if choice(resp)==rB:
            print(pgtsB[4])
            shuffle(resp)
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==selR :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='B'or ins=='b' and resp[1]==selR :
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            elif ins=='C'or ins=='c' and resp[2]==selR:
                print('Resposta Correta ! a chave esta escondida atrás da pedra na parede')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break

print()
print("=" * 200)
sleep(2)
print("O guerreiro encaixa a chave na fechadura e a porta se abre lentamente, revelando uma escadaria que leva ao próximo andar.")
print()
sleep(3)
print("Subindo...")
sleep(3)

# 1º andar

print("=" * 200)
sleep(2)
print("Ao chegar ao próximo andar, ele encontra um arqueiro.")
print()
sleep(3)
print("Arqueiro: — Não dê mais nenhum passo!")
print()
sleep(3)
print("Guerreiro: — Quem é você?")
print()
sleep(3)
print("Arqueiro: — Sou Taski, o melhor arqueiro de Maiden.")
print()
sleep(3)
print("Guerreiro: — Por que está aqui?")
print()
sleep(3)
print("Taski: — Vim a este lugar para aprimorar meus conhecimentos.")
print()
sleep(3)
print("Guerreiro: — Como alguém vem para este lugar por vontade própria?")
print()
sleep(3)
print("Taski: — Achei que seria capaz de superar a torre... mas fui frustrado.")
print()
sleep(3)
print("Taski: — Infelizmente, não consegui avançar pelo próximo andar.")           
print()
sleep(3)
print("Guerreiro: — Me leve até lá. Tentarei ajudá-lo.")      
print()
sleep(3)
print('Taski: Aqui há uma porta mágica com algo entalhado na porta ! Parece um enigma')
print()
sleep(3)
print('Guerreiro: Encontrei uma dessas anteriormente! e necessário resolver um desafio')
print()
sleep(3)
print('Na porta estava entalhada ...')
print()
sleep(3)

# Local das perguntas e respostas 
form1=['🗡️','🔨','⛏️','🪙🪙🪙','🪙🪙🪙🪙🪙','🪙🪙'] 
sefor3=choice(form1[3:5])
sefor2=choice(form1[0:2]) 
selP1=randint(1,5)
pgts1=[f'O Rei Arthur tem uma caverna feita para dragões ! Sendo {selR} o numero de celas ! Quantos Dragões podem ser acomodados la ?  ',
       f'Em uma lista tem um desenho {sefor2} , dentro de um báu tem varios itens, Qual objeto representa oque se pede ?',
       f'Um artesão cobra {sefor3} por armadura feita , quantas moedas o jovem guerreiro precisa para paga-lo ?',
       f'Em um caverna de Leões tinha 4 leões  , pórem veio uma legião e acabou com {selR} deles ! Quantas leões ainda restão restaram?',
       f'Uma elfa precisa {selR} flores de Yondu usados para poção de cura , quantas Flores você precisa encontrar ? ']
while True:
    if selP1==1:
        rB=selR
        if choice(resp)==rB:
            print(pgts1[0])
            shuffle(resp)
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='B'or ins=='b' and resp[1]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='C'or ins=='c' and resp[2]==rB:
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP1==2:
        rB=sefor2 
        shuffle(form1[0:2])
        if choice(form1[0:2])==rB:
            print(pgts1[1])
            print('='*100)
            print(f'A:{form1[0]}  B:{form1[1]} C:{form1[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and form1[0]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='B'or ins=='b' and form1[1]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='C'or ins=='c' and form1[2]==rB:
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP1==3:
        shuffle(form1[3:5])
        rB=sefor3
        if form1[3]==rB or form1[4]==rB or form1[5]==rB:
            print(pgts1[2])
            print('='*100)
            print(f'A:{form1[3]}  B:{form1[4]} C:{form1[5]}  | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and form1[3]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='B'or ins=='b' and form1[4]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='C'or ins=='c' and form1[5]==rB:
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            else: 
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break      
    elif selP1==4:
        rB=4-selR
        shuffle(resp)
        if choice(resp)==rB:
            print(pgts1[3])
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='B'or ins=='b' and resp[1]==rB :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='C'or ins=='c' and resp[2]==rB:
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
    elif selP1==5:
        rB=selR
        if choice(resp)==rB:
            print(pgts1[4])
            shuffle(resp)
            print('='*100)
            print(f'A:{resp[0]}  B:{resp[1]} C:{resp[2]}   | Vidas={vidas} ')
            ins=(input('Qual a resposta ? >>  '))
            if ins=='A'or ins=='a' and resp[0]==selR :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='B'or ins=='b' and resp[1]==selR :
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            elif ins=='C'or ins=='c' and resp[2]==selR:
                print('Resposta Correta ! A porta ira se abrir !!')
                break
            else:
                print('Resposta Errada , tente Novamente')
                vidas-=1
                print('='*100)
            if vidas==0:
                print('='*100)
                print('Você perdeu !!')
                break
# 2º andar

print("=" * 200)
sleep(2)
print("O guerreiro e Taski sobem mais um lance de escadas e chegam a um novo ambiente surpreendente.")
print()
sleep(3)
print("Estão em meio a um bosque dentro da torre.")
print()
sleep(3)
print("Árvores altas crescem entre pedras e raízes antigas. Há musgos, pequenas flores e o som distante de água correndo. A luz entra por rachaduras no teto, criando feixes que dançam no ar, misturando-se com partículas de poeira mágica.")
print()
sleep(3)
print("Guerreiro: — Árvores... aqui dentro? Isso desafia toda a lógica.")
print()
sleep(3)
print("Taski: — Já vi coisas estranhas, mas isso... isso é outro nível.")
print()
sleep(3)
print("Diante deles, uma árvore com casca retorcida carrega duas setas cravadas:")
print()
sleep(3)
print("Uma aponta para um caminho escuro, tomado por névoa e raízes retorcidas.")
print()
sleep(3)
print("A outra, para um caminho claro, com flores brilhantes e trilhos de luz no chão.")
print()
sleep(3)
print("Taski encara o guerreiro e diz:")
print()
sleep(3)
print("Taski: — Então... qual caminho escolheremos?")
print()
sleep(3)

print("=" * 200)
sleep(2)
print(">> Escolha qual caminho prosseguir:")
print()
sleep(2)
print("> 🌓 A - Caminho Escuro | Alta Dificuldade / Recompesas Valiosas / Perigoso")
print()
sleep(2)
print("> 🌞 B - Caminho Claro | Baixa Dificuldade / Recompensa Minima / Pacifico sem danos")
sleep(2)
print("=" * 200)
escolha1 = input("> ")
print("=" * 200)
sleep(2)
if(escolha1 != "A" and escolha1 != "a" and escolha1 != "B" and escolha1 != "b"):
    while(escolha1 != "A" and escolha1 != "a" and escolha1 != "B" and escolha1 != "b"):
        print("Escolha entre A ou B.")
        sleep(2)
        print("=" * 200)
        sleep(2)
        print(">> Escolha qual caminho prosseguir:")
        print()
        sleep(2)
        print("> 🌓 A - Caminho Escuro ")
        print()
        sleep(2)
        print("> 🌞 B - Caminho Claro ")
        print("=" * 200)
        escolha1 = input("> ")
        print("=" * 200)
        sleep(2)

# 2º andar - Caminho escuro

if(escolha1 == "A" or escolha1 == "a"):
    print(">> Você escolheu 🌓 A - Caminho Escuro.")
    sleep(2)
    print("=" * 200)
    sleep(2)
    print("O caminho é apertado. Galhos secos parecem se mover sozinhos. O ar fica pesado, e a névoa densa cobre o chão.")
    print()
    sleep(3)
    print("Depois de alguns metros, eles encontram uma estátua com olhos vermelhos brilhando. Ela fala:")
    print()
    sleep(3)
    print('Estatua - Bem vindo ao Destino Sombrio ! Aqui apesar de denso e escuro pode trazer tremenda Recompensa !')
    print()
    sleep(3)
    print('Estatua - Aqui apresento um de 2 desafios ! Desafios complexos que se concluidos , tera uma recompensa genuina !!')
    print()
    sleep(3)
    print('Estatua - Passe pelo portão escuro a sua frente e tera seu desafio !')
    print()
    sleep(3)
    #Area de Pergunta
    pgt2=[f'Em sua frente se materializou um baú negro esfumaçado , cravejado por Rubis, trancado por um mecanismo onde apenas a voz sussurar o numero correto ! ',
          f'Após passar o portão uma fumaça se dissipa se mostrando um Espectro com uma tunica negra e aparência esqueletica ']
    spgt2=choice(pgt2)
    if spgt2==pgt2[0]:
     while True:
            grito=int(input('Guerreiro - o numero é    '))
            if grito== 12:
                print('Taski - Acho que deu certo , o báu esta abrindo !')
                print()
                sleep(3)
                print('O guerreiro e Taski encontram uma pedra brilhante dentro do baú que ao pegar algo acontece...')
                break
            else:
                print('Taski - Aparentemente não aconteceu nada ! Pensa melhor e tenta denovo')
                vidas-=1
                print('='*100)
    if spgt2==pgt2[1]:
            print(pgt2[1])
            print()
            sleep(3)
            print('Espectro - Você não e bem vindo aqui !! Resolva o enigma e passe , falhe e caira na escuridão  eterna !!')
            print()
            sleep(3)
            print('O Espectro faz um mural subir do chão com sua magia , nela esta entalhado o determinado enigma :')
            print('='*100)
            print('Se multiplicares o número de luas no céu pela quantidade de esferas negras em meu dominio , obterás o numero secreto !! Há 5 luas no céu e 3 esferas negras em meu dominio !')
            print()
            sleep(3)
            print('Taski - Uma questão de multiplicação ! fique atento')
            print()
            sleep(3)
            while True:
                r2=int(input('Guerreiro - A resposta do enigma é    '))
                if r2==15:
                    print()
                    print('Espectro - Esta correto ! Va agora você e seu amigo ladino o mais rapido antes que me arrependa !')
                    print()
                    sleep(3)
                    print('O Espectro abre o caminho entre as nevoas !')
                    break
                else:
                    print(f'Espectro - Incorreto ! HA HA HA HA ! Vejo que não durara muito por aqui , vejo que so tem {vidas} sobrando ! Tente novamente com cautela !')
                    print()
                    print('Taski - Como ele pode saber disso ?')
                    vidas-=1
    print("=" * 200)
    sleep(2)
    print("A névoa desaparece.")
    print()
    sleep(3)
    print("A estátua se desativa.")
    print()
    sleep(3)
    print("Um portal de raízes se abre, levando ao próximo trecho da torre.")

# 2º andar - Caminho claro

if(escolha1 == "B" or escolha1 == "b"):
    print(">> Você escolheu 🌞 B - Caminho Claro.")
    sleep(2)
    print("=" * 200)
    sleep(2)
    print("Flores luminosas guiam o caminho. O ambiente é silencioso, calmo... talvez calmo até demais.")
    print()
    sleep(3)
    print("No fim da trilha, há uma fonte de pedra, com água cristalina. Acima dela, um espelho flutuante gira lentamente.")
    print()
    sleep(3)
    print('Dele sai uma mulher com vestido dourado e uma coroa de flores brilhantes !')
    print()
    sleep(3)
    print('Mulher Brilhante - Boas Vindas ao Vale Luminoso , Sou Ariandel , Rainha do Vale Luminoso ! Para atravessar meu vale ate a saída deve resolver alguns enigmas ao longo dele ! 2 Possveis enigmas ao longo do caminho')
    print()
    sleep(3)
    print('Ariandel - Mas fique tranquilo é um bosque pacifico , porém não espere nenhuma recompensa muito generosa , nós do vale Luminoso somos bem humildes ! O Rei da Torre dos Numeros não nos da recursos por facilitarmos o caminho dos pobres coitados que passam por aqui !')
    print()
    sleep(4)
    print('Ariandel - Siga pelo vale a frente , e encontrara um enigma ! Para passar deve resolve-lo ! Caso errar não se preocupe não sofrera Danos !')
    print()
    sleep(3)
    print("Um arco de flores se abre, revelando uma ponte suspensa entre galhos gigantes.")
    print()
    sleep(3)
    #Area de Pergunta 
    pgtvl=['Atravessando a ponte Taski e o Guerreiro se deparam com um pedestal brilhante com um livro sobre ele',
            'Atravessando a ponte Taski e o Guerreiro se deparam com um Paladino de armadura brilhante como as vestes de Ariandel']
    spgtvl=choice(pgtvl)
    if spgtvl==pgtvl[0]:
        print()
        sleep(3)
        print(pgtvl[0])
        print()
        sleep(3)
        print('O Livro se abre sozinho folheando as paginas, abrindo em uma especifica!')
        print()
        sleep(3)
        print('Nesta página contem um desenho de sete estrelas luminosas , Três luas prateadas desenhadas na página ao lado')
        print()
        sleep(3)
        print('Ao lado do livro aberto há uma Pena dentro de um pote de tinta , para poder escrever algo aparentemente')
        print()
        sleep(3)
        print('Taski - Aparentemente a pena é para escrever a soma do número que simboliza os desenhos , tem um espaço em branco embaixo da página, acredito que se escrever a resposta correta poderemos passar !')
        print()
        sleep(3)
        while True:
         r3=int('Guerreiro - Pois bem vou escrever a resposta    ')
         if r3==10:
            print('Guerreiro escreve o número e o livro se embaralha e se fecha ! O pedestal começa descer abrindo um caminho entre as arvores que bloqueavam o caminho! Taski e o Guerreiro atravessam !')
            break
         else:
             print('O livro apaga a tinta e nada acontece!')
             print()
             sleep(3)
             print('Acredito que não tenha funcionado , Tenta denovo')
    if spgtvl==pgtvl[1]:
        print()
        sleep(3)
        print('Atrás dele se encontrava um portão brilhante , Taski e o Guerreiro se aproximam do Paladino , que apenas bate seu enorme escudo e lança no chão. ')
        print()
        sleep(3)
        print('Paladino - Parados ! Sou Freyior guardião do vale Luminoso , para terem direito a passar devem resolver um enigma ! ')
        print()
        sleep(3)
        print('Freyior - Em meu escudo se esconde quatro luas , na haste de minha lança três sois ! Se somados me dão o poder ! Qual o poder maior que protege essas terras ? ')
        print()
        sleep(3)
        print('Taski - Aparentemente um enigma de soma ! Pode ser tranquilo ')
        print()
        sleep(3)
        while True:
            r4=int(input('Guerreiro - O pode maior que protege as terras é '))
            if r4==7:
                 print('Freyior - Esta correto ! Você pode seguir !!')
                 print()
                 sleep(3)
                 print('O Paladino abre caminho e eles passam pelo portão brilhante !')
                 print()
                 sleep(3)
                 break
            else:
                  print('Freyior - Esta incorreto ! Tente novamente !!')
                  print()
                  sleep(3)
                  print('Taski - Vamos la ! E um enigma de soma e tranquilo ! Sorte que não nos puniram pelos erros !')
    print("Ao completar o desafio de seu caminho, o guerreiro e Taski se deparam com uma escada de cipós que leva para o 3º andar.")
    print()
    sleep(3)
    print("Taski: — Seja qual for o propósito desta torre... ela nos testa de todas as formas possíveis.")

print()
sleep(3)
print("Subindo...")
sleep(3)

# 3º andar

print("=" * 200)
sleep(2)
print("Após subirem os cipós do bosque encantado, o guerreiro e Taski chegam a um corredor silencioso. As paredes ao redor são revestidas com espelhos altos, antigos, que refletem suas imagens com um leve atraso, como se houvesse algo de errado com o tempo ali dentro.")
print()
sleep(3)
print("Taski olha em volta, inquieto, e diz:")
print()
sleep(3)
print("Taski: — Isso está me deixando nervoso... os reflexos não estão certos.")
print()
sleep(3)
print("Conforme caminham, os espelhos começam a exibir imagens distorcidas: o guerreiro chorando, Taski ferido, os dois fugindo. Nenhuma delas parece real, mas todas causam desconforto.")
print()
sleep(3)
print("Ao final do corredor, uma porta de madeira escura surge, com uma trava em forma de espelho partido. Gravado acima dela está o seguinte texto:")
print()
sleep(3)
print('"A verdade liberta. O engano te aprisiona."')
print()
sleep(3)
print("A trava brilha e uma pergunta aparece diante deles:")
print()
sleep(3)
print('"O que mais revela sobre uma pessoa?"')
print()
sleep(3)
print("As opções se formam em símbolos flutuantes:")
print()
sleep(3)
print("A - Suas vitórias")
print()
sleep(3)
print("B - Suas escolhas")
print()
sleep(3)
print("C - Sua aparência")
print()
sleep(3)
print("Taski observa a pergunta, pensativo, e diz.")
print()
sleep(3)
print("Taski: — Não é o que a gente conquista... mas o que a gente escolhe fazer.")
sleep(3)

print("=" * 200)
sleep(2)
print('>> Desafio 3: "O que mais revela sobre uma pessoa?". Escolha a alternativa que responda corretamente a pergunta.')
print()
sleep(2)
print("> Vidas:", vidas)
print()
sleep(2)
print("A - Suas vitórias.       ", end="")
print("B - Suas escolhas.       ", end="")
print("C - Sua aparência.")
sleep(2)
print("=" * 200)
resposta3 = input("> ")
print("=" * 200)
sleep(2)
if(resposta3 != "A" or resposta3 != "a" or resposta3 != "B" or resposta3 != "b" or resposta3 != "C" or resposta3 != "c"):
    while(resposta3 != "A" and resposta3 != "a" and resposta3 != "B" and resposta3 != "b" and resposta3 != "C" and resposta3 != "c"):
        print("Escolha entre alternativas A, B ou C.")
        sleep(2)
        print("=" * 200)
        sleep(2)
        print('>> Desafio 3: "O que mais revela sobre uma pessoa?". Escolha a alternativa que responda corretamente a pergunta.')
        print()
        sleep(2)
        print("> Vidas:", vidas)
        print()
        sleep(2)
        print("A - Suas vitórias.       ", end="")
        print("B - Suas escolhas.       ", end="")
        print("C - Sua aparência.")
        sleep(2)
        print("=" * 200)
        resposta3 = input("> ")
        print("=" * 200)
        sleep(2)
if(resposta3 == "B" or resposta3 == "b"):
    print("> Vidas:", vidas)
    print()
    sleep(2)
    print(">> Respota correta!")
    sleep(2)
else:
    vidas -= 1
    while(vidas >= 1):
        print("Ao tocar o símbolo errado, a porta libera uma pequena explosão de luz, empurrando-os para trás e o guerreiro perde uma vida.")
        print()
        sleep(2)
        print("Resposta errada. Tente novamente.")
        sleep(2)
        print("=" * 200)
        sleep(2)
        print('>> Desafio 3: "O que mais revela sobre uma pessoa?". Escolha a alternativa que responda corretamente a pergunta.')
        print()
        sleep(2)
        print("> Vidas:", vidas)
        print()
        sleep(2)
        print("A - Suas vitórias.       ", end="")
        print("B - Suas escolhas.       ", end="")
        print("C - Sua aparência.")
        sleep(2)
        print("=" * 200)
        resposta3 = input("> ")
        print("=" * 200)
        sleep(2)
        if(resposta3 != "A" or resposta3 != "a" or resposta3 != "B" or resposta3 != "b" or resposta3 != "C" or resposta3 != "c"):
            while(resposta3 != "A" and resposta3 != "a" and resposta3 != "B" and resposta3 != "b" and resposta3 != "C" and resposta3 != "c"):
                print("Escolha entre alternativas A, B ou C.")
                sleep(2)
                print("=" * 200)
                sleep(2)
                print('>> Desafio 3: "O que mais revela sobre uma pessoa?". Escolha a alternativa que responda corretamente a pergunta.')
                print()
                sleep(2)
                print("> Vidas:", vidas)
                print()
                sleep(2)
                print("A - Suas vitórias.       ", end="")
                print("B - Suas escolhas.       ", end="")
                print("C - Sua aparência.")
                sleep(2)
                print("=" * 200)
                resposta3 = input("> ")
                print("=" * 200)
                sleep(2)
        if(resposta3 == "B" or resposta3 == "b"):
            break
        vidas -= 1
    if(vidas >= 1):
        print("> Vidas:", vidas)
        print()
        sleep(2)
        print(">> Resposta correta!")
        sleep(2)
    else:
        print("> Vidas:", vidas)
        print()
        sleep(2)
        print("Acabaram suas vidas! Fim de jogo.")
        sleep(2)
        print("=" * 200)
        exit()

print("=" * 200)
sleep(2)
print("A trava se desfaz em luz e a porta se abre lentamente. Um vento leve sopra do outro lado.")
print()
sleep(3)
print("Taski sorrindo aliviado, diz:")
print()
sleep(3)
print("Taski: — Parece que estamos começando a entender os segredos dessa torre.")
print()
sleep(3)
print("Ao passarem pela porta, encontram uma sala silenciosa e limpa. No centro, uma escada em espiral leva ao próximo andar.")
print()
sleep(3)
print("Taski: — Esses desafios estão ficando cada vez mais pessoais...")
print()
sleep(3)
print("Guerreiro: — E a torre parece saber quem somos...")
print()
sleep(3)
#4 Andar - Torre do chefe final. 

print('Taski e o Guerreiro chegam no que parece ser o ultimo andar da torre !')
print()
sleep(3)
print('Um enorme saguão com um trono vazio no meio ! não fazia sentido parecia ate mesmo um palácio , um tapete vermelho levava até o centro !')
print()
sleep(3)
print('Atrás do trono um enorme espelho , refletia visão de fora , uma saída !!')
print()
sleep(3)
print('Guerreiro - Olha Taski uma saída finalmente!')
print()
sleep(3)
print('O Guerreiro começa a camkinhar até o trono , porém Taski pede para que pare ! o Guerreiro sem entender para e se vira para Taski !')
print()
sleep(3)
print('Taski - Sinto muito ! Mas achou mesmo que seria assim tão simples ?')
print()
sleep(3)
print('Guerreiro - Não estou entendendo Taski ! Oque quer dizer ? - Diz o guerreiro olhando desconfiado.')
print()
sleep(3)
print('Taski - Você ainda não entendeu ! - Taski começa a se transfigurar em fumaça se tornando um velho com barba branca , tunica e vestes de mago ')
print()
sleep(3)
print('Guerreiro - Quem é você ? - pergunta o guerreiro desenbaiando sua espada')
print()
sleep(3)
print('Velho - Sinto muito garoto ! Você é parte de algo maior ! Sou Merlin , mago antigo conselheiro direto de seu pai Arthur !')
print()
sleep(3)
print('Guerreiro - Oque você quer comigo Merlin ! Porque me trouxe até aqui ?')
print()
sleep(3)
print('Merlin - Seu pai perdeu o pulso firme , deixou o reino ser tomado ! Ele é um fraco por se abrir a nossos inimigos !')
print()
sleep(3)
print('Guerreiro - Meu pai é honrado ! Ele quis os povos unidos para termos prosperidade !')
print()
sleep(3)
print('Merlin - Ele não tem visão ! Esta cego e você sofre ! Você esta perdido aqui e ele nem se moveu !')
print()
sleep(3)
print('Guerreiro - Esta errado isso ! Com certeza deve ter uma legião atrás de mim !')
print()
sleep(3)
print('Merlin - se não crê em mim ! Resolva um ultimo e mais arduo enigma e te deixarei sair ! Pois eu sou o Rei da Torre dos Numeros !')
print()
sleep(3)
print('Guerreiro - Pois bem diga !!')
print()
sleep(3)
print('Merlin - Eis o Enigma do Rei ! - "Tenho um número misterioso , Se você multiplica-lo por 4 e depois subtrair 6 , o resultado será 14 ! Qual é esse numero ?"')
print()
sleep(3)
rF=int(input('Guerreiro - O numero é   '))
while True:
    if rF==5:
        print()
        sleep(3)
        print('Merlin - Muito Bem ! - Diz Merlin batendo palma - Pois bem pode sair ! Veja a preocupação de seu pai o Grande Rei Arthur !')
        print()
        sleep(3)
        print('Guerreiro - Tenho certeza que sim ! - Diz ele se virando ao trono e indo em direção ao espelho enorme que havia se tornado um portal.')
        print()
        sleep(3)
        print('Merlin - Vai se surpreender com o caminho que ainda te espera ... Mordred ')
        print()
        sleep(3)
        print('FIM')
        break
    else:
        print()
        sleep(3)
        print('Merlin - Engraçado ! Achei que era mais inteligente ! E dificil sem seu amigo ... "Taski - Arqueiro de Maiden" para ajudar - Diz ele rindo')
        vidas-=1
