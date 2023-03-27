def vizinhanca(estado, i, j):
    if i == 0 and j == 0:
        if estado[i][j+1] != 0 or estado[i+1][j] != 0 or estado[i+1][j+1] != 0:
            return True
    elif i == 0 and j == len(estado[i])-1:
        if estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i+1][j-1] != 0:
            return True
    elif i == len(estado)-1 and j == 0:
        if estado[i][j+1] != 0 or estado[i-1][j] != 0 or estado[i-1][j+1] != 0:
            return True
    elif i == len(estado)-1 and j == len(estado[i])-1:
        if estado[i][j-1] != 0 or estado[i-1][j] != 0 or estado[i-1][j-1] != 0:
            return True
    elif i == 0:
        if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i+1][j+1] != 0 or estado[i+1][j-1] != 0:
            return True
    elif i == len(estado)-1:
        if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i-1][j] != 0 or estado[i-1][j+1] != 0 or estado[i-1][j-1] != 0:
            return True
    elif j == 0:
        if estado[i][j+1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0 or estado[i-1][j+1] != 0 or estado[i+1][j+1] != 0:
            return True
    elif j == len(estado[i])-1:
        if estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0 or estado[i+1][j-1] != 0 or estado[i-1][j-1] != 0:
            return True
    else:
        if estado[i][j+1] != 0 or estado[i][j-1] != 0 or estado[i+1][j] != 0 or estado[i-1][j] != 0 or estado[i+1][j+1] != 0 or estado[i+1][j-1] != 0 or estado[i-1][j+1] != 0 or estado[i-1][j-1] != 0:
            return True
    return False



estado = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

estado2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

for i in range(len(estado)):
    for j in range(len(estado)):
        if estado[i][j] == 0:
            if vizinhanca(estado, i, j):
                print(f'({i}, {j})')
                estado2[i][j] = 3

for linha in estado2:
    for elemento in linha:
        print(elemento, end=' ')
    print()