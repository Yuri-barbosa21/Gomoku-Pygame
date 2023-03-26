import numpy as np

matriz = np.zeros((15,15))

jogada = (5, 5)
#matriz[(0,0)] = 1
matriz[jogada] = 1
# matriz[(5,4)] = 2
# matriz[(5,6)] = 3
# matriz[(5,7)] = 4
# matriz[(5,8)] = 5
# matriz[(5,9)] = 6

print(matriz)


def diminuir_matriz(matriz, jogada):
    x = 4
    y = 4
    linha_inicio = 0
    coluna_inicio = 0
    linha_fim = 0
    coluna_fim = 0
    nova_matriz = np.zeros((9,9))
    
    if jogada[0] + x > 14:
        linha_inicio = jogada[0] - x
        linha_fim = 15

        if jogada[1] + y > 14:
            coluna_inicio = jogada[1] - y
            coluna_fim = 15

        if jogada[1] < y:
            coluna_inicio = 0
            coluna_fim = jogada[1] + y + 1
        
        # print(linha_inicio, linha_fim)
        # print(linha_inicio, linha_fim)

        # print(linha_fim - linha_inicio)
        # print(coluna_fim - coluna_inicio)

        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio))

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

        # print(linha_inicio, linha_fim)
        # print(coluna_inicio, coluna_fim)

        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio))

        for i in range(linha_fim - linha_inicio):
            for j in range(coluna_fim - coluna_inicio):
                nova_matriz[i][j] = matriz[linha_inicio + i][coluna_inicio + j]
    
        return nova_matriz

    # SE A JOGADA LINHA FOR MENOR QUE O TAMANHO DA MATRIZ
    if jogada[0] < x:
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

        # print(linha_inicio, linha_fim)
        # print(coluna_inicio, coluna_fim)

        # CRIA UMA MATRIZ COM O TAMANHO DA LINHA E COLUNA
        nova_matriz = np.zeros((linha_fim - linha_inicio, coluna_fim - coluna_inicio))

        for i in range(linha_fim - linha_inicio):
            for j in range(coluna_fim - coluna_inicio):
                nova_matriz[i][j] = matriz[linha_inicio + i][coluna_inicio + j]
    
        return nova_matriz
    



print(diminuir_matriz(matriz, jogada))


matriz_menor = diminuir_matriz(matriz, jogada)

matriz_menor[(3,4)] = 1

def converter_coord(jogada, jogada_menor):
    x = jogada[0] - abs((jogada_menor[0] - 4))
    y = jogada[1] - abs((jogada_menor[1] - 4))

    return x, y


#print(converter_coord(jogada, (3,4)))

#coord = converter_coord(jogada, (3,4))

#matriz[coord] = 5

#print(matriz)
