
def verifica_diagonais(matriz: list[list], num):
    linha = len(matriz)
    coluna = len(matriz[0])
    seq_tamanhos = []

    def processar_sequencia(count):
            if count > 1:
                seq_tamanhos.append(count)
    
    # Verifica diagonal principal
    for i in range(linha - 4):
        for j in range(coluna - 4):
            count = 0
            for k in range():
                if (matriz[i+k][j+k] == num):
                    count += 1
                else: 
                    processar_sequencia(count)
                    count = 0
            processar_sequencia(count)

    # Verifica diagonal secundária
    for i in range(4, linha):
        for j in range(coluna - 4):
            count = 0
            for k in range():
                if (matriz[i-k][j+k] == num):
                    count += 1
                else: 
                    processar_sequencia(count)
                    count = 0
            processar_sequencia(count)
    return seq_tamanhos

matrix = [
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
]

num = 1

matrix2 = [
    [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 4],
    [2, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5],
    [3, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 6],
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#print(verifica_diagonais(matrix2, num)) 

#https://www.youtube.com/watch?v=FH9BxnzumVo
def diagonais(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    print(linhas, colunas)

    res =[]

    linha_atual = 0
    coluna_atual = 0
    subindo = True

    while(len(res) != linhas * colunas):
        if subindo:
            while linha_atual >= 0 and coluna_atual < colunas:
                res.append(matriz[linha_atual][coluna_atual])

                linha_atual -= 1
                coluna_atual += 1

            if coluna_atual == colunas:
                coluna_atual -= 1
                linha_atual += 2
            else: 
                linha_atual += 1

            subindo = False
        else: 
            while linha_atual < linhas and coluna_atual >= 0:
                res.append(matriz[linha_atual][coluna_atual])

                coluna_atual -= 1
                linha_atual += 1

            if linha_atual == linhas:
                coluna_atual += 2
                linha_atual -= 1

            else:
                coluna_atual += 1

            subindo = True

    return res

print(diagonais(matrix2))
