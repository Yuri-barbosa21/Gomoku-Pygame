import regex

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
    return linhas_string


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


#Matrizes para testes
matriz_teste = [
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

# matriz_teste = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# matriz_teste = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

