import numpy as np
import random

# LINHA = 15
# COLUNA = 15 

matriz = np.zeros((15,15))

player = 2
minimax = 1

jogadas_player = []
jogadas_minimax = []


def verificar_jogada(matriz, jogada):
    if jogada[0] < 0 or jogada[0] > 14:
        return False
    
    if jogada[1] < 0 or jogada[1] > 14:
        return False

    if matriz[jogada] == 0:
        return True
    else:
        return False

def jogar(matriz, jogada, player):
    if verificar_jogada(matriz, jogada):
        matriz[jogada] = player
        return True
    else:
        False

def heuristica(jogadas_player, jogadas_minimax, player_atual, matriz):
    # FAZ A PRIMEIRA JOGADA DE TODAS NO CENTRO
    if len(jogadas_minimax) == 0 and len(jogadas_player) == 0:
        jogar(matriz, (7, 7), player_atual)
        return ((7, 7))

    # FAZ A PRIMEIRA JOGADA EM VOLTA DA DA JOGADA DO PLAYER
    if len(jogadas_minimax) == 0 and len(jogadas_player) == 1:
        while True:
            linha = random.randint(jogadas_player[0][0] - 1, jogadas_player[0][0] + 1)
            coluna = random.randint(jogadas_player[0][1] - 1, jogadas_player[0][1] + 1)

            if jogar(matriz, (linha, coluna), player_atual):
                break
        return ((linha, coluna))
    
    # FAZ A SEGUNDA JOGADA EM VOLTA DA DA JOGADA DO MINIMAX
    if len(jogadas_minimax) == 1 and (len(jogadas_player) == 1 or len(jogadas_player) == 2):
        while True:
            linha = random.randint(jogadas_minimax[0][0] - 1, jogadas_minimax[0][0] + 1)
            coluna = random.randint(jogadas_minimax[0][1] - 1, jogadas_minimax[0][1] + 1)

            if jogar(matriz, (linha, coluna), player_atual):
                break
        return ((linha, coluna))

    return False

jogar(matriz, (5,5), player)
jogadas_player.append((5,5))
print(f'{matriz}\n\n')

jogadas_minimax.append((heuristica(jogadas_player, jogadas_minimax, minimax, matriz)))
print(f'{matriz}\n\n')

jogar(matriz, (5,6), player)
jogadas_player.append((5,6))
print(f'{matriz}\n\n')

jogadas_minimax.append((heuristica(jogadas_player, jogadas_minimax, minimax, matriz)))
print(f'{matriz}\n\n')



