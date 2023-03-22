import matrizes

def valor_heuristico(estado, jogador):
    pass

def gerar_filhos(estado, jogador):
    pass

def jogo_final(estado):
    pass

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
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

num = 1

#print(matrizes.obter_tamanhos_sequencias(matrix, num)) 

matrizes.obter_linhas(matrix)