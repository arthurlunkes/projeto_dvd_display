import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Constantes
LARGURA = 800
ALTURA = 600
FPS = 60

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


class ObjetoMovel:
    
    def __init__(self, x, y, largura, altura, cor, velocidade_x, velocidade_y, texto=""):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.texto = texto
        
        # Garantir que as velocidades não sejam zero
        while self.velocidade_x == 0 and self.velocidade_y == 0:
            self.velocidade_x = random.randint(-3, 3)
            self.velocidade_y = random.randint(-3, 3)
    
    def mover(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y
    
    def verificar_colisao_parede(self, largura_tela, altura_tela):
        colidiu = False
        
        if self.rect.right >= largura_tela:
            self.rect.right = largura_tela
            self.velocidade_x = -abs(self.velocidade_x)
            colidiu = True
        
        # Colisão com parede esquerda
        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocidade_x = abs(self.velocidade_x)
            colidiu = True
        
        # Colisão com parede inferior
        if self.rect.bottom >= altura_tela:
            self.rect.bottom = altura_tela
            self.velocidade_y = -abs(self.velocidade_y)
            colidiu = True
        
        # Colisão com parede superior
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocidade_y = abs(self.velocidade_y)
            colidiu = True
        
        # Mudar cor quando colidir com a parede
        if colidiu:
            self.mudar_cor_aleatoria()
        
        return colidiu
    
    def verificar_colisao_objeto(self, outro_objeto):
        if self.rect.colliderect(outro_objeto.rect):
            self.velocidade_x, outro_objeto.velocidade_x = outro_objeto.velocidade_x, self.velocidade_x
            self.velocidade_y, outro_objeto.velocidade_y = outro_objeto.velocidade_y, self.velocidade_y
            
            self.separar_objetos(outro_objeto)
            
            self.mudar_cor_aleatoria()
            outro_objeto.mudar_cor_aleatoria()
            
            return True
        return False
    
    def separar_objetos(self, outro_objeto):
        dx = self.rect.centerx - outro_objeto.rect.centerx
        dy = self.rect.centery - outro_objeto.rect.centery
        
        # Mover objetos para fora da colisão
        if abs(dx) > abs(dy):
            if dx > 0:
                self.rect.left = outro_objeto.rect.right
            else:
                self.rect.right = outro_objeto.rect.left
        else:
            if dy > 0:
                self.rect.top = outro_objeto.rect.bottom
            else:
                self.rect.bottom = outro_objeto.rect.top
    
    def mudar_cor_aleatoria(self):
        self.cor = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
    
    def desenhar(self, tela, fonte=None):
        pygame.draw.rect(tela, self.cor, self.rect)
        pygame.draw.rect(tela, BRANCO, self.rect, 2)
        
        # Desenhar texto se houver
        if self.texto and fonte:
            texto_surface = fonte.render(self.texto, True, BRANCO)
            texto_rect = texto_surface.get_rect(center=self.rect.center)
            tela.blit(texto_surface, texto_rect)


class Jogo:
    
    def __init__(self):
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Simulação de Colisões - DVD')
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 40)
        self.fonte_info = pygame.font.SysFont(None, 30)
        
        # Criar dois objetos
        self.objeto1 = ObjetoMovel(
            x=100, 
            y=100, 
            largura=120, 
            altura=80, 
            cor=VERMELHO,
            velocidade_x=random.randint(-3, 3),
            velocidade_y=random.randint(-3, 3),
            texto="DVD 1"
        )
        
        self.objeto2 = ObjetoMovel(
            x=500, 
            y=400, 
            largura=120, 
            altura=80, 
            cor=AZUL,
            velocidade_x=random.randint(-3, 3),
            velocidade_y=random.randint(-3, 3),
            texto="DVD 2"
        )
        
        self.colisoes_parede = 0
        self.colisoes_objetos = 0
        self.rodando = True
    
    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.rodando = False
                elif evento.key == pygame.K_r:
                    self.reiniciar()
    
    def reiniciar(self):
        self.objeto1 = ObjetoMovel(
            x=100, 
            y=100, 
            largura=120,
            altura=80, 
            cor=VERMELHO,
            velocidade_x=random.randint(-3, 3),
            velocidade_y=random.randint(-3, 3),
            texto="DVD 1"
        )
        
        self.objeto2 = ObjetoMovel(
            x=500, 
            y=400, 
            largura=120, 
            altura=80, 
            cor=AZUL,
            velocidade_x=random.randint(-3, 3),
            velocidade_y=random.randint(-3, 3),
            texto="DVD 2"
        )
        
        self.colisoes_parede = 0
        self.colisoes_objetos = 0
    
    def atualizar(self):
        self.objeto1.mover()
        self.objeto2.mover()
        
        if self.objeto1.verificar_colisao_parede(LARGURA, ALTURA):
            self.colisoes_parede += 1
        if self.objeto2.verificar_colisao_parede(LARGURA, ALTURA):
            self.colisoes_parede += 1
        
        if self.objeto1.verificar_colisao_objeto(self.objeto2):
            self.colisoes_objetos += 1
    
    def desenhar(self):
        self.tela.fill(PRETO)
        
        self.objeto1.desenhar(self.tela, self.fonte)
        self.objeto2.desenhar(self.tela, self.fonte)
        
        # Desenhar informações
        info_parede = self.fonte_info.render(
            f"Colisões com parede: {self.colisoes_parede}", 
            True, 
            BRANCO
        )
        info_objetos = self.fonte_info.render(
            f"Colisões entre objetos: {self.colisoes_objetos}", 
            True, 
            BRANCO
        )
        info_teclas = self.fonte_info.render(
            "ESC: Sair | R: Reiniciar", 
            True, 
            BRANCO
        )
        
        self.tela.blit(info_parede, (10, 10))
        self.tela.blit(info_objetos, (10, 40))
        self.tela.blit(info_teclas, (10, ALTURA - 40))
        
        # Atualizar display
        pygame.display.flip()
    
    def executar(self):
        while self.rodando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
