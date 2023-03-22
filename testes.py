
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
    [2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 4],
    [0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5],
    [3, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 2, 0, 0],
    [9, 0, 0, 0, 3, 0, 3, 0, 3, 0, 2, 0, 0, 0]
]

#print(verifica_diagonais(matrix2, num)) 

#https://www.youtube.com/watch?v=FH9BxnzumVo
def diagonais(matriz):
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

def count_sequences(matrix, number):
    """
    Conta a quantidade de sequências seguidas do número em cada lista da matriz.
    Retorna um array com as contagens.
    """
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

# for a in matrix2:
#     print(a)

# diags1 = diagonais(matrix2)
# for b in diags1:
#     print(b)

# rodada = rodar_matriz(matrix2)
# for c in rodada:
#     print(c)

# diags2 = diagonais(rodada)
# for d in diags2:
#     print(d)

# print(count_sequences(diags1, 2))
# print(count_sequences(diags2, 3))

def obter_tamanhos_sequencias(matriz, num_jogador):
    diags = diagonais(matriz)
    matriz_rodada = rodar_matriz(matriz)
    diags_sec = diagonais(matriz_rodada)
    for line in diags_sec:
        diags.append(line)
    tudo = diags + matriz + matriz_rodada
    return(count_sequences(tudo, num_jogador))

print(obter_tamanhos_sequencias(matrix2, 2))
