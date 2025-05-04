from random import randint

from sys import exit

vidas = 3

sorteio1 = randint(1,3)
if(sorteio1 == 1):
    forma = "círculo"
elif(sorteio1 == 2):
    forma = "quadrado"
elif(sorteio1 == 3):
    forma = "triângulo"

# introdução

print("=" * 200)
print("Há muitos séculos atrás... Havia um humano considerado o maior enigmático de sua era. Ele conquistou fama resolvendo problemas que ninguém mais conseguia.")
print()
print("Durante sua jornada, cruzou o caminho de pessoas invejosas, que tramaram uma emboscada. Conseguiram atordoá-lo e o aprisionaram em uma torre misteriosa — uma estrutura tão complexa que apenas os mais sábios conseguiram escapar.")
print()
print("Entrar nela é fácil. Mas, uma vez lá dentro, encontrar a saída é praticamente impossível.")

# base da torre

print("=" * 200)
print("1 dia depois...")
print()
print("O guerreiro desperta, ainda desorientado, em um lugar úmido e sombrio. Sem saber onde está, começa a avançar pela torre. Após alguns passos, ele encontra uma porta.")
print()
print("Na porta, está escrito:")
print()
print(f'"A chave para a porta possui a forma de um {forma}."')
print()
print(f"Ao observar a fechadura, nota que há um encaixe com o formato exato para um {forma}.")
print()
print("Ele olha ao redor e encontra alguns itens espalhados pelo chão.")

print("=" * 200)
print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
print()
print("> Vidas:", vidas)
print()
print("A - 🔴   ", end="")
print(" B - 🟥   ", end="")
print(" C - 🔺")
print("=" * 200)
resposta1 = input("> ")
print("=" * 200)
if(resposta1 != "A" or resposta1 != "a" or resposta1 != "B" or resposta1 != "b" or resposta1 != "C" or resposta1 != "c"):
    while(resposta1 != "A" and resposta1 != "a" and resposta1 != "B" and resposta1 != "b" and resposta1 != "C" and resposta1 != "c"):
        print("Escolha entre alternativas A, B ou C.")
        print("=" * 200)
        print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
        print()
        print("> Vidas:", vidas)
        print()
        print("A - 🔴   ", end="")
        print(" B - 🟥   ", end="")
        print(" C - 🔺")
        print("=" * 200)
        resposta1 = input("> ")
        print("=" * 200)
if(resposta1 == "A" or resposta1 == "a"):
        resposta1 = "círculo"
elif(resposta1 == "B" or resposta1 == "b"):
        resposta1 = "quadrado"
elif(resposta1 == "C" or resposta1 == "c"):
    resposta1 = "triângulo"
if(resposta1 == forma):
    print("> Vidas:", vidas)
    print()
    print(">> Respota correta!")
else:
    vidas -= 1
    while(vidas >= 1):
        print("Resposta errada. Tente novamente.")
        print("=" * 200)
        print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
        print()
        print("> Vidas:", vidas)
        print()
        print("A - 🔴   ", end="")
        print(" B - 🟥   ", end="")
        print(" C - 🔺")
        print("=" * 200)
        resposta1 = input("> ")
        print("=" * 200)
        if(resposta1 != "A" or resposta1 != "a" or resposta1 != "B" or resposta1 != "b" or resposta1 != "C" or resposta1 != "c"):
            while(resposta1 != "A" and resposta1 != "a" and resposta1 != "B" and resposta1 != "b" and resposta1 != "C" and resposta1 != "c"):
                print("Escolha entre alternativas A, B ou C.")
                print("=" * 200)
                print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
                print()
                print("> Vidas:", vidas)
                print()
                print("A - 🔴   ", end="")
                print(" B - 🟥   ", end="")
                print(" C - 🔺")
                print("=" * 200)
                resposta1 = input("> ")
                print("=" * 200)
        if(resposta1 == "A" or resposta1 == "a"):
                resposta1 = "círculo"
        elif(resposta1 == "B" or resposta1 == "b"):
                resposta1 = "quadrado"
        elif(resposta1 == "C" or resposta1 == "c"):
            resposta1 = "triângulo"
        if(resposta1 == forma):
            break
        vidas -= 1
    if(vidas >= 1):
        print("> Vidas:", vidas)
        print()
        print(">> Resposta correta!")
    else:
        print("> Vidas:", vidas)
        print()
        print("Acabaram suas vidas! Fim de jogo.")
        print("=" * 200)
        exit()

