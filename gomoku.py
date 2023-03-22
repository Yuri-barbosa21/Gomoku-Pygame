import pygame
from sys import exit
import numpy as np
import copy
from random import randint


'''------------------------ MACROS DO JOGO ------------------------'''
# Tamanho da tela
TELA_X = 1800
TELA_Y = 1000

# Tamnho do tabuleiro
TABULEIRO_LARGURA = 15
TABULEIRO_ALTURA = 15

# Tamanho dos quadrados do tebuleiro
QUADRADO_ALTURA = 42
QUADRADO_LARGURA = 42

'''_________________________________________________________________'''


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

    def desenhar_tabuleiro(self, tela, i):
        self.imagem_tabuleiro = pygame.image.load(f'imagens/tabuleiros/tabuleiro{i}.png').convert_alpha()
        self.imagem_tabuleiro_rect = self.imagem_tabuleiro.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        tela.blit(self.imagem_tabuleiro, self.imagem_tabuleiro_rect)

    def gerar_matriz_cliclavel(self):
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
    
    def verificar_jogada(self, linha, coluna):
        if linha < 0 or linha > TABULEIRO_LARGURA:
            return False
        if coluna < 0 or coluna > TABULEIRO_ALTURA:
            return False

        if (self.matriz[linha][coluna] == 1 or self.matriz[linha][coluna] == 2):
            return False
        else:
            return True

    def jogar(self, linha, coluna, jogador):

        if self.verificar_jogada(linha, coluna):
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

    def desenhar_peca(self, tela, linha, coluna, jogador):
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

    '''----------------------- VERIFICA SE O JOGADOR GANHOU -------------------------'''
    def verificar_se_ganhou(self, peca):
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

        # Sorteia quem será o primeiro jogador
        if randint(0, 2) == 1:
            self.jogador_atual = self.jogador1
        else: self.jogador_atual = self.jogador2

        pygame.init() # Inicializa o Pygame

        self.tela = pygame.display.set_mode((TELA_X, TELA_Y)) # Inicialza a tela 
        pygame.display.set_caption('Gomoku') # Nome da janela do jogo
        self.clock = pygame.time.Clock() # Inicializa o relógio do código

        self.jogo_ativo = 0 # Determina para quais telas o jogo vai

        # Dicionário das telas do jogo
        self.jogo_status = {
            'jogar_menu1': 0,
            'opcoes_menu2': 1,
            'opcoes_menu3': 2,
            'opcoes_tabuleiros': 3,
            'opcoes_jogadores': 4,
            'jogar': 5,
            'fim_jogo': 6
        }


        self.indice_tabuleiro = 1
        self.indice_escolhe_tabuleiro = 1

        
        # Define o temporizador em milissegundos
        self.tempo_maximo = 900000  # 15 minutos em milissegundos
        self.tempo_restante = self.tempo_maximo

        # Define o evento de temporizador
        self.TIMER_EVENTO = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENTO, 1000)  # 1000ms = 1 segundo
        self.texto_temporizador = 900
   
    def carregar_imagens(self):

        ''' ------------------------- TELAS DE MENU --------------------------- '''
        # Menu 1
        self.jogar_menu1 = pygame.image.load('imagens/menu/jogar_menu1.png').convert()
        self.jogar_menu1_rect = self.jogar_menu1.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        # Menu 2        
        self.opcoes_menu2 = pygame.image.load('imagens/menu/opcoes_menu2.png').convert()
        self.opcoes_menu2_rect = self.opcoes_menu2.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        # Menu 3
        self.opcoes_menu3 = pygame.image.load('imagens/menu/opcoes_menu3.png').convert()
        self.opcoes_menu3_rect = self.opcoes_menu3.get_rect(center = (TELA_X / 2, TELA_Y / 2))

        ''' ----------------------------- BOTÕES ------------------------------- '''
        # Botão Jogar 1
        self.botao_jogar = pygame.image.load('imagens/botoes/jogar.png').convert_alpha()
        self.botao_jogar_rect = self.botao_jogar.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 150))

        # Botão jogadores
        self.botao_jogadores = pygame.image.load('imagens/botoes/jogadores.png').convert_alpha()
        self.botao_jogadores_rect = self.botao_jogadores.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 285))

        # Botão Tabuleiro
        self.botao_tabuleiros = pygame.image.load('imagens/botoes/tabuleiros.png').convert_alpha()
        self.botao_tabuleiros_rect = self.botao_tabuleiros.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 185))

        # Botão Jogar 2
        self.botao_jogar2 = pygame.image.load('imagens/botoes/jogar2.png').convert_alpha()
        self.botao_jogar2_rect = self.botao_jogar2.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 85))

        # Botão Voltar
        self.botao_voltar = pygame.image.load('imagens/botoes/voltar.png').convert_alpha()
        self.botao_voltar_rect = self.botao_voltar.get_rect(center = (TELA_X / 2, TELA_Y - 50))

        # Botão Player vs Player
        self.botao_player_vs_player = pygame.image.load('imagens/botoes/playervsplayer.png').convert_alpha()
        self.botao_player_vs_player_rect = self.botao_player_vs_player.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 168))

        # Botão Player vs IA
        self.botao_player_vs_IA = pygame.image.load('imagens/botoes/playervsIA.png').convert_alpha()
        self.botao_player_vs_IA_rect = self.botao_player_vs_IA.get_rect(center = (TELA_X / 2, (TELA_Y / 2) + 268))
        

        ''' ---------------------------- OUTRAS IMAGENS ---------------------------- '''
        # Sprite Relógio 1
        self.sprite_relogio1 = pygame.image.load('imagens/sprites/relogio.png').convert_alpha()
        self.sprite_relogio1_rect = self.sprite_relogio1.get_rect(center = ((TELA_X / 2) + 225, (TELA_Y / 2) - 345))

        # Sprite Relógio 2
        self.sprite_relogio2 = pygame.image.load('imagens/sprites/relogio.png').convert_alpha()
        self.sprite_relogio2_rect = self.sprite_relogio2.get_rect(center = ((TELA_X / 2) - 225, (TELA_Y / 2) + 345))

        # Sprite Seta para Direita
        self.sprite_seta_direita = pygame.image.load('imagens/sprites/setadireita.png').convert_alpha()
        self.sprite_seta_direita_rect = self.sprite_seta_direita.get_rect(center = (TELA_X - 250, (TELA_Y / 2)))

        # Sprite Seta para esquerda
        self.sprite_seta_esquerda = pygame.image.load('imagens/sprites/setaesquerda.png').convert_alpha()
        self.sprite_seta_esquerda_rect = self.sprite_seta_esquerda.get_rect(center = (250, (TELA_Y / 2)))       

        ''' ---------------------------- PALAVRAS ---------------------------- '''
        self.fonte_fredokaone_120 = pygame.font.Font('fontes/FredokaOne-Regular.ttf', 120)
        self.fonte_fredokaone_40 = pygame.font.Font('fontes/FredokaOne-Regular.ttf', 40)
        self.fonte_fredokaone_70 = pygame.font.Font('fontes/FredokaOne-Regular.ttf', 70)
        self.fonte_quicksand_32 = pygame.font.Font('fontes/Quicksand-VariableFont_wght.ttf', 32)

        # Jogadores
        self.fonte_jogadores = self.fonte_quicksand_32.render('Jogadores', True, '#CF302B')
        self.fonte_jogadores_rect = self.fonte_jogadores.get_rect(center= (TELA_X / 2, TELA_Y / 2))


    



    def iniciar_jogo(self):


        self.retangulos = self.tabuleiro.gerar_matriz_cliclavel() # Gera matriz clicavel do tabuleiro
        self.carregar_imagens() # Carrega imagens do jogo
        
        
        while True:

            # -------------------------- EVENTOS DO JOGO --------------------------------
            for event in pygame.event.get():
                # Verifica clique no x da janela do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()                                                                                       
                    exit()

                #------------------------------ MENU 1 -------------------------------
                if self.jogo_ativo == self.jogo_status['jogar_menu1']:
                    # Menu 1
                    self.tela.blit(self.jogar_menu1, self.jogar_menu1_rect)

                    # Botão Jogar
                    self.tela.blit(self.botao_jogar, self.botao_jogar_rect)
                    self.tabuleiro.animar_botao(self.botao_jogar, self.botao_jogar_rect, self.tela)

                    # Verifica clique nos botões
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.botao_jogar_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_menu2']

                #------------------------------ MENU 2 -------------------------------
                elif self.jogo_ativo == self.jogo_status['opcoes_menu2']:
                    # Menu 2
                    self.tela.blit(self.opcoes_menu2, self.opcoes_menu2_rect)

                    # Botão Payer vs Player
                    self.tela.blit(self.botao_player_vs_player, self.botao_player_vs_player_rect)
                    self.tabuleiro.animar_botao(self.botao_player_vs_player, self.botao_player_vs_player_rect, self.tela)
                    
                    # Botão Player vs IA
                    self.tela.blit(self.botao_player_vs_IA, self.botao_player_vs_IA_rect)
                    self.tabuleiro.animar_botao(self.botao_player_vs_IA, self.botao_player_vs_IA_rect, self.tela)
                    
                    # Verifica clique nos botões
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.botao_player_vs_player_rect.collidepoint(pos) or self.botao_player_vs_IA_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_menu3']

                #------------------------------ MENU 3 -------------------------------
                elif self.jogo_ativo == self.jogo_status['opcoes_menu3']:
                    # Menu 3
                    self.tela.blit(self.opcoes_menu3, self.opcoes_menu3_rect)

                    # Botão Voltar
                    self.tela.blit(self.botao_voltar, self.botao_voltar_rect)
                    self.tabuleiro.animar_botao(self.botao_voltar, self.botao_voltar_rect, self.tela)

                    # Botão Tabuleiros
                    self.tela.blit(self.botao_tabuleiros, self.botao_tabuleiros_rect)
                    self.tabuleiro.animar_botao(self.botao_tabuleiros, self.botao_tabuleiros_rect, self.tela)

                    # Botão Jogar
                    self.tela.blit(self.botao_jogar2, self.botao_jogar2_rect)
                    self.tabuleiro.animar_botao(self.botao_jogar2, self.botao_jogar2_rect, self.tela)

                    # Botão Jogadores
                    self.tela.blit(self.botao_jogadores, self.botao_jogadores_rect)
                    self.tabuleiro.animar_botao(self.botao_jogadores, self.botao_jogadores_rect, self.tela)
                    
                    # Verifia clique nos botões
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Jogar
                        if self.botao_jogar2_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['jogar']

                        # Escolher Tabuleiro
                        if self.botao_tabuleiros_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_tabuleiros']

                        # Escolher Jogador
                        if self.botao_jogadores_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_jogadores']

                        # Voltar
                        if self.botao_voltar_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_menu2']
                        
                #--------------------------- MENU TABULEIROS --------------------------
                elif self.jogo_ativo == self.jogo_status['opcoes_tabuleiros']:
                    self.tela.fill('#FFF8D1') # Pinta o fundo do tela

                    # Botão Voltar
                    self.tela.blit(self.botao_voltar, self.botao_voltar_rect)
                    self.tabuleiro.animar_botao(self.botao_voltar, self.botao_voltar_rect, self.tela)


                    # Fonte Tabuleiros
                    self.fonte_tabuleiros = self.fonte_fredokaone_120.render(f'Tabuleiro {self.indice_escolhe_tabuleiro}', True, '#CF302B')
                    self.fonte_tabuleiros_rect = self.fonte_tabuleiros.get_rect(center= (TELA_X / 2, 100))
                    self.tela.blit(self.fonte_tabuleiros, self.fonte_tabuleiros_rect)

                    # Só desenha a seta esquerda se o tabuleiro for maior que 1
                    if self.indice_escolhe_tabuleiro > 1:
                        # Seta para Esquerda
                        self.tela.blit(self.sprite_seta_esquerda, self.sprite_seta_esquerda_rect)
                        self.tabuleiro.animar_botao(self.sprite_seta_esquerda, self.sprite_seta_esquerda_rect, self.tela)

                    if self.indice_escolhe_tabuleiro < 3:
                        # Seta para Direita
                        self.tela.blit(self.sprite_seta_direita, self.sprite_seta_direita_rect)
                        self.tabuleiro.animar_botao(self.sprite_seta_direita, self.sprite_seta_direita_rect, self.tela)


                    self.imagem_tabuleiro = pygame.image.load(f'imagens/tabuleiros/tabuleiro{self.indice_escolhe_tabuleiro}.png').convert_alpha()
                    self.imagem_tabuleiro_rect = self.imagem_tabuleiro.get_rect(center = (TELA_X / 2, TELA_Y / 2))
                    self.tela.blit(self.imagem_tabuleiro, self.imagem_tabuleiro_rect)
                    self.tabuleiro.animar_botao(self.imagem_tabuleiro, self.imagem_tabuleiro_rect, self.tela)

                    # Fonte Jogadores_

                    # Verifia clique nos botões
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # Voltar
                        if self.botao_voltar_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_menu3']

                        # Seta para Esquerda
                        if self.sprite_seta_esquerda_rect.collidepoint(pos) and self.indice_escolhe_tabuleiro > 1:
                            self.indice_escolhe_tabuleiro -= 1

                        # Seta para Direita
                        if self.sprite_seta_direita_rect.collidepoint(pos) and self.indice_escolhe_tabuleiro < 3:
                            self.indice_escolhe_tabuleiro += 1

                        if self.imagem_tabuleiro_rect.collidepoint(pos):
                            self.indice_tabuleiro = self.indice_escolhe_tabuleiro
                            self.jogo_ativo = self.jogo_status['opcoes_menu3']

                #--------------------------- MENU JOGADORES ----------------------------
                elif self.jogo_ativo == self.jogo_status['opcoes_jogadores']:
                    self.tela.fill('#FFF8D1') # Pinta o fundo do tela

                    # Botão Voltar
                    self.tela.blit(self.botao_voltar, self.botao_voltar_rect)
                    self.tabuleiro.animar_botao(self.botao_voltar, self.botao_voltar_rect, self.tela)

                    # Verifia clique nos botões
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # Voltar
                        if self.botao_voltar_rect.collidepoint(pos):
                            self.jogo_ativo = self.jogo_status['opcoes_menu3']

                # ----------------------------- JOGAR ---------------------------------
                elif self.jogo_ativo ==  self.jogo_status['jogar']:


                    

                    
                    # Verifica clique nos vertices do tabuleiro para gerar uma jogada 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # botão direito do mouse

                            pos = pygame.mouse.get_pos()
                            for linha in range(TABULEIRO_LARGURA):
                                for coluna in range(TABULEIRO_ALTURA):
                                    if self.retangulos[linha][coluna].collidepoint(pos): # Verifica colisão do clique com os vértices

                                        if self.tabuleiro.jogar(linha= coluna, coluna= linha, jogador= self.jogador_atual): # Efetua joga se for válida
                                            print(obter_sequencias(self.tabuleiro, 1))   
                                            self.tabuleiro.desenhar_peca(self.tela, linha, coluna, self.jogador_atual) # Desenha peça no local clicado

                                            if self.tabuleiro.verificar_se_ganhou(self.jogador_atual.num_peca): # Verifica se ganhou
                                                
                                                self.jogo_ativo = self.jogo_status['fim_jogo']

                                            else:
                                                # Troca jogador
                                                self.jogador_atual = self.jogador2  if self.jogador_atual == self.jogador1 else self.jogador1
                                        else:
                                            pass
                                            # Colocar audio para indicar jogada invalida
                                            # Colocar efeito visual para indicar jogada invalida       
                                    


                    self.tela.fill('#FFF8D1') # Pinta o fundo do tela
                    self.tabuleiro.desenhar_tabuleiro(self.tela, self.indice_tabuleiro) # Mostra tabuleiro na tela

                    # Fonte Jogador 1
                    self.fonte_jogador1 = self.fonte_fredokaone_70.render('Jogador 1', True, '#CF302B')
                    self.fonte_jogador1_rect = self.fonte_jogador1.get_rect(center= (TELA_X / 2, 100))
                    self.tela.blit(self.fonte_jogador1, self.fonte_jogador1_rect)

                    # Fonte Jogador 2
                    self.fonte_jogador2 = self.fonte_fredokaone_70.render('Jogador 2', True, '#CF302B')
                    self.fonte_jogador2_rect = self.fonte_jogador2.get_rect(center= (TELA_X / 2, TELA_Y - 100))
                    self.tela.blit(self.fonte_jogador2, self.fonte_jogador2_rect)

                    # Relógio 1
                    self.tela.blit(self.sprite_relogio1, self.sprite_relogio1_rect)
                    if self.jogador_atual == self.jogador1:
                        if event.type == self.TIMER_EVENTO:
                            self.tempo_restante -= 1000  # 1000ms = 1 segundo

                        segundos_restantes = self.tempo_restante // 1000
                        minutos = 15
                    
                        self.texto_temporizador = self.fonte_quicksand_32.render(f"{segundos_restantes}", True, 'Red')
                        self.texto_temporizador_rect = self.sprite_relogio1.get_rect(center= (170 / 2, 56 / 2))
                        self.tela.blit(self.texto_temporizador, self.texto_temporizador_rect)

                        
                    else:
                        #if self.texto_temporizador == 900:

                        #self.tela.blit(self.texto_temporizador, self.sprite_relogio1_rect)
                        pass



                    # Relógio 2
                    self.tela.blit(self.sprite_relogio2, self.sprite_relogio2_rect)

                    # Desenha Peças no tabuleiro
                    for i in range(TABULEIRO_LARGURA):
                        for j in range(TABULEIRO_ALTURA):
                            if self.tabuleiro.matriz[i][j] == 1:
                                self.tabuleiro.desenhar_peca(self. tela, i, j, self.jogador1)
                            elif self.tabuleiro.matriz[i][j] == 2:
                                self.tabuleiro.desenhar_peca(self. tela, i, j, self.jogador2)

                # --------------------------- FIM DE JOGO ------------------------------
                elif self.jogo_ativo == self.jogo_status['fim_jogo']:
                    superficie_transparente = pygame.Surface((TELA_X, TELA_Y), pygame.SRCALPHA)

                    # Preenche a superfície com uma cor com transparência
                    superficie_transparente.fill((255, 255, 255, 1))
                    self.tela.blit(superficie_transparente, (0,0))


                    self.fonte_ganhador = self.fonte_fredokaone_120.render(f'{self.jogador_atual.nome} ganhou', True, '#CF302B')
                    self.fonte_ganhador_rect = self.fonte_ganhador.get_rect(center= (TELA_X / 2, TELA_Y / 2))
                    self.tela.blit(self.fonte_ganhador, self.fonte_ganhador_rect)

                    self.fonte_recomecar = self.fonte_fredokaone_40.render('Pressione ENTER para recomeçar', True, 'Black')
                    self.fonte_recomecar_rect = self.fonte_recomecar.get_rect(center= (TELA_X / 2, (TELA_Y / 2) + 200))
                    self.tela.blit(self.fonte_recomecar, self.fonte_recomecar_rect)



                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.tabuleiro.limpar_tabuleiro()

                            if randint(0, 2) == 1: self.jogador_atual = self.jogador1
                            else: self.jogador_atual = self.jogador2   

                            self.jogo_ativo = self.jogo_status['jogar']
        

            pygame.display.update() # Atualiza a tela
            self.clock.tick(60) # Mantem o jogoo a 60 frames por segundo


    
