import minimax

JOGADAS_MINIMAX = []
JOGADAS_PLAYER = []

ESTADO = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#JOGADA PLAYER
ESTADO[4][4] = 1
JOGADAS_PLAYER.append((4, 4))
print(f'Jogada PLAYER: {4}, {4}')

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 3, JOGADAS_PLAYER, JOGADAS_MINIMAX, (4,4))
JOGADAS_MINIMAX.append(jogada)
ESTADO[jogada[0]][jogada[1]] = 2

#JOGADA PLAYER
ESTADO[4][3] = 1
JOGADAS_PLAYER.append((4, 3))
print(f'Jogada PLAYER: {4}, {3}')

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 3, JOGADAS_PLAYER, JOGADAS_MINIMAX, (4,3))
JOGADAS_MINIMAX.append(jogada)
ESTADO[jogada[0]][jogada[1]] = 2

#JOGADA PLAYER
ESTADO[4][2] = 1
JOGADAS_PLAYER.append((4, 2))
print(f'Jogada PLAYER: {4}, {2}')

#ATÉ AQUI FUNCIONA

print(JOGADAS_PLAYER)
print(JOGADAS_MINIMAX)

#JOGADA MINIMAX
jogada = minimax.jogar(ESTADO, 2, JOGADAS_PLAYER, JOGADAS_MINIMAX, (4,2))
JOGADAS_MINIMAX.append(jogada)
print(jogada)
ESTADO[jogada[0]][jogada[1]] = 2