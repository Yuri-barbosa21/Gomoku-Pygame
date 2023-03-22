
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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0],
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

num_elementos_diagonais = []

# iterar sobre cada elemento da matriz
for i in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        
        # calcular a diagonal que passa pelo elemento (i,j)
        diagonal = []
        k, l = i, j
        while k < len(matrix2) and l < len(matrix2[0]):
            diagonal.append(matrix2[k][l])
            k += 1
            l += 1
        
        # adicionar o número de elementos na diagonal à lista
        num_elementos_diagonais.append(len(diagonal))

# imprimir o número de elementos em cada diagonal
#print(num_elementos_diagonais)
def diagonals(matrix, num):
    for i in range(0, len(matrix)):
        for j in 
        