class Gomoku:
    def __init__(self):
        self.tabuleiro = Tabuleiro(TABULEIRO_LARGURA, TABULEIRO_ALTURA)
        self.jogador1 = Jogador('Jogador 1','pretas')
        self.jogador2 = Jogador('Jogador 2','brancas')
        self.computador = 0

        self.jogo = Jogo(self.tabuleiro, self.jogador1, self.jogador2)

        

    
if __name__ == "__main__":
    gomoku = Gomoku()
    gomoku.jogo.iniciar_jogo()

def obter_sequencias(estado: Tabuleiro, peca):
    tamanhos_sequencias = []
    # Verifica linha
    for i in range(estado.linha):
        ganhou = 0
        for j in range(estado.coluna):
            if (estado.matriz[i][j] == peca):
                ganhou += 1
            else:
                if ganhou > 2:
                    tamanhos_sequencias.append(ganhou)
                ganhou = 0


    # Verifica coluna
    for j in range(estado.coluna):
        ganhou = 0
        for i in range(estado.linha):
            if (estado.matriz[i][j] == peca):
                ganhou += 1
            else:
                if ganhou > 2:
                    tamanhos_sequencias.append(ganhou)
                ganhou = 0

    # Verifica diagonal principal
    for i in range(estado.linha - 4):
        for j in range(estado.coluna - 4):
            ganhou = 0
            for k in range(5):
                if (estado.matriz[i+k][j+k] == peca):
                    ganhou += 1
                else:
                    if ganhou > 2:
                        tamanhos_sequencias.append(ganhou)
                    ganhou = 0

    # Verifica diagonal secundária
    for i in range(4, estado.linha):
        for j in range(estado.coluna - 4):
            ganhou = 0
            for k in range(5):
                if (estado.matriz[i-k][j+k] == peca):
                    ganhou += 1
                else:
                    if ganhou > 2:
                        tamanhos_sequencias.append(ganhou)
                    ganhou = 0

    return tamanhos_sequencias