print("=" * 200)
print("Ele encaixa a chave na fechadura e a porta se abre lentamente, revelando uma escadaria que leva ao próximo andar.")
print()
print("Subindo...")

# 1º andar

print("=" * 200)
print("Ao chegar ao próximo andar, o guerreiro encontra um arqueiro.")
print()
print("Arqueiro: — Não dê mais nenhum passo!")
print()
print("Jogador: — Quem é você?")
print()
print("Arqueiro: — Sou Taski, o melhor arqueiro de Maiden.")
print()
print("Jogador: — Por que está aqui?")
print()
print("Taski: — Vim a este lugar para aprimorar meus conhecimentos.")
print()
print("Jogador: — Como alguém vem para este lugar por vontade própria?")
print()
print("Taski: — Achei que seria capaz de superar a torre... mas fui frustrado.")
print()
print("Taski: — Infelizmente, não consegui passar da porta deste andar.")
print()
print("Jogador: — Me leve até ela. Tentarei ajudá-lo.")
print()
print("O jogador chega à porta e encontra um novo desafio escrito:")
print()

# 2º andar

print("=" * 200)
print("O jogador e Taski sobem mais um lance de escadas e chegam a um novo ambiente surpreendente.")
print()
print("Estão em meio a um bosque dentro da torre.")
print()
print("Árvores altas crescem entre pedras e raízes antigas. Há musgos, pequenas flores e o som distante de água correndo. A luz entra por rachaduras no teto, criando feixes que dançam no ar, misturando-se com partículas de poeira mágica.")
print()
print("Jogador: — Árvores... aqui dentro? Isso desafia toda a lógica.")
print()
print("Taski: — Já vi coisas estranhas, mas isso... isso é outro nível.")
print()
print("Diante deles, uma árvore com casca retorcida carrega duas setas cravadas:")
print()
print("Uma aponta para um caminho escuro, tomado por névoa e raízes retorcidas.")
print()
print("A outra, para um caminho claro, com flores brilhantes e trilhos de luz no chão.")
print()
print("Taski encara o jogador e diz:")
print()
print("Taski: — Então... qual caminho escolheremos?")
print()

print("=" * 200)
print(">> Escolha qual caminho prosseguir:")
print()
print("> 🌓 A - Caminho Escuro")
print()
print("> 🌞 B - Caminho Claro")
print("=" * 200)
escolha1 = input("> ")
print("=" * 200)
if(escolha1 != "A" and escolha1 != "a" and escolha1 != "B" and escolha1 != "b"):
    while(escolha1 != "A" and escolha1 != "a" and escolha1 != "B" and escolha1 != "b"):
        print("Escolha entre A ou B.")
        print("=" * 200)
        print(">> Escolha qual caminho prosseguir:")
        print()
        print("> 🌓 A - Caminho Escuro")
        print()
        print("> 🌞 B - Caminho Claro")
        print("=" * 200)
        escolha1 = input("> ")
        print("=" * 200)

# 2º andar - Caminho escuro

