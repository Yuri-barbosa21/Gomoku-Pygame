import matrizes
import re

def valor_heuristico(estado, jogador):
    valor = matrizes.calcular_pontuacao(estado, jogador)
    return valor

def gerar_filhos(estado, jogador):
    pass

def jogo_final(estado: list[list]):
    tabuleiro_linear = matrizes.obter_linhas_string(estado)
    for item in tabuleiro_linear:
        if re.search("11111", item) or re.search("22222", item):
            return True
        elif re.search("0+", item) is None:
            return True
    return False

def minimax(estado, profundidade, jogador_max, alfa, beta):
    if profundidade == 0 or jogo_final(estado):
        return valor_heuristico(estado, jogador_max)
    
    if jogador_max:
        valor_max = float("-inf")
        for filho in gerar_filhos(estado):
            valor = minimax(filho, profundidade-1, False, alfa, beta)
            valor_max = max(valor_max, valor)
            alfa = max(alfa, valor_max)
            if beta <= alfa:
                break
        return valor_max
    else:
        valor_min = float("inf")
        for filho in gerar_filhos(estado):
            valor = minimax(filho, profundidade-1, True, alfa, beta)
            valor_min = min(valor_min, valor)
            beta = min(beta, valor_min)
            if beta <= alfa:
                break
        return valor_min

matrix = [
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

num = 1

