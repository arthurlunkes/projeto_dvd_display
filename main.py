import pygame
import sys
import random

pygame.init()

largura =800
altura =600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Janela')

AZUL= (0,0,255)
PRETO= (0,0,0)
VERMELHO= (255,0,0)
VERDE= (0,255,0)
BRANCO= (255,255,255)

tamanho_fonte =50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Rafael", True, BRANCO)
texto_rect = texto.get_rect(center=(largura/2, altura/2))

clock = pygame.time.Clock()

#velocidade_x = 1
#velocidade_y = 1
velocidade_x = random.randint(-1,1)
velocidade_y = random.randint(-1,1)

while velocidade_x ==0and velocidade_y ==0:
    velocidade_x = random.randint(-1,1)
    velocidade_y = random.randint(-1,1)


rodando =True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando =False

    tela.fill(PRETO)
    tela.blit(texto,texto_rect)
    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1,0)
        velocidade_y = random.randint(-1,1)
        cor_aleatoria = (random.randint(1,255),
                         random.randint(1,255),
                         random.randint(1,255))
        texto = fonte.render("Rafael", True, cor_aleatoria)

    if texto_rect.left <=0:
        velocidade_x = random.randint(0,1)
        velocidade_y = random.randint(-1,1)
        cor_aleatoria = (random.randint(1,255),
                         random.randint(1,255),
                         random.randint(1,255))
        texto = fonte.render("Rafael", True, cor_aleatoria)

    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(-1,0)
        cor_aleatoria = (random.randint(1,255),
                         random.randint(1,255),
                         random.randint(1,255))
        texto = fonte.render("Rafael", True, cor_aleatoria)
       
    if texto_rect.top <=0:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(0,1)
        cor_aleatoria = (random.randint(1,255),
                         random.randint(1,255),
                         random.randint(1,255))
        texto = fonte.render("Rafael", True, cor_aleatoria)
       
    clock.tick(512)
    pygame.display.flip()
   
       
pygame.quit()
sys.exit()