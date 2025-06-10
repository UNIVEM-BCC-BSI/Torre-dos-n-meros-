# bibliotecas
import pygame
import sys
import os
import random

# iniciar a engine
pygame.init()

# tamanho e nome da janela
info = pygame.display.Info()
largura = info.current_w
altura = info.current_h
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("A Torre dos Números")

# imagens
caminho_base = os.path.dirname(os.path.abspath(__file__))

caminho_menu = os.path.join(caminho_base, "imagens", "menu.jpg")
caminho_logo = os.path.join(caminho_base, "imagens", "logo.png")

caminho_base_torre = os.path.join(caminho_base, "imagens", "base.jpg")
caminho_escadas1 = os.path.join(caminho_base, "imagens", "escadas1.jpg")

caminho_andar1 = os.path.join(caminho_base, "imagens", "andar1.jpg")
caminho_andar1_porta1 = os.path.join(caminho_base, "imagens", "andar1 porta1.jpg")
caminho_escadas2 = os.path.join(caminho_base, "imagens", "escadas2.jpg")

caminho_escolha_caminhos = os.path.join(caminho_base, "imagens", "escolha caminhos.jpg")

caminho_caminho_escuro1 = os.path.join(caminho_base, "imagens", "caminho escuro1.jpg")
caminho_caminho_escuro2 = os.path.join(caminho_base, "imagens", "caminho escuro2.jpg")
caminho_caminho_claro1 = os.path.join(caminho_base, "imagens", "caminho claro1.jpg")
caminho_caminho_claro2 = os.path.join(caminho_base, "imagens", "caminho claro2.jpg")
caminho_escadas3 = os.path.join(caminho_base, "imagens", "escadas3.jpg")

caminho_andar3 = os.path.join(caminho_base, "imagens", "andar3.jpg")
caminho_escadas4 = os.path.join(caminho_base, "imagens", "escadas4.jpg")

#caminho_andar4 = os.path.join(caminho_base, "imagens", "andar4.jpg")
caminho_final = os.path.join(caminho_base, "imagens", "final.jpg")

imagem_menu = pygame.image.load(caminho_menu)
imagem_menu = pygame.transform.scale(imagem_menu, (largura, altura))
imagem_logo = pygame.image.load(caminho_logo)
imagem_logo = pygame.transform.scale(imagem_logo, (largura // 7, altura // 7))

imagem_base_torre = pygame.image.load(caminho_base_torre)
imagem_base_torre = pygame.transform.scale(imagem_base_torre, (largura, altura))
imagem_escadas1 = pygame.image.load(caminho_escadas1)
imagem_escadas1 = pygame.transform.scale(imagem_escadas1, (largura, altura))

imagem_andar1 = pygame.image.load(caminho_andar1)
imagem_andar1 = pygame.transform.scale(imagem_andar1, (largura, altura))
imagem_andar1_porta1 = pygame.image.load(caminho_andar1_porta1)
imagem_andar1_porta1 = pygame.transform.scale(imagem_andar1_porta1, (largura, altura))
imagem_escadas2 = pygame.image.load(caminho_escadas2)
imagem_escadas2 = pygame.transform.scale(imagem_escadas2, (largura, altura))

imagem_escolha_caminhos = pygame.image.load(caminho_escolha_caminhos)
imagem_escolha_caminhos = pygame.transform.scale(imagem_escolha_caminhos, (largura, altura))

imagem_caminho_escuro1 = pygame.image.load(caminho_caminho_escuro1)
imagem_caminho_escuro1 = pygame.transform.scale(imagem_caminho_escuro1, (largura, altura))
imagem_caminho_escuro2 = pygame.image.load(caminho_caminho_escuro2)
imagem_caminho_escuro2 = pygame.transform.scale(imagem_caminho_escuro2, (largura, altura))
imagem_caminho_claro1 = pygame.image.load(caminho_caminho_claro1)
imagem_caminho_claro1 = pygame.transform.scale(imagem_caminho_claro1, (largura, altura))
imagem_caminho_claro2 = pygame.image.load(caminho_caminho_claro2)
imagem_caminho_claro2 = pygame.transform.scale(imagem_caminho_claro2, (largura, altura))
imagem_escadas3 = pygame.image.load(caminho_escadas3)
imagem_escadas3 = pygame.transform.scale(imagem_escadas3, (largura, altura))

imagem_andar3 = pygame.image.load(caminho_andar3)
imagem_andar3 = pygame.transform.scale(imagem_andar3, (largura, altura))
imagem_escadas4 = pygame.image.load(caminho_escadas4)
imagem_escadas4 = pygame.transform.scale(imagem_escadas4, (largura, altura))

#imagem_andar4 = pygame.image.load(caminho_andar4)
#imagem_andar4 = pygame.transform.scale(imagem_andar4, (largura, altura))
imagem_final = pygame.image.load(caminho_final)
imagem_final = pygame.transform.scale(imagem_final, (largura, altura))

# cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0,)
AZUL = (50, 120, 120)
AZUL_ESCURO = (50, 100, 100)

# fontes
fonte_titulo = pygame.font.SysFont("comicsansms", 70)
fonte_texto = pygame.font.SysFont("comicsansms", 33)
fonte_botao = pygame.font.SysFont("comicsansms", 25)

# perguntas
sorteio_pergunta_base = random.randint(1,5)
numero_pergunta_base = random.randint(1,3)
if numero_pergunta_base == 1:
    forma_pergunta_base = "uma forma rendonda."
elif numero_pergunta_base == 2:
    forma_pergunta_base = "quatro lados."
elif numero_pergunta_base == 3:
    forma_pergunta_base = "três lados."

sorteio_pergunta_andar1 = random.randint(1,5)
numero_pergunta_andar1 = random.randint(1,3)

sorteio_pergunta_caminho_escuro = random.randint(1,2)
numero_pergunta_caminho_escuro = random.randint(1,3)

sorteio_pergunta_caminho_claro = random.randint(1,2)
numero_pergunta_caminho_claro = random.randint(1,3)

# sistema de vidas
vidas = 3
def perder_vida():
    global vidas
    vidas -= 1

# desenhar botões
def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(tela, cor_hover, (x, y, largura, altura))
        if clique[0] == 1 and acao:
            pygame.time.delay(1000)
            acao()
    else:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))
    
    texto_superficie = fonte_botao.render(texto, True, PRETO)
    texto_ret = texto_superficie.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_superficie, texto_ret)

