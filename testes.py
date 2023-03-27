import minimax
import numpy as np

JOGADAS_MINIMAX = []
JOGADAS_PLAYER = []

ESTADO = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

# ESTADO = np.zeros((15,15), dtype=int)
nova_matriz = np.zeros((15,15))
print(type(nova_matriz))
print(type(ESTADO))

#JOGADA PLAYER
ESTADO[4][4] = 2
JOGADAS_PLAYER.append((4, 4))
print(f'Jogada PLAYER: {4}, {4}')
for linha in ESTADO:
    print(linha)
print('\n\n')

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 3, JOGADAS_PLAYER, JOGADAS_MINIMAX, (4,4))
JOGADAS_MINIMAX.append(jogada)
ESTADO[jogada[0]][jogada[1]] = 1
for linha in ESTADO:
    print(linha)
print('\n\n')

#JOGADA PLAYER
ESTADO[3][4] = 2
JOGADAS_PLAYER.append((3, 4))
print(f'Jogada PLAYER: {3}, {4}')
for linha in ESTADO:
    print(linha)
print('\n\n')

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 3, JOGADAS_PLAYER, JOGADAS_MINIMAX, (3,4))
JOGADAS_MINIMAX.append(jogada)
ESTADO[jogada[0]][jogada[1]] = 1
for linha in ESTADO:
    print(linha)
print('\n\n')

#JOGADA PLAYER
ESTADO[5][5] = 2
JOGADAS_PLAYER.append((5, 5))
print(f'Jogada PLAYER: {5}, {5}')
for linha in ESTADO:
    print(linha)
print('\n\n')

#ATÉ AQUI FUNCIONA

# print(JOGADAS_PLAYER)
# print(JOGADAS_MINIMAX)

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 3, JOGADAS_PLAYER, JOGADAS_MINIMAX, (5,5))
JOGADAS_MINIMAX.append(jogada)
print(jogada)
ESTADO[jogada[0]][jogada[1]] = 1
for linha in ESTADO:
    print(linha)
print('\n\n')


#JOGADA PLAYER
ESTADO[8][7] = 1
JOGADAS_MINIMAX.append((8, 7))
ESTADO[8][6] = 1
JOGADAS_MINIMAX.append((8, 6))
ESTADO[8][5] = 1
JOGADAS_MINIMAX.append((8, 5))
ESTADO[8][4] = 1
JOGADAS_MINIMAX.append((8, 4))

ESTADO[9][7] = 2
JOGADAS_PLAYER.append((9, 7))

for linha in ESTADO:
    print(linha)
print('\n\n')

jogada = minimax.jogar(ESTADO, 2, JOGADAS_PLAYER, JOGADAS_MINIMAX, (9, 7))
JOGADAS_MINIMAX.append(jogada)
print(jogada)
ESTADO[jogada[0]][jogada[1]] = 1
for linha in ESTADO:
    print(linha)
print('\n\n')