if(escolha1 == "A" or escolha1 == "a"):
    print(">> Você escolheu 🌓 A  -Caminho Escuro.")
    print("=" * 200)
    print("O caminho é apertado. Galhos secos parecem se mover sozinhos. O ar fica pesado, e a névoa densa cobre o chão.")
    print()
    print("Depois de alguns metros, eles encontram uma estátua com olhos vermelhos brilhando. Ela fala:")
    print()
    print('"A sabedoria guia os passos do justo. Três símbolos te mostro, apenas um é justo. Escolha com clareza, ou a névoa será seu fim."')
    print()
    print("No chão surgem três símbolos:")
    print()
    print("👁 Um olho aberto.")
    print()
    print("🐍 Uma serpente enrolada.")
    print()
    print("⚖ Uma balança desequilibrada.")
    print()
    print("Taski: — Isso parece um teste de julgamento...")

    print("=" * 200)
    print('>> Desafio 2: "Vejo sem julgar, mas mesmo cega sou justa. Aquele que tudo enxerga, pode tudo enganar. O verdadeiro caminho é o da justiça, mesmo imperfeita.". Escolha a alternativa que corresponda com o enigma.')
    print()
    print("> Vidas:", vidas)
    print()
    print("A - 👁 Olho     ", end="")
    print("B - 🐍 Serpente     ", end="")
    print("C - ⚖ Balança")
    print("=" * 200)
    resposta2 = input("> ")
    print("=" * 200)
    if(resposta2 != "A" or resposta2 != "a" or resposta2 != "B" or resposta2 != "b" or resposta2 != "C" or resposta2 != "c"):
        while(resposta2 != "A" and resposta2 != "a" and resposta2 != "B" and resposta2 != "b" and resposta2 != "C" and resposta2 != "c"):
            print("Escolha entre alternativas A, B ou C.")
            print("=" * 200)
            print('>> Desafio 2: "Vejo sem julgar, mas mesmo cega sou justa. Aquele que tudo enxerga, pode tudo enganar. O verdadeiro caminho é o da justiça, mesmo imperfeita.". Escolha a alternativa que corresponda com o enigma.')
            print()
            print("> Vidas:", vidas)
            print()
            print("A - 👁 Olho     ", end="")
            print("B - 🐍 Serpente     ", end="")
            print("C - ⚖ Balança")
            print("=" * 200)
            resposta2 = input("> ")
            print("=" * 200)
    if(resposta2 == "C" or resposta2 == "c"):
        print("> Vidas:", vidas)
        print()
        print(">> Respota correta!")
    else:
        vidas -= 1
        while(vidas >= 1):
            print("Resposta errada. Tente novamente.")
            print("=" * 200)
            print('>> Desafio 2: "Vejo sem julgar, mas mesmo cega sou justa. Aquele que tudo enxerga, pode tudo enganar. O verdadeiro caminho é o da justiça, mesmo imperfeita.". Escolha a alternativa que corresponda com o enigma.')
            print()
            print("> Vidas:", vidas)
            print()
            print("A - 👁 Olho     ", end="")
            print("B - 🐍 Serpente     ", end="")
            print("C - ⚖ Balança")
            print("=" * 200)
            resposta2 = input("> ")
            print("=" * 200)
            if(resposta2 != "A" or resposta2 != "a" or resposta2 != "B" or resposta2 != "b" or resposta2 != "C" or resposta2 != "c"):
                while(resposta2 != "A" and resposta2 != "a" and resposta2 != "B" and resposta2 != "b" and resposta2 != "C" and resposta2 != "c"):
                    print("Escolha entre alternativas A, B ou C.")
                    print("=" * 200)
                    print('>> Desafio 2: "Vejo sem julgar, mas mesmo cega sou justa. Aquele que tudo enxerga, pode tudo enganar. O verdadeiro caminho é o da justiça, mesmo imperfeita.". Escolha a alternativa que corresponda com o enigma.')
                    print()
                    print("> Vidas:", vidas)
                    print()
                    print("A - 👁 Olho     ", end="")
                    print("B - 🐍 Serpente     ", end="")
                    print("C - ⚖ Balança")
                    print("=" * 200)
                    resposta2 = input("> ")
                    print("=" * 200)
            if(resposta2 == "C" or resposta2 == "c"):
                break
            vidas -= 1
        if(vidas >= 1):
            print("> Vidas:", vidas)
            print()
            print(">> Resposta correta!")
        else:
            print("> Vidas:", vidas)
            print()
            print("Acabaram suas vidas! Fim de jogo.")
            print("=" * 200)
            exit()
    print("=" * 200)
    print("A névoa desaparece.")
    print()
    print("A estátua se desativa.")
    print()
    print("Um portal de raízes se abre, levando ao próximo trecho da torre.")

# 2º andar - Caminho claro