# mudar de estado
def mudar_estado(novo_estado):
    global estado_atual
    estado_atual = novo_estado

# definir os estados
estado_atual = "menu"

# menu
def menu():
    tela.blit(imagem_menu, (0, 0))
    desenhar_botao("Jogar", largura // 2 - 100, (altura // 4) * 3 - 50, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("introducao1"))
    desenhar_botao("Créditos", largura // 2 - 100, (altura // 4) * 3 + 25, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("creditos"))
    desenhar_botao("Sair", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("sair"))

# créditos
def creditos():
    tela.blit(imagem_menu, (0, 0))
    tela.blit(imagem_logo, ((largura // 8) * 6, altura // 9))
    desenhar_botao("Voltar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("menu"))

# fechar o jogo
def sair():
    pygame.quit()
    sys.exit()

# cena game over
def perdeu():
    tela.fill(PRETO)
    desenhar_botao("Menu", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("menu_perdeu"))

def menu_perdeu():
    tela.blit(imagem_menu, (0, 0))
    desenhar_botao("Jogar", largura // 2 - 100, (altura // 4) * 3 - 50, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("introducao1"))
    desenhar_botao("Créditos", largura // 2 - 100, (altura // 4) * 3 + 25, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("creditos"))
    desenhar_botao("Sair", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("sair"))

# introdução
def introducao1():
    tela.blit(imagem_menu, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("introducao2"))

def introducao2():
    tela.blit(imagem_menu, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("introducao3"))

def introducao3():
    tela.blit(imagem_menu, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base"))

# base da torre
def base():
    tela.blit(imagem_base_torre, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta1"))

def base_porta1():
    tela.blit(imagem_base_torre, (0, 0))

    if sorteio_pergunta_base == 1:

        if numero_pergunta_base == 1:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 2:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 3:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
    elif sorteio_pergunta_base == 2:

        if numero_pergunta_base == 1:
            desenhar_botao("Círculo", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("Quadrado", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("Triângulo", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 2:
            desenhar_botao("Círculo", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("Quadrado", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("Triângulo", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 3:
            desenhar_botao("Círculo", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("Quadrado", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("Triângulo", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))

    elif sorteio_pergunta_base == 3:
        if numero_pergunta_base == 1:
            desenhar_botao("1", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 2:
            desenhar_botao("1", (largura // 3) * 1.5- 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 3:
            desenhar_botao("1", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
    
    elif sorteio_pergunta_base == 4:
        if numero_pergunta_base == 1:
            desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
        elif numero_pergunta_base == 2:
            desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 3:
            desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("2", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])

    elif sorteio_pergunta_base == 5:
        if numero_pergunta_base == 1:
            desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 2:
            desenhar_botao("1", (largura // 3) * 2- 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
        elif numero_pergunta_base == 3:
            desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("base_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("base_porta2"))
  
def base_porta2():
    tela.blit(imagem_escadas1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escadas1"))

def escadas1():
    tela.blit(imagem_escadas1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_1"))

# 1º andar
def andar1_1():
    tela.blit(imagem_andar1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_2"))

def andar1_2():
    tela.blit(imagem_andar1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_3"))

def andar1_3():
    tela.blit(imagem_andar1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta1"))

def andar1_porta1():
    tela.blit(imagem_andar1_porta1, (0, 0))
    if sorteio_pergunta_andar1 == 1:
            
            if numero_pergunta_andar1 == 1:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 2:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 3:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
    
    elif sorteio_pergunta_andar1 == 2:
            
            if numero_pergunta_andar1 == 1:
                desenhar_botao("Espada", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("Martelo", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("Picareta", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 2:
                desenhar_botao("Espada", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("Martelo", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("Picareta", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 3:
                desenhar_botao("Espada", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("Martelo", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("Picareta", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))

    elif sorteio_pergunta_andar1 == 3:

            if numero_pergunta_andar1 == 1:
                desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 2:
                desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            if numero_pergunta_andar1 == 3:
                desenhar_botao("1", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
    elif sorteio_pergunta_andar1 == 4:

        if numero_pergunta_andar1 == 1:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
        elif numero_pergunta_andar1 == 2:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
        elif numero_pergunta_andar1 == 3:
            desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("3", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])

    elif sorteio_pergunta_andar1 == 5:

        if numero_pergunta_andar1 == 1:
            desenhar_botao("1", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
        elif numero_pergunta_andar1 == 2:
            desenhar_botao("1", (largura // 3) * 1.5- 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
        elif numero_pergunta_andar1 == 3:
            desenhar_botao("1", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("2", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar1_porta1")])
            desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar1_porta2"))

def andar1_porta2():
    tela.blit(imagem_escadas2, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escadas2"))

def escadas2():
    tela.blit(imagem_escadas2, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar2_1"))

# 2º andar
def andar2_1():
    tela.blit(imagem_escolha_caminhos, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar2_2"))

def andar2_2():
    tela.blit(imagem_escolha_caminhos, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar2_3"))

def andar2_3():
    tela.blit(imagem_escolha_caminhos, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar2_4"))

def andar2_4():
    tela.blit(imagem_escolha_caminhos, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escolha_caminho"))

# escolher o caminho
def escolha_caminho():
    tela.blit(imagem_escolha_caminhos, (0, 0))
    desenhar_botao("Escuro", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro1"))
    desenhar_botao("Claro", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro1"))

# caminho escuro
def caminho_escuro1():
    tela.blit(imagem_caminho_escuro1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro2"))

def caminho_escuro2():
    tela.blit(imagem_caminho_escuro1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio1"))

def caminho_escuro_desafio1():
    tela.blit(imagem_caminho_escuro1, (0, 0))
    if sorteio_pergunta_caminho_escuro == 1:
            
            if numero_pergunta_caminho_escuro == 1:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
            if numero_pergunta_caminho_escuro == 2:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
            if numero_pergunta_caminho_escuro == 3:
                desenhar_botao("1", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("2", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("3", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))
    elif sorteio_pergunta_caminho_escuro == 2:
            
            if numero_pergunta_caminho_escuro == 1:
                desenhar_botao("4", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))
                desenhar_botao("8", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("12", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
            if numero_pergunta_caminho_escuro == 2:
                desenhar_botao("4", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("8", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))
                desenhar_botao("12", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
            if numero_pergunta_caminho_escuro == 3:
                desenhar_botao("4", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("8", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_escuro_desafio1")])
                desenhar_botao("12", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_escuro_desafio2"))

def caminho_escuro_desafio2():
    tela.blit(imagem_caminho_escuro2, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escadas3"))

# caminho claro
def caminho_claro1():
    tela.blit(imagem_caminho_claro1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro2"))

def caminho_claro2():
    tela.blit(imagem_caminho_claro1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro3"))

def caminho_claro3():
    tela.blit(imagem_caminho_claro1, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio1"))

def caminho_claro_desafio1():
    tela.blit(imagem_caminho_claro1, (0, 0))
    if sorteio_pergunta_caminho_claro == 1:
            
            if numero_pergunta_caminho_claro == 1:
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))
                desenhar_botao("4", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("5", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
            if numero_pergunta_caminho_claro == 2:
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("4", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))
                desenhar_botao("5", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
            if numero_pergunta_caminho_claro == 3:
                desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("4", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("5", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))
    elif sorteio_pergunta_caminho_claro == 2:
            
            if numero_pergunta_caminho_claro == 1:
                desenhar_botao("5", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))
                desenhar_botao("6", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("7", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
            if numero_pergunta_caminho_claro == 2:
                desenhar_botao("5", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("6", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))
                desenhar_botao("7", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
            if numero_pergunta_caminho_claro == 3:
                desenhar_botao("5", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("6", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("caminho_claro_desafio1")])
                desenhar_botao("7", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("caminho_claro_desafio2"))

def caminho_claro_desafio2():
    tela.blit(imagem_caminho_claro2, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escadas3"))

def escadas3():
    tela.blit(imagem_escadas3, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_1"))

# 3º andar
def andar3_1():
    tela.blit(imagem_andar3, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_2"))

def andar3_2():
    tela.blit(imagem_andar3, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_3"))

def andar3_3():
    tela.blit(imagem_andar3, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_4"))

def andar3_4():
    tela.blit(imagem_andar3, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_porta1"))

def andar3_porta1():
    tela.blit(imagem_andar3, (0, 0))
    desenhar_botao("A", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar3_porta1")])
    desenhar_botao("B", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_porta2"))
    desenhar_botao("C", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar3_porta1")])

def andar3_porta2():
    tela.blit(imagem_escadas4, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar3_porta3"))

def andar3_porta3():
    tela.blit(imagem_escadas4, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("escadas4"))

def escadas4():
    tela.blit(imagem_escadas4, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_1"))

def andar4_1():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_2"))

def andar4_2():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_3"))

def andar4_3():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_4"))

def andar4_4():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_5"))

def andar4_5():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_6"))

def andar4_6():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_7"))

def andar4_7():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_8"))

def andar4_8():
    tela.fill(PRETO)
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_porta1"))

def andar4_porta1():
    tela.fill(AZUL_ESCURO)
    desenhar_botao("3", (largura // 3) - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar4_porta1")])
    desenhar_botao("5", (largura // 3) * 1.5 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_porta2"))
    desenhar_botao("7", (largura // 3) * 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: [perder_vida(), mudar_estado("andar4_porta1")])

def andar4_porta2():
    tela.blit(imagem_final, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("andar4_porta3"))

def andar4_porta3():
    tela.blit(imagem_final, (0, 0))
    desenhar_botao("Avançar", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("fim"))

def fim():
    tela.blit(imagem_final, (0, 0))
    desenhar_botao("Menu", largura // 2 - 100, (altura // 4) * 3 + 100, 200, 50, AZUL, AZUL_ESCURO, acao=lambda: mudar_estado("menu_perdeu"))

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

    # menu e créditos
    if estado_atual == "menu":
        menu()
        titulo = fonte_titulo.render("A Torre dos Números", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(largura // 2, altura // 5))
        tela.blit(titulo, titulo_rect)
    
    elif estado_atual == "creditos":
        creditos()
        texto1 = fonte_texto.render("Créditos", True, BRANCO)
        texto2 = fonte_texto.render("Guilherme Kanachiro de Souza", True, BRANCO)
        texto3 = fonte_texto.render("Eduardo Pontes", True, BRANCO)
        texto4 = fonte_texto.render("Emerson Sebastião Teles Da Silva", True, BRANCO)
        texto5 = fonte_texto.render("Vinicius Marques de Lima", True, BRANCO)
        texto6 = fonte_texto.render("Felipe Andrade Vieira", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 10))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
        tela.blit(texto5, (largura // 15, altura // 8 + 200))
        tela.blit(texto6, (largura // 15, altura // 8 + 250))
    
    elif estado_atual == "sair":
        sair()

    # menu após game over
    elif estado_atual == "menu_perdeu":
        menu_perdeu()
        titulo = fonte_titulo.render("A Torre dos Números", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(largura // 2, altura // 5))
        tela.blit(titulo, titulo_rect)
        
        vidas = 3

        sorteio_pergunta_base = random.randint(1,5)
        numero_pergunta_base = random.randint(1,3)
        if numero_pergunta_base == 1:
            forma_pergunta_base = "uma forma rendonda."
        elif numero_pergunta_base == 2:
            forma_pergunta_base = "quatro lados."
        elif numero_pergunta_base == 3:
            forma_pergunta_base = "três lados."

        sorteio_pergunta_andar1 = random.randint(1,5)
        numero_pergunta_andar1 = random.randint(1,3)

        sorteio_pergunta_caminho_escuro = random.randint(1,2)
        numero_pergunta_caminho_escuro = random.randint(1,3)

        sorteio_pergunta_caminho_claro = random.randint(1,2)
        numero_pergunta_caminho_claro = random.randint(1,3)

    # introdução
    elif estado_atual == "introducao1":
        introducao1()
        texto1 = fonte_texto.render("Há muitos séculos atrás...", True, BRANCO)
        texto2 = fonte_texto.render("Havia um humano considerado o maior enigmático de sua era.", True, BRANCO)
        texto3 = fonte_texto.render("Ele conquistou fama resolvendo problemas que ninguém mais conseguia.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    elif estado_atual == "introducao2":
        introducao2()
        texto1 = fonte_texto.render("Em sua jornada, cruzou o caminho de pessoas invejosas, que armaram uma emboscada.", True, BRANCO)
        texto2 = fonte_texto.render("Conseguiram atordoá-lo e o aprisionaram em uma torre misteriosa:", True, BRANCO)
        texto3 = fonte_texto.render("Uma estrutura tão complexa que apenas os mais sábios conseguiram escapar.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    elif estado_atual == "introducao3":
        introducao3()
        texto1 = fonte_texto.render("Entrar nela é fácil.", True, BRANCO)
        texto2 = fonte_texto.render("Mas, uma vez lá dentro, encontrar a saída é praticamente impossível.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
    
    # base da torre
    elif estado_atual == "base":
        base()
        texto1 = fonte_texto.render("1 dia depois...", True, BRANCO)
        texto2 = fonte_texto.render("O guerreiro desperta, ainda desorientado, em um lugar úmido e sombrio.", True, BRANCO)
        texto3 = fonte_texto.render("Sem saber onde está, começa a avançar pela torre.", True, BRANCO)
        texto4 = fonte_texto.render("Após alguns passos, ele encontra uma porta.", True, BRANCO)
        texto5 = fonte_texto.render("Na porta, está escrito:", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
        tela.blit(texto5, (largura // 15, altura // 8 + 200))
    
    elif estado_atual == "base_porta1":
        base_porta1()
        if sorteio_pergunta_base == 1:
            texto1 = fonte_texto.render("Um sábio druída tem o dever de criar poções para pessoas doentes!", True, BRANCO)
            texto2 = fonte_texto.render(f"Sendo {numero_pergunta_base} doentes quantas poções precisam ser feitas?", True, BRANCO)
            texto3 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
        elif sorteio_pergunta_base == 2:
            texto1 = fonte_texto.render("Um Feiticeiro pediu para seus servos buscar um item para amaldiçoar.", True, BRANCO)
            texto2 = fonte_texto.render(f"O item possui {forma_pergunta_base}", True, BRANCO)
            texto3 = fonte_texto.render("Qual o nome do objeto escolhido?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
        elif sorteio_pergunta_base == 3:
            texto1 = fonte_texto.render("Um temido rei perdeu suas míseras moedas.", True, BRANCO)
            texto2 = fonte_texto.render(f"Ele tinha {numero_pergunta_base} moedas.", True, BRANCO)
            texto3 = fonte_texto.render("Quantas moedas ele precisa encontrar?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))

        elif sorteio_pergunta_base == 4:
            texto1 = fonte_texto.render("Em um vilarejo haviam 4 crianças brincando.", True, BRANCO)
            texto2 = fonte_texto.render(f"Uma bruxa veio e levou {numero_pergunta_base}!", True, BRANCO)
            texto3 = fonte_texto.render("Quantas crianças restaram?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
        
        elif sorteio_pergunta_base == 5:
            texto1 = fonte_texto.render(f"Um guerreiro encontrou uma caverna com {numero_pergunta_base} goblins.", True, BRANCO)
            texto2 = fonte_texto.render("Ele consegue derrotar todos.", True, BRANCO)
            texto3 = fonte_texto.render("Qual o total de goblins derrotados?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
    elif estado_atual == "base_porta2":
        base_porta2()
        texto1 = fonte_texto.render("O guerreiro encaixa a chave na fechadura e a porta se abre lentamente.", True, BRANCO)
        texto2 = fonte_texto.render("Atrás, havia a escadaria para o próximo andar.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
    
    elif estado_atual == "escadas1":
        escadas1()
        texto = fonte_texto.render("Subindo...", True, BRANCO)
        tela.blit(texto, (largura // 15, altura // 8))

    # 1º andar
    elif estado_atual == "andar1_1":
        andar1_1()
        texto1 = fonte_texto.render("Ao chegar ao próximo andar, ele encontra um arqueiro.", True, BRANCO)
        texto2 = fonte_texto.render("Arqueiro: — Não dê mais nenhum passo!", True, BRANCO)
        texto3 = fonte_texto.render("Guerreiro: — Quem é você?", True, BRANCO)
        texto4 = fonte_texto.render("Arqueiro: — Sou Taski, o melhor arqueiro de Maiden.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    elif estado_atual == "andar1_2":
        andar1_2()
        texto1 = fonte_texto.render("Guerreiro: — Por que está aqui?", True, BRANCO)
        texto2 = fonte_texto.render("Taski: — Vim a este lugar para aprimorar meus conhecimentos.", True, BRANCO)
        texto3 = fonte_texto.render("Guerreiro: — Como alguém vem para este lugar por vontade própria?", True, BRANCO)
        texto4 = fonte_texto.render("Taski: — Achei que seria capaz de superar a torre... mas fui frustrado.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
    
    elif estado_atual == "andar1_3":
        andar1_3()
        texto1 = fonte_texto.render("Taski: — Infelizmente, não consegui avançar pela porta deste andar.", True, BRANCO)
        texto2 = fonte_texto.render("Guerreiro: — Me leve até lá. Tentarei ajudá-lo.", True, BRANCO)
        texto3 = fonte_texto.render("Então, Taski leva o guerreiro até a porta.", True, BRANCO)
        texto4 = fonte_texto.render("Na porta estava entalhado:", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    elif estado_atual == "andar1_porta1":
        andar1_porta1()
        if sorteio_pergunta_andar1 == 1:
            texto1 = fonte_texto.render("O Rei Arthur tem uma caverna feita para dragões!", True, BRANCO)
            texto2 = fonte_texto.render(f"São {numero_pergunta_andar1} o número de celas.", True, BRANCO)
            texto3 = fonte_texto.render("Quantos dragões podem ser acomodados nessa caverna?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
        
        elif sorteio_pergunta_andar1 == 2:
            texto1 = fonte_texto.render("Dentro de um baú existem vários itens e uma lista:", True, BRANCO)
            texto2 = fonte_texto.render("1 - Espada", True, BRANCO)
            texto3 = fonte_texto.render("2 - Martelo", True, BRANCO)
            texto4 = fonte_texto.render("3 - Picareta", True, BRANCO)
            texto5 = fonte_texto.render(f"O número {numero_pergunta_andar1} representa qual item?", True, BRANCO)
            texto6 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
            tela.blit(texto5, (largura // 15, altura // 8 + 200))
            tela.blit(texto6, (largura // 15, altura // 8 + 250))
        
        elif sorteio_pergunta_andar1 == 3:
            texto1 = fonte_texto.render(f"Um ferreiro cobra {numero_pergunta_andar1} moedas por armadura feita.", True, BRANCO)
            texto2 = fonte_texto.render("Um jovem guerreiro deseja comprar uma armadura do ferreiro.", True, BRANCO)
            texto3 = fonte_texto.render("Quantas moedas o jovem guerreiro precisa pagá-lo?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))

        elif sorteio_pergunta_andar1 == 4:
            texto1 = fonte_texto.render("Em uma arena, haviam 4 ferozes leões.", True, BRANCO)
            texto2 = fonte_texto.render(f"Uma legião entrou na arena e derrotou {numero_pergunta_andar1} deles!", True, BRANCO)
            texto3 = fonte_texto.render("Quantas leões ainda estão na arena?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
        
        elif sorteio_pergunta_andar1 == 5:
            texto1 = fonte_texto.render(f"Uma elfa precisa de {numero_pergunta_andar1} flores para uma poção de cura.", True, BRANCO)
            texto2 = fonte_texto.render("Então, uma gentil criança entregou as flores que a elfa precisava.", True, BRANCO)
            texto3 = fonte_texto.render("Quantas flores a criança entregou para a elfa?", True, BRANCO)
            texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))

    elif estado_atual == "andar1_porta2":
        andar1_porta2()
        texto1 = fonte_texto.render("Então, o guerreiro responde o enigma em voz alta.", True, BRANCO)
        texto2 = fonte_texto.render("A porta se desfaz, revelando a escadaria para o próximo andar.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))

    elif estado_atual == "escadas2":
        escadas2()
        texto = fonte_texto.render("Subindo...", True, BRANCO)
        tela.blit(texto, (largura // 15, altura // 8))

    # 2º andar
    elif estado_atual == "andar2_1":
        andar2_1()
        texto1 = fonte_texto.render("O guerreiro e Taski chegam a um novo ambiente surpreendente.", True, BRANCO)
        texto2 = fonte_texto.render("Estão em meio a um bosque dentro da torre.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))

    elif estado_atual == "andar2_2":
        andar2_2()
        texto1 = fonte_texto.render("Árvores altas crescem entre pedras e raízes antigas.", True, BRANCO)
        texto2 = fonte_texto.render("Há musgos, pequenas flores e o som distante de água correndo.", True, BRANCO)
        texto3 = fonte_texto.render("A luz entra por rachaduras no teto, criando feixes que dançam no ar.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))

    elif estado_atual == "andar2_3":
        andar2_3()
        texto1 = fonte_texto.render("Guerreiro: — Árvores... aqui dentro? Isso desafia toda a lógica.", True, BRANCO)
        texto2 = fonte_texto.render("Taski: — Já vi coisas estranhas, mas isso... isso é outro nível.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))

    elif estado_atual == "andar2_4":
        andar2_4()
        texto1 = fonte_texto.render("Diante deles, uma árvore com casca retorcida carrega duas setas cravadas:", True, BRANCO)
        texto2 = fonte_texto.render("Uma aponta para um caminho escuro, tomado por névoa e raízes retorcidas.", True, BRANCO)
        texto3 = fonte_texto.render("A outra, para um caminho claro, com flores brilhantes e trilhos de luz no chão.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "escolha_caminho":
        escolha_caminho()
        texto1 = fonte_texto.render("Taski encara o guerreiro e diz:", True, BRANCO)
        texto2 = fonte_texto.render("Taski: — Então... qual caminho escolheremos?", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
    
    # caminho escuro
    elif estado_atual == "caminho_escuro1":
        caminho_escuro1()
        texto1 = fonte_texto.render("O caminho é apertado.", True, BRANCO)
        texto2 = fonte_texto.render("Galhos secos parecem se mover sozinhos.", True, BRANCO)
        texto3 = fonte_texto.render("O ar fica pesado, e a névoa densa cobre o chão.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "caminho_escuro2":
        caminho_escuro2()
        if sorteio_pergunta_caminho_escuro == 1:
            texto1 = fonte_texto.render("Depois de alguns metros, um baú negro esfumaçado aparece.", True, BRANCO)
            texto2 = fonte_texto.render("Cravejado por rubis, ele possui uma tranca acionada por voz.", True, BRANCO)
            texto3 = fonte_texto.render("Taski: - Esse baú pode ser a nossa saída deste andar!", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 130))
        elif sorteio_pergunta_caminho_escuro == 2:
            texto = fonte_texto.render("Depois de alguns metros, o Guerreiro e Taski encontram uma figur peculiar.", True, BRANCO)
            texto = fonte_texto.render("Era um Espectro, com uma tunica negra e aparência esqueletica.", True, BRANCO)
            texto = fonte_texto.render("Utilizando usa magia, o espectro faz um mural subir e diz:", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "caminho_escuro_desafio1":
        caminho_escuro_desafio1()
        if sorteio_pergunta_caminho_escuro == 1:
            texto1 = fonte_texto.render(f"Taski: - Olhe bem, o baú possui {numero_pergunta_caminho_escuro} rubis encravados.", True, BRANCO)
            texto2 = fonte_texto.render("Qual é número que deverá ser falado em voz alta?", True, BRANCO)
            texto3 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 80))
            tela.blit(texto3, (largura // 15, altura // 8 + 130))
        elif sorteio_pergunta_caminho_escuro == 2:
            texto1 = fonte_texto.render("Espectro: - Você não é bem-vindo aqui.", True, BRANCO)
            texto2 = fonte_texto.render("Espectro: - A resposta do meu enigma é o número de luas vezes o número de esferas negras.", True, BRANCO)
            texto3 = fonte_texto.render(f"Espectro: - Este andar tem 4 luas no céu e {numero_pergunta_caminho_escuro} esferas negras.", True, BRANCO)
            texto4 = fonte_texto.render("Espectro: - Qual é a resposta?", True, BRANCO)
            texto5 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
            tela.blit(texto5, (largura // 15, altura // 8 + 200))
    elif estado_atual == "caminho_escuro_desafio2":
        caminho_escuro_desafio2()
        if sorteio_pergunta_caminho_escuro == 1:
            texto1 = fonte_texto.render("O baú se abre, saindo de dentro um feixe de luz.", True, BRANCO)
            texto2 = fonte_texto.render("A névoa desaparece.", True, BRANCO)
            texto3 = fonte_texto.render("Um portal de raízes se abre, levando ao próximo trecho da torre.", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
        elif sorteio_pergunta_caminho_escuro == 2:
            texto1 = fonte_texto.render("Ao responder corretamente, o Espectro acena com sua cabeça.", True, BRANCO)
            texto2 = fonte_texto.render("A névoa desaparece.", True, BRANCO)
            texto3 = fonte_texto.render("Um portal de raízes se abre, levando ao próximo trecho da torre.", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "caminho_claro1":
        caminho_claro1()
        texto1 = fonte_texto.render("Flores luminosas guiam o caminho.", True, BRANCO)
        texto2 = fonte_texto.render("O ambiente é silencioso, calmo... talvez calmo até demais.", True, BRANCO)
        texto3 = fonte_texto.render("No fim da trilha, há uma fonte de pedra, com água cristalina.", True, BRANCO)
        texto4 = fonte_texto.render("Acima dela, um espelho flutuante gira lentamente.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
    
    elif estado_atual == "caminho_claro2":
        caminho_claro2()
        texto1 = fonte_texto.render("Dele sai uma mulher com vestido dourado e uma coroa de flores brilhantes!", True, BRANCO)
        texto2 = fonte_texto.render("Mulher: - Boas Vindas ao Vale Luminoso, Sou Ariandel, Rainha do Vale Luminoso!", True, BRANCO)
        texto3 = fonte_texto.render("Ariandel: - Para atravessar meu vale, vocês precisam resolver um enigma.", True, BRANCO)
        texto4 = fonte_texto.render("Ariandel: - Continuem prosseguindo e encontrarão o enigma!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    elif estado_atual == "caminho_claro3":
        caminho_claro3()
        if sorteio_pergunta_caminho_claro == 1:
            texto1 = fonte_texto.render("Atravessando a ponte, deparam-se com o enigma.", True, BRANCO)
            texto2 = fonte_texto.render("Um pedestal brilhante com um livro aberto sobre ele.", True, BRANCO)
            texto3 = fonte_texto.render("Na página que o livro está aberto, tem o desenho de estrelas e luas.", True, BRANCO)
            texto4 = fonte_texto.render("Embaixo, está escrito:", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
        elif sorteio_pergunta_caminho_claro == 2:
            texto1 = fonte_texto.render("Atravessando a ponte, deparam-se com um paladino de armadura brilhante.", True, BRANCO)
            texto2 = fonte_texto.render("Atrás dele se encontrava um portão.", True, BRANCO)
            texto3 = fonte_texto.render("Então, o paladino bate seu enorme escudo e lança no chão.", True, BRANCO)
            texto4 = fonte_texto.render("Paladino: - Parados! Sou Freyior, guardião do vale Luminoso.", True, BRANCO)
            texto5 = fonte_texto.render("Freyior: - Para terem direito a passar devem resolver o enigma!", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 180))
            tela.blit(texto5, (largura // 15, altura // 8 + 230))
    
    elif estado_atual == "caminho_claro_desafio1":
        caminho_claro_desafio1()
        if sorteio_pergunta_caminho_claro == 1:
            texto1 = fonte_texto.render(f'"São {numero_pergunta_caminho_claro} estrelas luminosas e 2 luas prateadas."', True, BRANCO)
            texto2 = fonte_texto.render('"Se eu somar as estrelas com as luas, qual é o número total de corpos celestes?"', True, BRANCO)
            texto3 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
        elif sorteio_pergunta_caminho_claro == 2:
            texto1 = fonte_texto.render("Freyior: - Em meu escudo se escondem 4 luas.", True, BRANCO)
            texto2 = fonte_texto.render(f"Freyior: - Na haste de minha lança, {numero_pergunta_caminho_claro} sóis!", True, BRANCO)
            texto3 = fonte_texto.render("Freyior: - Se somados me dão o poder!", True, BRANCO)
            texto4 = fonte_texto.render("Freyior: - Qual o número do maior poder que protege essas terras?", True, BRANCO)
            texto5 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
            tela.blit(texto4, (largura // 15, altura // 8 + 150))
            tela.blit(texto5, (largura // 15, altura // 8 + 200))
    elif estado_atual == "caminho_claro_desafio2":
        caminho_claro_desafio2()
        if sorteio_pergunta_caminho_claro == 1:
            texto1 = fonte_texto.render("O guerreiro pega a pena com a tinta ao lado do livro e escreve a resposta.", True, BRANCO)
            texto2 = fonte_texto.render("O livro se embaralha e fecha, e o pedestal começa a descer", True, BRANCO)
            texto3 = fonte_texto.render("Assim, é aberto um caminho entre as árvores, que levam até às escadas.", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 50))
            tela.blit(texto3, (largura // 15, altura // 8 + 100))
        elif sorteio_pergunta_caminho_claro == 2:
            texto1 = fonte_texto.render("Freyior: - Parabéns, resposta correta! Vocês podem prosseguir.", True, BRANCO)
            texto2 = fonte_texto.render("O paladino abre caminho e eles passam pelo portão.", True, BRANCO)
            texto3 = fonte_texto.render("Além do portão, havia uma escada de cipós que levavam para o próximo andar.", True, BRANCO)
            tela.blit(texto1, (largura // 15, altura // 8))
            tela.blit(texto2, (largura // 15, altura // 8 + 80))
            tela.blit(texto3, (largura // 15, altura // 8 + 130))
        
    elif estado_atual == "escadas3":
        escadas3()
        texto = fonte_texto.render("Subindo...", True, BRANCO)
        tela.blit(texto, (largura // 15, altura // 8))
    
    # 3º andar
    elif estado_atual == "andar3_1":
        andar3_1()
        texto1 = fonte_texto.render("Após atravessarem o bosque encantado, o guerreiro e Taski chegam a um corredor silencioso.", True, BRANCO)
        texto2 = fonte_texto.render("As paredes ao redor são revestidas com espelhos altos, antigos.", True, BRANCO)
        texto3 = fonte_texto.render("Refletem suas imagens com um leve atraso...", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "andar3_2":
        andar3_2()
        texto1 = fonte_texto.render("Taski olha em volta, inquieto, e diz:", True, BRANCO)
        texto2 = fonte_texto.render("Taski: — Isso está me deixando nervoso... os reflexos não estão certos.", True, BRANCO)
        texto3 = fonte_texto.render("Conforme caminham, os espelhos começam a exibir imagens distorcidas:", True, BRANCO)
        texto4 = fonte_texto.render("O guerreiro chorando, Taski ferido, os dois fugindo.", True, BRANCO)
        texto5 = fonte_texto.render("Nenhuma delas parece real, mas todas causam desconforto.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 160))
        tela.blit(texto4, (largura // 15, altura // 8 + 210))
        tela.blit(texto5, (largura // 15, altura // 8 + 260))
    
    elif estado_atual == "andar3_3":
        andar3_3()
        texto1 = fonte_texto.render("Ao final do corredor, uma porta de madeira escura surge.", True, BRANCO)
        texto2 = fonte_texto.render("Possui uma trava em forma de espelho partido.", True, BRANCO)
        texto3 = fonte_texto.render("Gravado acima dela está o seguinte texto:", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "andar3_4":
        andar3_4()
        texto1 = fonte_texto.render('"A verdade liberta. O engano te aprisiona."', True, BRANCO)
        texto2 = fonte_texto.render("Opções se formam em símbolos flutuantes.", True, BRANCO)
        texto3 = fonte_texto.render("A trava brilha e uma pergunta aparece diante deles:", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
    
    elif estado_atual == "andar3_porta1":
        andar3_porta1()
        texto1 = fonte_texto.render('"O que mais revela sobre uma pessoa?"', True, BRANCO)
        texto2 = fonte_texto.render("A - Suas vitórias", True, BRANCO)
        texto3 = fonte_texto.render("B - Suas escolhas", True, BRANCO)
        texto4 = fonte_texto.render("C - Sua aparência", True, BRANCO)
        texto5 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
        tela.blit(texto5, (largura // 15, altura // 8 + 200))
    
    elif estado_atual == "andar3_porta2":
        andar3_porta2()
        texto1 = fonte_texto.render("A trava se desfaz em luz e a porta se abre lentamente.", True, BRANCO)
        texto2 = fonte_texto.render("Um vento leve sopra do outro lado.", True, BRANCO)
        texto3 = fonte_texto.render("Taski sorrindo aliviado, diz:", True, BRANCO)
        texto4 = fonte_texto.render("Taski: — Parece que estamos começando a entender os segredos dessa torre.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
    
    elif estado_atual == "andar3_porta3":
        andar3_porta3()
        texto1 = fonte_texto.render("Ao passarem pela porta, encontram uma sala silenciosa e limpa.", True, BRANCO)
        texto2 = fonte_texto.render("No centro, uma escada em espiral leva ao próximo andar.", True, BRANCO)
        texto3 = fonte_texto.render("Taski: — Esses desafios estão ficando cada vez mais pessoais...", True, BRANCO)
        texto4 = fonte_texto.render("Guerreiro: — E a torre parece saber quem somos...", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    elif estado_atual == "escadas4":
        escadas4()
        texto = fonte_texto.render("Subindo...", True, BRANCO)
        tela.blit(texto, (largura // 15, altura // 8))
    
    # 4º andar
    elif estado_atual == "andar4_1":
        andar4_1()
        texto1 = fonte_texto.render("Taski e o Guerreiro chegam no que parece ser o último andar da torre.", True, BRANCO)
        texto2 = fonte_texto.render("Era um enorme saguão com um trono vazio no meio.", True, BRANCO)
        texto3 = fonte_texto.render("Não fazia sentido, parecia atá mesmo um palácio.", True, BRANCO)
        texto4 = fonte_texto.render("Um tapete vermelho levava até o centro.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
    
    elif estado_atual == "andar4_2":
        andar4_2()
        texto1 = fonte_texto.render("Atrás do trono um enorme espelho refletia visão de fora!", True, BRANCO)
        texto2 = fonte_texto.render("Uma saída!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))

    elif estado_atual == "andar4_3":
        andar4_3()
        texto1 = fonte_texto.render("Guerreiro: - Olhe, Taski! Uma saída finalmente!", True, BRANCO)
        texto2 = fonte_texto.render("O guerreiro começa a caminhar até o trono.", True, BRANCO)
        texto3 = fonte_texto.render("Porém, Taski pede para o guerreiro que pare.", True, BRANCO)
        texto4 = fonte_texto.render("O guerreiro, confuso, para e se vira para Taski.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))

    elif estado_atual == "andar4_4":
        andar4_4()
        texto1 = fonte_texto.render("Taski: - Sinto muito, mas achou mesmo que seria assim tão fácil?", True, BRANCO)
        texto2 = fonte_texto.render("Guerreiro: - Não estou entendendo. O que quer dizer?", True, BRANCO)
        texto3 = fonte_texto.render("Taski: - Você ainda não entendeu?", True, BRANCO)
        texto4 = fonte_texto.render("Taski transfigura, tornando-se em um velho com barba branca e vestes de mago.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))

    elif estado_atual == "andar4_5":
        andar4_5()
        texto1 = fonte_texto.render("Guerreiro: - Quem é você?!", True, BRANCO)
        texto2 = fonte_texto.render("Velho: - Sinto muito garoto.", True, BRANCO)
        texto3 = fonte_texto.render("Velho: - Você é parte de algo maior.", True, BRANCO)
        texto4 = fonte_texto.render("Velho: - Sou Merlin, mago antigo conselheiro de seu pai, Rei Arthur!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))

    elif estado_atual == "andar4_6":
        andar4_6()
        texto1 = fonte_texto.render("Guerreiro: - O que você quer comigo Merlin?!", True, BRANCO)
        texto2 = fonte_texto.render("Guerreiro: - Porque me trouxe até aqui?!", True, BRANCO)
        texto3 = fonte_texto.render("Merlin: - Seu pai perdeu o pulso firme, deixou o reino ser tomado!", True, BRANCO)
        texto4 = fonte_texto.render("Merlin: - Ele é um fraco por se abrir a nossos inimigos!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))

    elif estado_atual == "andar4_7":
        andar4_7()
        texto1 = fonte_texto.render("Guerreiro: - Meu pai é honrado!", True, BRANCO)
        texto2 = fonte_texto.render("Guerreiro: - Ele quis os povos unidos para termos prosperidade!", True, BRANCO)
        texto3 = fonte_texto.render("Merlin: - Ele não tem visão! Está cego e você sofre!", True, BRANCO)
        texto4 = fonte_texto.render("Merlin: - Você está perdido aqui e ele nem se moveu!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))

    elif estado_atual == "andar4_8":
        andar4_8()
        texto1 = fonte_texto.render("Guerreiro: - Está errado. Com certeza deve ter uma legião atrás de mim!", True, BRANCO)
        texto2 = fonte_texto.render("Merlin: - Se não crê em mim, resolva o último e mais árduo enigma e te deixarei sair!", True, BRANCO)
        texto3 = fonte_texto.render("Merlin: - Pois eu sou o Rei da Torre dos Números!", True, BRANCO)
        texto4 = fonte_texto.render("Guerreiro: - Pois bem diga!", True, BRANCO)
        texto5 = fonte_texto.render("Merlin: - Eis o enigma do Rei:", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
        tela.blit(texto5, (largura // 15, altura // 8 + 200))
    
    elif estado_atual == "andar4_porta1":
        andar4_porta1()
        texto1 = fonte_texto.render("Merlin: - Tenho um número misterioso.", True, BRANCO)
        texto2 = fonte_texto.render("Merlin: - Se você multiplicá-lo por 4 e depois subtrair 6, o resultado será 14.", True, BRANCO)
        texto3 = fonte_texto.render("Qual é esse número?", True, BRANCO)
        texto4 = fonte_texto.render(f"Vidas: {vidas}", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
        tela.blit(texto3, (largura // 15, altura // 8 + 100))
        tela.blit(texto4, (largura // 15, altura // 8 + 150))
    
    elif estado_atual == "andar4_porta2":
        andar4_porta2()
        texto1 = fonte_texto.render("Merlin bate palmas e diz:", True, BRANCO)
        texto2 = fonte_texto.render("Merlin: - Muito bem, pois pode sair!", True, BRANCO)
        texto3 = fonte_texto.render("Merlin: - Veja a preocupação de seu pai, o Grande Rei Arthur!", True, BRANCO)
        texto4 = fonte_texto.render("Guerreiro: - Pois tenho certeza que sim!", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    elif estado_atual == "andar4_porta3":
        andar4_porta3()
        texto1 = fonte_texto.render("Merlin: - Vai se surpreender com o caminho que ainda te espera, Mordred... ", True, BRANCO)
        texto2 = fonte_texto.render("Então, o guerreiro se vira e vai em direção ao espelho.", True, BRANCO)
        texto3 = fonte_texto.render("O espelho torna-se em um portal, e o guerreiro atravessa.", True, BRANCO)
        texto4 = fonte_texto.render("A sua jornada finalmente acabou.", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 80))
        tela.blit(texto3, (largura // 15, altura // 8 + 130))
        tela.blit(texto4, (largura // 15, altura // 8 + 180))
    
    # fim
    elif estado_atual == "fim":
        fim()
        #fim = fonte_titulo.render("Fim", True, BRANCO)
        #fim_rect = fim.get_rect(center=(largura // 2, altura // 5))
        #tela.blit(fim, fim_rect)
        texto = fonte_texto.render("Fim", True, BRANCO)
        tela.blit(texto, (largura // 15, altura // 8))
    
    # game over
    if vidas <= 0:
        perdeu()
        texto1 = fonte_texto.render("Acabaram as suas vidas!", True, BRANCO)
        texto2 = fonte_texto.render("Fim de jogo", True, BRANCO)
        tela.blit(texto1, (largura // 15, altura // 8))
        tela.blit(texto2, (largura // 15, altura // 8 + 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()