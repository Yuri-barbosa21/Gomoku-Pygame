import pygame
from sys import exit
import numpy as np
from random import randint


TELA_X = 1800
TELA_Y = 1000

TABULEIRO_LARGURA = 15
TABULEIRO_ALTURA = 15


# Tamanho dos quadrados do tebuleiro
QUADRADO_ALTURA = 42
QUADRADO_LARGURA = 42

JOGO_ATIVO = True


class Jogador:
    def __init__(self, nome, peca):
        self.nome = nome
        self.peca = peca
        self.num_peca = 0
        if self.peca == 'pretas':
            self.num_peca = 1
        else: self.num_peca = 2




class Tabuleiro:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.matriz = np.zeros((linha,coluna))
        self.jogos = [] # Lista para guardas os estados do jogo
        self.pecas_desenhadas = []

    def desenha_tabuleiro(self, tela):
        self.imagem_tabuleiro = pygame.image.load('imagens/tabuleiros/tabuleiro2.png').convert_alpha()
        self.imagem_tabuleiro_rect = self.imagem_tabuleiro.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        tela.blit(self.imagem_tabuleiro, self.imagem_tabuleiro_rect)

    def matriz_cliclavel(self):
        self.quadrados = []
                
        for i in range(TABULEIRO_LARGURA):
            linhas = []
            for j in range(TABULEIRO_ALTURA):
                x = (i * QUADRADO_ALTURA)
                y = (j * QUADRADO_LARGURA) 

                quadrado = pygame.Rect(x + 585, y + 185, QUADRADO_ALTURA, QUADRADO_LARGURA)
                linhas.append(quadrado)
            self.quadrados.append(linhas)

        return self.quadrados

    def jogar(self, linha, coluna):
        self.matriz[linha][coluna] = 1

    def desenha_peca(self, tela, i, j):
        peca = pygame.image.load('imagens/pecas/brancas.png').convert_alpha()
        peca_rect = peca.get_rect()
        peca_rect.center = self.quadrados[i][j].center
        tela.blit(peca, peca_rect)
        self.pecas_desenhadas.append(self.quadrados[i][j])


        




    

class Jogo:
    def __init__(self, tabuleiro, jogador1, jogador2):
        self.tabuleiro = tabuleiro
        self.jogador1 = jogador1
        self.jogador2 = jogador2

        if randint(0, 2) == 1:
            self.jogador_atual = self.jogador1
        else: self.jogador_atual = self.jogador2

        pygame.init()

        self.tela = pygame.display.set_mode((TELA_X, TELA_Y)) # Inicialza a tela 
        pygame.display.set_caption('Gomoku') # Nome da janela do jogo
        self.clock = pygame.time.Clock() # Inicializa o relógio do código



    def iniciar_jogo(self):

        self.retangulos = self.tabuleiro.matriz_cliclavel()
        
        while True:
            # Eventos do Jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
                if JOGO_ATIVO:

                    
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        for i in range(TABULEIRO_LARGURA):
                            for j in range(TABULEIRO_ALTURA):
                                if self.retangulos[i][j].collidepoint(pos):
                                    print(f'Cliquei no quadrado {i} {j}') # mostra na tela as cordenadas do clique
                                    #pygame.draw.circle(self.tela, 'White', self.retangulos[i][j].center, 18)
                                    self.tabuleiro.jogar(i, j)
                                    self.tabuleiro.desenha_peca(self.tela, i, j)
                                    
                                    self.jogador_atual = self.jogador2  if self.jogador_atual == self.jogador1 else self.jogador1


                    self.tela.fill((186, 215, 233)) # Pinta o fundo do tela
                    self.tabuleiro.desenha_tabuleiro(self.tela) # Mostra tabuleiro na tela

                    for i in range(TABULEIRO_LARGURA):
                        for j in range(TABULEIRO_ALTURA):
                            if self.tabuleiro.matriz[i][j] == 1:
                                self.tabuleiro.desenha_peca(self. tela, i, j)
                #print(pygame.mouse.get_pos())


        

            '''
            #TESTAR LOCAL DOS QUADRADOS CLICAVEIS
            for i in range(TABULEIRO_LARGURA):
                for j in range(TABULEIRO_ALTURA):
                    pygame.draw.rect(self.tela, (255, 255, 255), self.retangulos[i][j])
            '''

            pygame.display.update() # Atualiza a tela
            self.clock.tick(60) # Mantem o jogoo a 60 frames por segundo



    
class Gomoku:
    def __init__(self):
        self.tabuleiro = Tabuleiro(15, 15)
        self.jogador1 = Jogador('Jogador 1','pretas')
        self.jogador2 = Jogador('Jogador 2','brancas')

        self.jogo = Jogo(self.tabuleiro, self.jogador1, self.jogador2)

        

    
if __name__ == "__main__":
    gomoku = Gomoku()
    gomoku.jogo.iniciar_jogo()