if(escolha1 == "B" or escolha1 == "b"):
    print(">> Você escolheu 🌞 B - Caminho Claro.")
    print("=" * 200)
    print("Flores luminosas guiam o caminho. O ambiente é silencioso, calmo... talvez calmo até demais.")
    print()
    print("No fim da trilha, há uma fonte de pedra, com água cristalina. Acima dela, um espelho flutuante gira lentamente.")
    print()
    print("Assim que se aproximam, o espelho brilha e projeta três reflexos diferentes do jogador — cada um com um detalhe sutilmente errado, e diz:")
    print()
    print('"Aquele que conhece a si mesmo pode seguir. Três faces vêem a luz, apenas uma é real. Toque o reflexo verdadeiro — ou fique aqui para sempre."')
    print()
    print("🍎 | 🍊")
    print()
    print("🍎 | 🍌")
    print()
    print("🍎 | 🍎")
    print()
    print("Taski olha para os reflexos e diz:")
    print()
    print("Taski: — Preste atenção nos reflexos. Um deles é idêntico, os outros são diferentes.")
    
    print("=" * 200)
    print(">> Desafio 2: Escolha a alternativa que tenha o reflexo idêntico.")
    print()
    print("> Vidas:", vidas)
    print()
    print("A - 🍎 | 🍊     ", end="")
    print("B - 🍎 | 🍌     ", end="")
    print("C - 🍎 | 🍎")
    print("=" * 200)
    resposta2 = input("> ")
    print("=" * 200)
    if(resposta2 != "A" or resposta2 != "a" or resposta2 != "B" or resposta2 != "b" or resposta2 != "C" or resposta2 != "c"):
        while(resposta2 != "A" and resposta2 != "a" and resposta2 != "B" and resposta2 != "b" and resposta2 != "C" and resposta2 != "c"):
            print("Escolha entre alternativas A, B ou C.")
            print("=" * 200)
            print(">> Desafio 2: Escolha a alternativa que tenha o reflexo idêntico.")
            print()
            print("> Vidas:", vidas)
            print()
            print("A - 🍎 | 🍊     ", end="")
            print("B - 🍎 | 🍌     ", end="")
            print("C - 🍎 | 🍎")
            print("=" * 200)
            resposta2 = input("> ")
            print("=" * 200)
    if(resposta2 == "C" or resposta2 == "c"):
        print("> Vidas:", vidas)
        print()
        print(">> Respota correta!")
    else:
        vidas -= 1
        while(vidas >= 1):
            print("Resposta errada. Tente novamente.")
            print("=" * 200)
            print(">> Desafio 2: Escolha a alternativa que tenha o reflexo idêntico.")
            print()
            print("> Vidas:", vidas)
            print()
            print("A - 🍎 | 🍊     ", end="")
            print("B - 🍎 | 🍌     ", end="")
            print("C - 🍎 | 🍎")
            print("=" * 200)
            resposta2 = input("> ")
            print("=" * 200)
            if(resposta2 != "A" or resposta2 != "a" or resposta2 != "B" or resposta2 != "b" or resposta2 != "C" or resposta2 != "c"):
                while(resposta2 != "A" and resposta2 != "a" and resposta2 != "B" and resposta2 != "b" and resposta2 != "C" and resposta2 != "c"):
                    print("Escolha entre alternativas A, B ou C.")
                    print("=" * 200)
                    print(">> Desafio 2: Escolha a alternativa que tenha o reflexo idêntico.")
                    print()
                    print("> Vidas:", vidas)
                    print()
                    print("A - 🍎 | 🍊     ", end="")
                    print("B - 🍎 | 🍌     ", end="")
                    print("C - 🍎 | 🍎")
                    print("=" * 200)
                    resposta2 = input("> ")
                    print("=" * 200)
            if(resposta2 == "C" or resposta2 == "c"):
                break
            vidas -= 1
        if(vidas >= 1):
            print("> Vidas:", vidas)
            print()
            print(">> Resposta correta!")
        else:
            print("> Vidas:", vidas)
            print()
            print("Acabaram suas vidas! Fim de jogo.")
            print("=" * 200)
            exit()
    print("=" * 200)
    print("O espelho se desfaz em luz.")
    print()
    print("Um arco de flores se abre, revelando uma ponte suspensa entre galhos gigantes.")
    print()
    print("Ao completar o desafio de seu caminho, o jogador e Taski se reencontram em uma área comum — uma escada de cipós que leva para o 3º andar.")
    print()
    print("Taski: — Seja qual for o propósito desta torre... ela nos testa de todas as formas possíveis.")
print()
print("Subindo...")