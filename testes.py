import matrizes, regex, minimax

#15x15
ESTADO = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

mini = minimax.Minimax("Minimax", "Brancas")

#Parte do jogo
jogadas_player = []
jogadas_minimax = []

#Tamanho da matriz
print(f'Tamanho da matriz: {len(ESTADO)}x{len(ESTADO[0])}')


#====================================================================================================
#Testes de verficar jogadas
#====================================================================================================

print("INICIO DE TESTES DE JOGADAS VÁLIDAS E INVÁLIDAS")
print(" ")

#Jogada válida
jogada_verificar_linha = 0
jogada_verificar_coluna = 14
print(f'A jogada ({jogada_verificar_linha}, {jogada_verificar_coluna}) é {mini.verificar_jogada(ESTADO, (jogada_verificar_linha, jogada_verificar_coluna))}')
print(" ")

#Jogada inválida (SE (0, 0) for 1)
jogada_verificar_linha = 0
jogada_verificar_coluna = 0
print(f'A jogada ({jogada_verificar_linha}, {jogada_verificar_coluna}) é {mini.verificar_jogada(ESTADO, (jogada_verificar_linha, jogada_verificar_coluna))} <- (0, 0) != 0')
print(" ")

#====================================================================================================
#Testes da Heurística
#====================================================================================================

#Limpar a matriz para testes limpos
ESTADO[0][0] = 0

##Jogada do minimax

print("INICIO DOS TESTES DE HEURÍSTICA")
print("")

#Deve retornar (7,7) pois é a primeira jogada da partida e é a vez do minimax
jogada_1_minimax = mini.heuristica(jogadas_player, jogadas_minimax, ESTADO)
print(" ")

#Registro da jogada do Minimax e atualização do estado
jogadas_minimax.append(jogada_1_minimax)
ESTADO[jogada_1_minimax[0]][jogada_1_minimax[1]] = 1

#for linha in ESTADO: print(linha)
#print(" ")

print(f'Jogadas do Minimax: {jogadas_minimax}')
print(f'Jogadas do Player: {jogadas_player}')
print(" ")

##Jogada do player

jogadas_player.append((6, 6))
ESTADO[6][6] = 2

#for linha in ESTADO: print(linha)

print(f'Jogadas do Minimax: {jogadas_minimax}')
print(f'Jogadas do Player: {jogadas_player}')
print(" ")


##Jogada do minimax

jogada_2_minimax = mini.heuristica(jogadas_player, jogadas_minimax, ESTADO)
print(" ")

#Registro da jogada do Minimax e atualização do estado
jogadas_minimax.append(jogada_2_minimax)
ESTADO[jogada_2_minimax[0]][jogada_2_minimax[1]] = 1

#for linha in ESTADO: print(linha)

print(f'Jogadas do Minimax: {jogadas_minimax}')
print(f'Jogadas do Player: {jogadas_player}')
print(" ")

##Jogada do player

jogadas_player.append((7, 6))
ESTADO[7][6] = 2

#for linha in ESTADO: print(linha)

print(f'Jogadas do Minimax: {jogadas_minimax}')
print(f'Jogadas do Player: {jogadas_player}')
print(" ")

#====================================================================================================
#Testes Jogadas Minimax
#====================================================================================================

print("INÍCIO TESTES MATRIZ REDUZIDA")
print(" ")

##Teste da reduzida

#estado_reduzido = matrizes.diminuir_matriz(ESTADO, jogadas_player[(len(jogadas_player) - 1)])
estado_reduzido = matrizes.diminuir_matriz(ESTADO, jogadas_minimax[(len(jogadas_minimax) - 1)])
print("Estado reduzido:")
for linha in estado_reduzido: print(linha)
print(" ")

#====================================================================================================
#Testes de Vizinhança
#====================================================================================================

print("INÍCIO TESTES VIZINHANÇA")
print(" ")

##Teste da vizinhança 

def teste_vizinhanca(estado):
    jogadas_possiveis = []
    for i in range(len(estado)):
        for j in range(len(estado[i])):
               if estado[i][j] == 0 and matrizes.vizinhanca(estado, i, j):
                     jogadas_possiveis.append((i, j))
    print("Jogadas possíveis pela vizinhança:")
    for line in jogadas_possiveis: print(line)
    print(" ")
    return jogadas_possiveis
                    
teste_vizinhanca(estado_reduzido)

#====================================================================================================
#Comparação de vizinhança completa e reduzida
#====================================================================================================

print("INÍCIO COMPARAÇÃO VIZINHANÇA COMPLETA E REDUZIDA")
print(" ")

import time

#Vizinhança completa:
print("Vizinhança completa:")
inicio_completa = time.time()
vizinhança_completa = teste_vizinhanca(ESTADO)
tempo_completa = time.time() - inicio_completa

#Vizinhança reduzida:
print("Vizinhança reduzida:")
inicio_reduzida = time.time()
estado_reduzido_tempo = matrizes.diminuir_matriz(ESTADO, jogadas_minimax[(len(jogadas_minimax) - 1)])
vizinhança_reduzida = teste_vizinhanca(estado_reduzido_tempo)
tempo_reduzida = time.time() - inicio_reduzida

print("COMPARAÇÃO DE TEMPO DE EXEXUÇÃO DA VIZINHANÇA COMPLETA E REDUZIDA")
print(" ") 

print(f'Tempo de execução da vizinhança completa: {tempo_completa}')
print(f'Tempo de execução da vizinhança reduzida: {tempo_reduzida}')
print(f'Diferença de tempo: {tempo_completa - tempo_reduzida}')

#====================================================================================================
#Teste da remoção de zeros
#====================================================================================================

print("INÍCIO TESTES REMOÇÃO DE ZEROS")
print(" ")

##Teste da remoção de zeros

teste_remover_zeros = matrizes.obter_linhas_string(ESTADO)

print("Estado atual")
for linha in ESTADO: print(linha)
print("")

print("obter_linhas_string sem os zeros:")
for line in teste_remover_zeros: print(line)
print("")

#====================================================================================================
#Teste cálculo de valor heurístico
#====================================================================================================

print("INÍCIO TESTES CÁLCULO DE VALOR HEURÍSTICO")
print(" ")

##Teste do cálculo de valor heurístico

print("Estado atual")
for linha in ESTADO: print(linha)
print("")

##Teste do Regex
print("Cálculo do valor heurístico pelo REGEX")

#Todas as direções após remoção dos zeros
print("Todas as direções após remoção dos zeros")
linhas_estado_sem_zeros = matrizes.obter_linhas_string(ESTADO)
for linha in linhas_estado_sem_zeros: print(linha)
print("")

#Cálculo do valor heurístico no REGEX
print("String, regras e matches")
valor_teste_1 = regex.calcular_pontuacao(linhas_estado_sem_zeros, regex.regras_jogador1)
print(f'Valor heurístico do estado atual para o jogador 1: {valor_teste_1}')
print(" ")

#Calculo do valor heurístico pelas matrizes
print("Cálculo do valor heurístico pelas matrizes")
valor_teste_2 = matrizes.calcular_pontuacao(ESTADO, 1)
print(f'Valor heurístico do estado atual para o jogador 1: {valor_teste_2}')
print(" ")

#Comparação dos resultados
print(f"Diferença na pontuação: {valor_teste_1 - valor_teste_2}")
