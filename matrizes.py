import regex
import numpy as np
import re

#https://www.youtube.com/watch?v=FH9BxnzumVo
def diagonal_principal(matriz: list[list]):
    """
    Params: matriz -> Uma matriz quadrada (lista de listas)
    Returns: Uma matriz sendo cada linha uma diagonal
    
    1 0 0
    0 1 0   -> Retorna: [[1], [0,0], [0,1,0], [0,0], [1]]
    0 0 1 
    """
    linhas = len(matriz)
    colunas = len(matriz[0])

    parcial = []
    controle = 0
    res = []

    linha_atual = 0
    coluna_atual = 0
    subindo = True

    while(controle != linhas * colunas):
        if subindo:
            while linha_atual >= 0 and coluna_atual < colunas:
                parcial.append(matriz[linha_atual][coluna_atual])
                controle += 1

                linha_atual -= 1
                coluna_atual += 1

            if coluna_atual == colunas:
                coluna_atual -= 1
                linha_atual += 2
            else: 
                linha_atual += 1
            
            if parcial != []:
                res.append(parcial)
                parcial = []
            subindo = False
        else: 
            while linha_atual < linhas and coluna_atual >= 0:
                parcial.append(matriz[linha_atual][coluna_atual])
                controle +=1

                coluna_atual -= 1
                linha_atual += 1

            if linha_atual == linhas:
                coluna_atual += 2
                linha_atual -= 1

            else:
                coluna_atual += 1

            if parcial != []:
                res.append(parcial)
                parcial = []
            subindo = True
    return res


def rodar_matriz(matriz: list[list]):
    """
    #Params: matriz -> uma matriz quadrada (lista de listas)
    #Returns: a transposta da matriz
    """
    matriz_nova = list(map(list, zip(*matriz[::-1])))
    return matriz_nova


def diagonal_secundaria(matriz):
    """
    #Params: matriz -> uma matriz quadrada (lista de listas)
    #Returns: Uma matriz sendo cada linha uma diagonal
    """
    rodada = rodar_matriz(matriz)
    return diagonal_principal(rodada)


def obter_linhas(matriz: list[list]):
    """
    #Params: matriz -> uma matriz quadrada (lista de listas)
    #returns: Uma matriz que contém todas as linhas, colunas e ambas diagonais da matriz original
    """
    diagonais = []
    principal = diagonal_principal(matriz)
    secundaria = diagonal_secundaria(matriz)

    diagonais = principal + secundaria

    linhas_e_colunas = []
    for line in matriz:
        linhas_e_colunas.append(line)

    colunas = rodar_matriz(matriz)
    for linha in colunas:
        linhas_e_colunas.append(linha)

    tudo = diagonais + linhas_e_colunas
    return tudo


def obter_linhas_string(matriz: list[list]):
    """
    Params: matriz -> uma matriz quadrada (lista de listas)
    returns: Uma matriz que contém todas as linhas, colunas e ambas diagonais da matriz original mas em formato de string
    """
    tudo = obter_linhas(matriz)
    linhas_string = []
    for item in tudo:
        linhas_string.append(''.join(str(num) for num in item))

    return remover_zeros(linhas_string)


def remover_zeros(linhas_string):
    linhas_sem_zero = []
    for i in range(len(linhas_string)):
        if not re.match("^[0]+$", linhas_string[i]):
            linhas_sem_zero.append(linhas_string[i])

    return linhas_sem_zero


def calcular_pontuacao(estado: list[list], jogador: int):
    """
    Params: estado -> matriz do estado atual do jogo
            jogador -> número do jogador (1 ou 2)
    returns: pontuação do estado atual
    """
    lista_de_strings = obter_linhas_string(estado)
    if jogador == 1: 
        return regex.calcular_pontuacao(lista_de_strings, regex.regras_jogador1)
    else:
        return regex.calcular_pontuacao(lista_de_strings, regex.regras_jogador2)


