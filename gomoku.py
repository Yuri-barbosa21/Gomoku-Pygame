import pygame
from sys import exit
import numpy as np
import copy
from random import randint


TELA_X = 1800
TELA_Y = 1000

TABULEIRO_LARGURA = 15
TABULEIRO_ALTURA = 15


# Tamanho dos quadrados do tebuleiro
QUADRADO_ALTURA = 42
QUADRADO_LARGURA = 42




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
        self.pecas_brancas_desenhadas = []
        self.pecas_pretas_desenhadas = []

    def desenha_tabuleiro(self, tela):
        self.imagem_tabuleiro = pygame.image.load('imagens/tabuleiros/tabuleiro4.png').convert_alpha()
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
    
    def verifica_jogada(self, linha, coluna):
        if linha < 0 or linha > TABULEIRO_LARGURA:
            return False
        if coluna < 0 or coluna > TABULEIRO_ALTURA:
            return False

        if (self.matriz[linha][coluna] == 1 or self.matriz[linha][coluna] == 2):
            return False
        else:
            return True

    def jogar(self, linha, coluna, jogador):

        if self.verifica_jogada(linha, coluna):
            self.matriz_copia = copy.deepcopy(self.matriz)
            self.jogos.append(self.matriz_copia) # Cria uma cópia do estado atual e adiciona na lista de estados

            print(f'LINHA: {linha} - COLUNA: {coluna}')

            if jogador.num_peca == 1:
                self.matriz[linha][coluna] = 1
                return True
            else:
                self.matriz[linha][coluna] = 2
                return True
        return False
             
        

    def desenha_peca(self, tela, linha, coluna, jogador):
        peca_branca = pygame.image.load('imagens/pecas/brancas.png').convert_alpha()
        peca_preta = pygame.image.load('imagens/pecas/pretas.png').convert_alpha()

        if jogador.num_peca == 1:
            peca_branca_rect = peca_branca.get_rect()
            peca_branca_rect.center = self.quadrados[coluna][linha].center
            tela.blit(peca_branca, peca_branca_rect)
            self.pecas_brancas_desenhadas.append(self.quadrados[coluna][linha])
        else:
            peca_preta_rect = peca_preta.get_rect()
            peca_preta_rect.center = self.quadrados[coluna][linha].center
            tela.blit(peca_preta, peca_preta_rect)
            self.pecas_pretas_desenhadas.append(self.quadrados[coluna][linha])


            #----------------------- VERIFICA SE O JOGADOR GANHOU -------------------------
    def verifica_se_ganhou(self, peca):
        # Verifica linha
        for i in range(self.linha):
            ganhou = 0
            for j in range(self.coluna):
                if (self.matriz[i][j] == peca):
                    ganhou += 1
                    if (ganhou == 5):
                        print('GANHOU')
                        return True
                else:
                    ganhou = 0

        # Verifica coluna
        for j in range(self.coluna):
            ganhou = 0
            for i in range(self.linha):
                if (self.matriz[i][j] == peca):
                    ganhou += 1
                    if (ganhou == 5):
                        print('GANHOU')
                        return True
                else:
                    ganhou = 0

        # Verifica diagonal principal
        for i in range(self.linha - 4):
            for j in range(self.coluna - 4):
                ganhou = 0
                for k in range(5):
                    if (self.matriz[i+k][j+k] == peca):
                        ganhou += 1
                        if (ganhou == 5):
                            print('GANHOU')
                            return True

        # Verifica diagonal secundária
        for i in range(4, self.linha):
            for j in range(self.coluna - 4):
                ganhou = 0
                for k in range(5):
                    if (self.matriz[i-k][j+k] == peca):
                        ganhou += 1
                        if (ganhou == 5):
                            print('GANHOU')
                            return True

        return False



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

        self.JOGO_ATIVO = True


    def iniciar_jogo(self):

        self.retangulos = self.tabuleiro.matriz_cliclavel()
        
        while True:

            #print(self.jogador_atual.num_peca)
            # Eventos do Jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                                                                                       
                    exit()
        
                if self.JOGO_ATIVO:
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        for linha in range(TABULEIRO_LARGURA):
                            for coluna in range(TABULEIRO_ALTURA):
                                if self.retangulos[linha][coluna].collidepoint(pos):
                                    print(f'Cliquei no quadrado {coluna} {linha}') # mostra na tela as cordenadas do clique
                                    #pygame.draw.circle(self.tela, 'White', self.retangulos[i][j].center, 18)
                                    if self.tabuleiro.jogar(linha= coluna, coluna= linha, jogador= self.jogador_atual):
                                        self.tabuleiro.desenha_peca(self.tela, linha, coluna, self.jogador_atual)
                                        if self.tabuleiro.verifica_se_ganhou(self.jogador_atual.num_peca):
                                            self.JOGO_ATIVO = False
                                        else:
                                            self.jogador_atual = self.jogador2  if self.jogador_atual == self.jogador1 else self.jogador1
                                            
                                            
                                        print(self.tabuleiro.matriz)
                                    else:
                                        jogada_valida = False
                                        print('JOGADA INVALIDA')       
                                        print(self.tabuleiro.matriz)


                    self.tela.fill((186, 215, 233)) # Pinta o fundo do tela
                    self.tabuleiro.desenha_tabuleiro(self.tela) # Mostra tabuleiro na tela

                    for i in range(TABULEIRO_LARGURA):
                        for j in range(TABULEIRO_ALTURA):
                            if self.tabuleiro.matriz[i][j] == 1:
                                self.tabuleiro.desenha_peca(self. tela, i, j, self.jogador1)
                            elif self.tabuleiro.matriz[i][j] == 2:
                                self.tabuleiro.desenha_peca(self. tela, i, j, self.jogador2)
                                
                #print(pygame.mouse.get_pos())

                else:
                    ganhou = pygame.font.Font('fontes/Roobek.otf', 60)
                    ganhou_fonte = ganhou.render(f'{self.jogador_atual.nome} ganhou', True, 'Red')
                    ganho_font_rect = ganhou_fonte.get_rect(center= (TELA_X / 2, TELA_Y / 2))
                    self.tela.blit(ganhou_fonte, ganho_font_rect)
        

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
