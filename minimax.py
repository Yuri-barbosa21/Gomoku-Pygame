import matrizes
import re
import copy

def valor_heuristico(estado, jogador):
    if jogador == 1:
        return matrizes.calcular_pontuacao(estado, jogador)
    else: return matrizes.calcular_pontuacao(estado, jogador)

def gerar_filhos(estado, jogador_atual):
    filhos = []
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                novo_estado = copy.deepcopy(estado) 
                novo_estado[i][j] = jogador_atual  
                filhos.append(novo_estado)
    return filhos


def minimax(estado, profundidade, jogador):
    if profundidade == 0 or jogo_final(estado):
        return valor_heuristico(estado, jogador)

    if jogador == 1:
        valor_max = float("-inf")
        for filho in gerar_filhos(estado, jogador):
            valor = minimax(filho, profundidade - 1, 2)
            valor_max = max(valor_max, valor)
        return valor_max
    else:
        valor_min = float("inf")
        for filho in gerar_filhos(estado, jogador):
            valor = minimax(filho, profundidade - 1, 1)
            valor_min = min(valor_min, valor)
        return valor_min
    

def fazer_jogada_minimax(estado, jogador, profundidade_maxima):
    melhor_valor = float('-inf') if jogador == 1 else float('inf')
    melhor_jogada = None
    melhor_coordenada = None
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] == 0:
                jogada = copy.deepcopy(estado)
                jogada[i][j] = jogador
                valor = minimax(jogada, profundidade_maxima, jogador)
                if jogador == 1 and valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                    melhor_coordenada = (i, j)
                elif jogador == 2 and valor < melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                    melhor_coordenada = (i, j)
    return melhor_jogada, melhor_coordenada



def jogo_final(estado: list[list]):
    tabuleiro_linear = matrizes.obter_linhas_string(estado)
    for item in tabuleiro_linear:
        if re.search("11111", item) or re.search("22222", item):
            return True
        elif re.search("0+", item) is None:
            return True
    return False


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

resp, jogada = fazer_jogada_minimax(matriz_teste, 2, 4)
for i in resp:
    print(i)
print(jogada)
