import matrizes
import re
import regex
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
                novo_estado = copy.deepcopy(estado)  # faz uma cópia do estado atual
                novo_estado[i][j] = jogador_atual  # preenche a posição vazia com a peça do jogador atual
                filhos.append(novo_estado)
    return filhos



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

def fazer_jogada_minimax(estado, jogador_atual, profundidade_maxima):
    melhor_valor = float('-inf') if jogador_atual == 1 else float('inf')
    melhor_jogada = None
    for jogada in gerar_filhos(estado, jogador_atual):
        valor = minimax(jogada, profundidade_maxima, jogador_atual == 1, float('-inf'), float('inf'))
        if jogador_atual == 1 and valor > melhor_valor:
            melhor_valor = valor
            melhor_jogada = jogada
        elif jogador_atual == 2 and valor < melhor_valor:
            melhor_valor = valor
            melhor_jogada = jogada
    return melhor_jogada

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

