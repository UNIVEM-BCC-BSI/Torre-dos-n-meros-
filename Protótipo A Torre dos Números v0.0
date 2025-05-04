# introdução

print("=" * 262)

print("Há muitos séculos atrás... Havia um humano considerado o maior enigmático de sua era. Ele conquistou fama resolvendo problemas que ninguém mais conseguia.")
print()
print("Durante sua jornada, cruzou o caminho de pessoas invejosas, que tramaram uma emboscada. Conseguiram atordoá-lo e o aprisionaram em uma torre misteriosa — uma estrutura tão complexa que apenas os mais sábios conseguiram escapar.")
print()
print("Entrar nela é fácil. Mas, uma vez lá dentro, encontrar a saída é praticamente impossível.")

# 1º andar

print("=" * 262)

from random import randint

vidas = 3
sorteio = randint(1,3)
if(sorteio == 1):
    forma = "círculo"
elif(sorteio == 2):
    forma = "quadrado"
elif(sorteio == 3):
    forma = "triângulo"

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

print("=" * 262)

print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
print()
print("> Vidas:", vidas)
print()
print("A - 🔴   ", end="")
print(" B - 🟥   ", end="")
print(" C - 🔺")
print("=" * 262)
resposta1 = input("> ")
print("=" * 262)
if(resposta1 != "A" or resposta1 != "a" or resposta1 != "B" or resposta1 != "b" or resposta1 != "C" or resposta1 != "c"):
    while(resposta1 != "A" and resposta1 != "a" and resposta1 != "B" and resposta1 != "b" and resposta1 != "C" and resposta1 != "c"):
        print("Escolha entre alternativas A, B ou C.")
        print("=" * 262)
        print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
        print()
        print("> Vidas:", vidas)
        print()
        print("A - 🔴   ", end="")
        print(" B - 🟥   ", end="")
        print(" C - 🔺")
        print("=" * 262)
        resposta1 = input("> ")
        print("=" * 262)
if(resposta1 == "A" or resposta1 == "a"):
        resposta1 = "círculo"
elif(resposta1 == "B" or resposta1 == "b"):
        resposta1 = "quadrado"
elif(resposta1 == "C" or resposta1 == "c"):
    resposta1 = "triângulo"
if(resposta1 == forma):
    print("Vidas:", vidas)
    print()
    print(">> Respota correta!")
else:
    vidas -= 1
    while(vidas >= 1):
        print("Resposta errada. Tente novamente.")
        print("=" * 262)
        print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
        print()
        print("> Vidas:", vidas)
        print()
        print("A - 🔴   ", end="")
        print(" B - 🟥   ", end="")
        print(" C - 🔺")
        print("=" * 262)
        resposta1 = input("> ")
        print("=" * 262)
        if(resposta1 != "A" or resposta1 != "a" or resposta1 != "B" or resposta1 != "b" or resposta1 != "C" or resposta1 != "c"):
            while(resposta1 != "A" and resposta1 != "a" and resposta1 != "B" and resposta1 != "b" and resposta1 != "C" and resposta1 != "c"):
                print("Escolha entre alternativas A, B ou C.")
                print("=" * 262)
                print(f">> Desafio 1: Escolha a alternativa com a forma de um {forma}.")
                print()
                print("> Vidas:", vidas)
                print()
                print("A - 🔴   ", end="")
                print(" B - 🟥   ", end="")
                print(" C - 🔺")
                print("=" * 262)
                resposta1 = input("> ")
                print("=" * 262)
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
        print("Vidas:", vidas)
        print()
        print(">> Resposta correta!")
    else:
        print("Vidas:", vidas)
        print()
        print("Acabaram suas vidas! Fim de jogo.")
