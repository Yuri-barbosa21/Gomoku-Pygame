import matrizes
import re
import copy
import random

JOGADAS_MINIMAX = []

def valor_heuristico(estado, jogador):
    if jogador == 1:
        return matrizes.calcular_pontuacao(estado, jogador)

def gerar_filhos(estado, jogador_atual):
    filhos = []     
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                novo_estado = copy.deepcopy(estado) 
                novo_estado[i][j] = jogador_atual  
                filhos.append(novo_estado)
    return filhos


def jogo_final(estado: list[list]):
    #tabuleiro_linear = matrizes.obter_linhas_string(estado)
    linhas_string = []
    for item in estado:
        linhas_string.append(''.join(str(num) for num in item))

    for item in linhas_string:
        if re.search("11111", item) or re.search("22222", item):
            return True
        elif re.search("0+", item) is None:
            return True
    return False  


# def minimax(estado, profundidade, jogador):
#     if profundidade == 0 or jogo_final(estado):
#         return valor_heuristico(estado, jogador)

#     if jogador == 1:
#         valor_max = float("-inf")
#         for filho in gerar_filhos(estado, jogador):
#             valor = minimax(filho, profundidade - 1, 2)
#             valor_max = max(valor_max, valor)
#         return valor_max
#     else:
#         valor_min = float("inf")
#         for filho in gerar_filhos(estado, jogador):
#             valor = minimax(filho, profundidade - 1, 1)
#             valor_min = min(valor_min, valor)
#         return valor_min

def minimax(estado, profundidade, jogador , alpha, beta):
    if profundidade == 0 or jogo_final(estado):
        return valor_heuristico(estado, jogador)

    if jogador == 1:
        valor_max = float("-inf")
        for filho in gerar_filhos(estado, jogador):
            valor = minimax(filho, profundidade - 1, 2, alpha, beta)
            valor_max = max(valor_max, valor)
            alpha = max(alpha, valor_max)
            print("max")
            if beta <= alpha:
                break
        return valor_max
    else:
        valor_min = float("inf")
        for filho in gerar_filhos(estado, jogador):
            valor = minimax(filho, profundidade - 1, 1, alpha, beta)
            valor_min = min(valor_min, valor)
            beta = min(beta, valor_min)
            print("min")
            if beta <= alpha:
                break
        return valor_min



def fazer_jogada_minimax(estado, jogador, profundidade_maxima, jogada):
    melhor_valor = float('-inf') if jogador == 1 else float('inf')
    melhor_jogada = None
    melhor_coordenada = None
    novo_estado = matrizes.diminuir_matriz(estado, jogada)
    print(novo_estado)
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                novo_estado = copy.deepcopy(estado)
                novo_estado[i][j] = jogador
                valor = minimax(novo_estado, profundidade_maxima, jogador, float("-inf"), float("inf"))
                print(valor)
                if jogador == 1 and valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                    melhor_coordenada = (i, j)
                elif jogador == 2 and valor < melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                    melhor_coordenada = (i, j)
    return melhor_jogada, melhor_coordenada






matriz_teste = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def verificar_jogada(matriz, jogada):
    if jogada[0] < 0 or jogada[0] > 14:
        return False
    
    if jogada[1] < 0 or jogada[1] > 14:
        return False


    if matriz[jogada[0]][jogada[1]] == 0:
        return True
    else:
        return False
    
def heuristica(jogadas_player, jogadas_minimax, player_atual, matriz):
    # FAZ A PRIMEIRA JOGADA DE TODAS NO CENTRO
    if len(jogadas_minimax) == 0 and len(jogadas_player) == 0:
        #jogar(matriz, (7, 7), player_atual)
        print(f'Rodada ZERO: (7, 7)')
        return ((7, 7))

    # FAZ A PRIMEIRA JOGADA EM VOLTA DA DA JOGADA DO PLAYER
    if len(jogadas_minimax) == 0 and len(jogadas_player) == 1:
        while True:
            linha = random.randint(jogadas_player[0][0] - 1, jogadas_player[0][0] + 1)
            coluna = random.randint(jogadas_player[0][1] - 1, jogadas_player[0][1] + 1)

            if verificar_jogada(matriz, (linha, coluna)):
                JOGADAS_MINIMAX.append((linha, coluna))
                break
        print(f'Rodada 2: {linha}, {coluna}')
        return ((linha, coluna))
    
    # FAZ A SEGUNDA JOGADA EM VOLTA DA DA JOGADA DO MINIMAX
    if len(jogadas_minimax) == 1 and (len(jogadas_player) == 1 or len(jogadas_player) == 2):
        while True:
            linha = random.randint(jogadas_minimax[0][0] - 1, jogadas_minimax[0][0] + 1)
            coluna = random.randint(jogadas_minimax[0][1] - 1, jogadas_minimax[0][1] + 1)

            if verificar_jogada(matriz, (linha, coluna)):
                JOGADAS_MINIMAX.append((linha, coluna))
                break
        print(f'Rodada 3: {linha}, {coluna}')
        return ((linha, coluna))

    return False

def jogar(estado, profundidade_max, jogadas_player, jogadas_minimax, ult_jogada):
    jogada_heuristica = heuristica(jogadas_player, jogadas_minimax, 2, estado)
    if jogada_heuristica == False:
        um, dois = fazer_jogada_minimax(estado, 2, profundidade_max, ult_jogada)
        jogada_mm = matrizes.converter_coord(ult_jogada, dois)
        return jogada_mm
    else: return jogada_heuristica

    