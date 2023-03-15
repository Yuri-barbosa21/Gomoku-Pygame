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
             
    def animar_botao(self, botao, botao_rect, tela):
        pos = pygame.mouse.get_pos()
        
        if botao_rect.collidepoint(pos):
            cor_sobreposicao = (50, 50, 50)

            botao_copy = botao.copy()
            botao_copy.fill(cor_sobreposicao, special_flags=pygame.BLEND_ADD)
            tela.blit(botao_copy, botao_rect)

    def desenha_peca(self, tela, linha, coluna, jogador):
        pretas = 'pretas'

        peca_branca = pygame.image.load('imagens/pecas/brancas.png').convert_alpha()
        peca_preta = pygame.image.load(f'imagens/pecas/{pretas}.png').convert_alpha()

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


    def limpar_tabuleiro(self):
        for i in range(TABULEIRO_LARGURA):
            for j in range(TABULEIRO_ALTURA):
                if self.matriz[i][j] != 0:
                    self.matriz[i][j] = 0

        self.pecas_brancas_desenhadas.clear()
        self.pecas_pretas_desenhadas.clear()

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

        self.JOGO_ATIVO = 0

        self.jogo_status = {
            'jogar_menu1': 0,
            'opcoes_menu2': 1,
            'opcoes_menu3': 2,
            'jogar': 3,
            'fim_jogo': 4
        }

        # Menu 1
        self.jogar_menu1 = pygame.image.load('imagens/menu/jogar_menu1.png').convert()
        self.jogar_menu1_rect = self.jogar_menu1.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        # Menu 2        
        self.opcoes_menu2 = pygame.image.load('imagens/menu/opcoes_menu2.png').convert()
        self.opcoes_menu2_rect = self.opcoes_menu2.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        # Menu 3
        self.opcoes_menu3 = pygame.image.load('imagens/menu/opcoes_menu3.png').convert()
        self.opcoes_menu3_rect = self.opcoes_menu3.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        # Botão Jogar
        self.botao_jogar = pygame.image.load('imagens/botoes/jogar.png').convert_alpha()
        self.botao_jogar_rect = self.botao_jogar.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 150))

        # Botão jogadores
        self.botao_jogadores = pygame.image.load('imagens/botoes/jogadores.png').convert_alpha()
        self.botao_jogadores_rect = self.botao_jogadores.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 150))

        # Botão Relógio
        self.botao_relogio = pygame.image.load('imagens/botoes/relogio.png').convert_alpha()
        self.botao_relogio_rect = self.botao_relogio.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 150))

        # Botão Tabuleiro
        self.botao_tabuleiro = pygame.image.load('imagens/botoes/tabuleiros.png').convert_alpha()
        self.botao_tabuleiro_rect = self.botao_tabuleiro.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 150))

        # Botão Voltar
        self.botao_voltar = pygame.image.load('imagens/botoes/voltar.png').convert_alpha()
        self.botao_voltar_rect = self.botao_voltar.get_rect(center = (TELA_X / 2, TELA_Y - 50))
        
        

    def iniciar_jogo(self):
        

        self.retangulos = self.tabuleiro.matriz_cliclavel()
        
        while True:

            #print(self.jogador_atual.num_peca)
            # Eventos do Jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                                                                                       
                    exit()

                #------------------------------ MENU 1 -------------------------------

                if self.JOGO_ATIVO == self.jogo_status['jogar_menu1']:
                    self.tela.blit(self.jogar_menu1, self.jogar_menu1_rect)

                    self.tela.blit(self.botao_jogar, self.botao_jogar_rect)
                    
                    
                    self.tabuleiro.animar_botao(self.botao_jogar, self.botao_jogar_rect, self.tela)
                    pos = pygame.mouse.get_pos()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.botao_jogar_rect.collidepoint(pos):
                            self.JOGO_ATIVO = self.jogo_status['opcoes_menu2']

                #------------------------------ MENU 2 -------------------------------

                elif self.JOGO_ATIVO == self.jogo_status['opcoes_menu2']:
                    self.tela.blit(self.opcoes_menu2, self.opcoes_menu2_rect)

                    #self.tela.blit(self.botao_voltar, self.botao_voltar_rect)
                    #self.tabuleiro.animar_botao(self.botao_voltar, self.botao_voltar_rect, self.tela)
                    
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.botao_jogar_rect.collidepoint(pos):
                            self.JOGO_ATIVO = self.jogo_status['opcoes_menu3']

                #------------------------------ MENU 3 -------------------------------

                elif self.JOGO_ATIVO == self.jogo_status['opcoes_menu3']:
                    self.tela.blit(self.opcoes_menu3, self.opcoes_menu3_rect)

                    self.tela.blit(self.botao_voltar, self.botao_voltar_rect)
                    self.tabuleiro.animar_botao(self.botao_voltar, self.botao_voltar_rect, self.tela)

                    self.tela.blit(self.botao_tabuleiros, self.botao_tabuleiros_rect)
                    self.tabuleiro.animar_botao(self.botao_tabuleiros, self.botao_tabuleiros_rect, self.tela)
                    
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.botao_jogar_rect.collidepoint(pos):
                            self.JOGO_ATIVO = self.jogo_status['jogar']

                        if self.botao_voltar_rect.collidepoint(pos):
                            self.JOGO_ATIVO = self.jogo_status['opcoes_menu2']
                        

                elif self.JOGO_ATIVO ==  self.jogo_status['jogar']:
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # botão direito do mouse
                            pos = pygame.mouse.get_pos()
                            for linha in range(TABULEIRO_LARGURA):
                                for coluna in range(TABULEIRO_ALTURA):
                                    if self.retangulos[linha][coluna].collidepoint(pos):

                                        if self.tabuleiro.jogar(linha= coluna, coluna= linha, jogador= self.jogador_atual):
                                            self.tabuleiro.desenha_peca(self.tela, linha, coluna, self.jogador_atual)
                                            if self.tabuleiro.verifica_se_ganhou(self.jogador_atual.num_peca):
                                                self.JOGO_ATIVO = self.jogo_status['fim_jogo']
                                            else:
                                                self.jogador_atual = self.jogador2  if self.jogador_atual == self.jogador1 else self.jogador1
                                        else:
                                            print('JOGADA INVALIDA')       
                                    


                    self.tela.fill('#FFF8D1') # Pinta o fundo do tela
                    self.tabuleiro.desenha_tabuleiro(self.tela) # Mostra tabuleiro na tela

                    for i in range(TABULEIRO_LARGURA):
                        for j in range(TABULEIRO_ALTURA):
                            if self.tabuleiro.matriz[i][j] == 1:
                                self.tabuleiro.desenha_peca(self. tela, i, j, self.jogador1)
                            elif self.tabuleiro.matriz[i][j] == 2:
                                self.tabuleiro.desenha_peca(self. tela, i, j, self.jogador2)

                elif self.JOGO_ATIVO == self.jogo_status['fim_jogo']:
                    ganhou = pygame.font.Font('fontes/Roobek.otf', 60)
                    ganhou_fonte = ganhou.render(f'{self.jogador_atual.nome} ganhou', True, 'Red')
                    ganho_font_rect = ganhou_fonte.get_rect(center= (TELA_X / 2, TELA_Y / 2))
                    self.tela.blit(ganhou_fonte, ganho_font_rect)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.tabuleiro.limpar_tabuleiro()

                            if randint(0, 2) == 1: self.jogador_atual = self.jogador1
                            else: self.jogador_atual = self.jogador2   

                            self.JOGO_ATIVO = self.jogo_status['jogar']
        

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