def vizinhanca(estado: list[list], i: int, j:int):
        if i == 0 and j == 0:
            if estado[i][j+1] != 0 or estado[i+1][j] != 0:
                return True
        elif i == 0 and j == len(estado[i])-1:
            if estado[i][j-1] != 0 or estado[i+1][j] != 0:
                return True
        elif i == len(estado)-1 and j == 0:
            if estado[i][j+1] != 0 or estado[i-1][j] != 0:
                return True
        elif i == len(estado)-1 and j == len(estado[i])-1:
            if estado[i][j-1] != 0 or estado[i-1][j] != 0:
                return True
        elif i == 0:
            if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i+1][j] != 0:
                return True
        elif i == len(estado)-1:
            if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i-1][j] != 0:
                return True
        elif j == 0:
            if estado[i][j+1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0:
                return True
        elif j == len(estado[i])-1:
            if estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0:
                return True
        else:
            if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0:
                return True
        return False


def verificar_jogada(matriz: list[list], jogada: tuple):
    #Verifica se a jogada está dentro da matriz e se a posição está vazia
    #Só funciona na matriz original (15x15)
    if jogada[0] < 0 or jogada[0] > 14:
        return False
    
    if jogada[1] < 0 or jogada[1] > 14:
        return False

    if matriz[jogada[0]][jogada[1]] == 0:
        return True
    else:
        return False
       

def converter_coord(jogada, jogada_menor):
    if (jogada[0] - 4) <= 0:
        x = 0
    else:
        x = jogada[0] - 4

    if (jogada[1] - 4) <= 0:
        y = 0
    else:
        y = jogada[1] - 4

    resultado = (x + jogada_menor[0]), (y + jogada_menor[1])
    return resultado


def diminuir_matriz(matriz, jogada: tuple):
    x = 4
    y = 4
    linha_inicio = 0
    coluna_inicio = 0
    linha_fim = 0
    coluna_fim = 0
    
    if jogada[0] + x > 14:
        linha_inicio = jogada[0] - x
        linha_fim = 15

        if jogada[1] + y > 14:
            coluna_inicio = jogada[1] - y
            coluna_fim = 15

        if jogada[1] < y:
            coluna_inicio = 0
            coluna_fim = jogada[1] + y + 1
        
        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio), dtype=int).tolist()
        for i in range(linha_fim - linha_inicio):
            for j in range(coluna_fim - coluna_inicio):
                nova_matriz[i][j] = matriz[linha_inicio + i][coluna_inicio + j]
        return nova_matriz

    if jogada[0] > x:
        linha_inicio = jogada[0] - x
        linha_fim = jogada[0] + x + 1
        

        if jogada[0] + x > 14:
            linha_inicio = jogada[0] - x
            linha_fim = 15

        if jogada[1] < y:
         coluna_inicio = 0
         coluna_fim = jogada[1] + y + 1

        if jogada[1] > y:
            coluna_inicio = jogada[1] - y
            coluna_fim = jogada[1] + y + 1

        if jogada[1] + y > 14:
            coluna_inicio = jogada[1] - y
            coluna_fim = 15

        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio), dtype=int).tolist()

        for i in range(linha_fim - linha_inicio):
            for j in range(coluna_fim - coluna_inicio):
                nova_matriz[i][j] = matriz[linha_inicio + i][coluna_inicio + j]
    
        return nova_matriz

    # SE A JOGADA LINHA FOR MENOR QUE O TAMANHO DA MATRIZ
    if jogada[0] <= x:
        linha_inicio = 0
        linha_fim = jogada[0] + x + 1
        
        # SE A JOGADA COLUNA FOR MENOR QUE O TAMANHO DA MATRIZ
        if jogada[1] < y:
         coluna_inicio = 0
         coluna_fim = jogada[1] + y + 1

        if jogada[1] > y:
            coluna_inicio = jogada[1] - y
            coluna_fim = jogada[1] + y + 1

        if jogada[1] + y > 14:
            coluna_inicio = jogada[1] - y
            coluna_fim = 15
            
        # CRIA UMA MATRIZ COM O TAMANHO DA LINHA E COLUNA
        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio), dtype=int).tolist()

        for i in range(linha_fim - linha_inicio):
            for j in range(coluna_fim - coluna_inicio):
                nova_matriz[i][j] = matriz[linha_inicio + i][coluna_inicio + j]
    
        return nova_matriz
