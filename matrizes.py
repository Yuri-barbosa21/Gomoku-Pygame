#https://www.youtube.com/watch?v=FH9BxnzumVo
def diagonal_principal(matriz):
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

def rodar_matriz(matriz):
    matriz_nova = list(map(list, zip(*matriz[::-1])))
    return matriz_nova

def diagonal_secundaria(matriz):
    rodada = rodar_matriz(matriz)
    return diagonal_principal(rodada)

def count_sequences(matrix, number):
    counts = []
    for sublist in matrix:
        count = 0
        max_count = 0
        for item in sublist:
            if item == number:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        if max_count > 1:
            counts.append(max_count)
    return counts
    
#Recebe uma matriz e devolve um array com linhas, colunas em forma de linha e ambas diagonais
def obter_linhas(matriz):
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



