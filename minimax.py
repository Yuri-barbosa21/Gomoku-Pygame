import matrizes
import re
import copy
import random

JOGADAS_MINIMAX = []

class Minimax:
    def __init__(self, nome, peca):
        self.nome = nome
        self.peca = peca
        self.num_peca = 1

    def valor_heuristico(self, estado, jogador):
        return matrizes.calcular_pontuacao(estado, jogador)


    # def gerar_filhos(self, estado, jogador_atual):
    #     posicoes_vazias = [(i, j) for i in range(len(estado)) for j in range(len(estado[i])) if estado[i][j] == 0]
    #     print(posicoes_vazias)
    #     filhos = [copy.deepcopy(estado) for _ in posicoes_vazias]
    #     for filho, (i, j) in zip(filhos, posicoes_vazias):
    #         filho[i][j] = jogador_atual
    #     return filhos if filhos else [[]]

    def gerar_filhos(self, estado, jogador_atual):
        posicoes_vazias = []
        
        for i in range(len(estado)):
            for j in range(len(estado)):
                if estado[i][j] == 0 and matrizes.vizinhanca(estado, i, j):
                    posicoes_vazias.append((i, j))
                    
            
        print(posicoes_vazias)

        filhos = [copy.deepcopy(estado) for _ in posicoes_vazias]
        for filho, (i, j) in zip(filhos, posicoes_vazias):
            filho[i][j] = jogador_atual
        return filhos if filhos else [[]] 


    def jogo_final(self, estado: list[list]):
        linhas_string = [''.join(str(num) for num in item) for item in estado]
        for item in linhas_string:
            if re.search("11111", item) or re.search("22222", item):
                return True
        return not any(0 in linha for linha in estado)


    def minimax(self, estado, profundidade, jogador , alpha, beta):
        if profundidade == 0 or self.jogo_final(estado):
            return self.valor_heuristico(estado, jogador)

        if jogador == 1:
            valor_max = float("-inf")
            for filho in self.gerar_filhos(estado, jogador):
                valor = self.minimax(filho, profundidade - 1, 2, alpha, beta)
                valor_max = max(valor_max, valor)
                alpha = max(alpha, valor_max)
                if beta <= alpha:
                    break
            return valor_max
        else:
            valor_min = float("inf")
            for filho in self.gerar_filhos(estado, jogador):
                valor = self.minimax(filho, profundidade - 1, 1, alpha, beta)
                valor_min = min(valor_min, valor)
                beta = min(beta, valor_min)
                if beta <= alpha:
                    break
            return valor_min


    def fazer_jogada_minimax(self, estado, jogador, profundidade_maxima, jogada):
        melhor_valor = float('-inf') if jogador == 1 else float('inf')
        melhor_coordenada = None
  

        for i in range(len(estado)):
            for j in range(len(estado[i])):
                if estado[i][j] == 0 and matrizes.vizinhanca(estado, i, j):
                    novo_estado = copy.deepcopy(estado)
                    novo_estado[i][j] = jogador
                    valor = self.minimax(novo_estado, profundidade_maxima-1, jogador, float("-inf"), float("inf"))
                    if jogador == 1 and valor > melhor_valor:
                        melhor_valor = valor
                        melhor_coordenada = (i, j)
                    elif jogador == 2 and valor < melhor_valor:
                        melhor_valor = valor
                        melhor_coordenada = (i, j)
        return melhor_coordenada
 

    def heuristica(self, jogadas_player, jogadas_minimax, matriz):
        # FAZ A PRIMEIRA JOGADA DE TODAS NO CENTRO
        if len(jogadas_minimax) == 0 and len(jogadas_player) == 0:
            print(f'MINIMAX.PY/heuristica -> Rodada 1: (7, 7)')
            return ((7, 7))

        # FAZ A PRIMEIRA JOGADA EM VOLTA DA DA JOGADA DO PLAYER
        if len(jogadas_minimax) == 0 and len(jogadas_player) == 1:
            while True:
                linha = random.randint(jogadas_player[0][0] - 1, jogadas_player[0][0] + 1)
                coluna = random.randint(jogadas_player[0][1] - 1, jogadas_player[0][1] + 1)

                if matrizes.verificar_jogada(matriz, (linha, coluna)):
                    JOGADAS_MINIMAX.append((linha, coluna))
                    break

            print(f'Rodada 2: ({linha}, {coluna})')
            return ((linha, coluna))
        
        # FAZ A SEGUNDA JOGADA EM VOLTA DA DA JOGADA DO MINIMAX
        if len(jogadas_minimax) == 1 and (len(jogadas_player) == 1 or len(jogadas_player) == 2):
            while True:
                linha = random.randint(jogadas_minimax[0][0] - 1, jogadas_minimax[0][0] + 1)
                coluna = random.randint(jogadas_minimax[0][1] - 1, jogadas_minimax[0][1] + 1)

                if matrizes.verificar_jogada(matriz, (linha, coluna)):
                    JOGADAS_MINIMAX.append((linha, coluna))
                    break

            print(f'MINIMAX.PY/heuristica -> Rodada 3: ({linha}, {coluna})')
            return ((linha, coluna))

        return False

    def jogar(self, estado, profundidade_max, jogadas_player, jogadas_minimax, ult_jogada, jogador):
        jogada_heuristica = self.heuristica(jogadas_player, jogadas_minimax, estado)
        if jogada_heuristica == False:
            
            coordenada_minimax = self.fazer_jogada_minimax(estado, jogador, profundidade_max, ult_jogada)
            return coordenada_minimax
        else: return jogada_heuristica
