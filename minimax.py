'''
def verificar_jogada(self, linha, coluna):
        if linha < 0 or linha > TABULEIRO_LARGURA:
            return False
        if coluna < 0 or coluna > TABULEIRO_ALTURA:
            return False

        if (self.matriz[linha][coluna] == 1 or self.matriz[linha][coluna] == 2):
            return False
        else:
            return True

    def jogar(self, linha, coluna, jogador):

        if self.verificar_jogada(linha, coluna):
            self.matriz_copia = copy.deepcopy(self.matriz)
            self.jogos.append(self.matriz_copia) # Cria uma cópia do estado atual e adiciona na lista de estados

            print(f'LINHA: {linha} - COLUNA: {coluna}')

            if jogador.jogador_peca == 1:
                self.matriz[linha][coluna] = 1
                return True
            else:
                self.matriz[linha][coluna] = 2
                return True
        return False
        
'''

def valor_heuristico(estado, jogador):
    pass

def gerar_filhos(estado, jogador):
    pass

def jogo_final(estado):
    pass

def obter_sequencias(matriz,jogador):
    linha = len(matriz)
    coluna = len(matriz[0])
    seq_tamanhos = []

    def processar_sequencia(count):
        if count >= 2:
            seq_tamanhos.append(count)

    # Verificar horizontal
    for i in range(linha):
        count = 0
        for j in range(coluna):
            if matriz[i][j] == jogador:
                count += 1
            else:
                processar_sequencia(count)
                count = 0
        processar_sequencia(count)

    # Verificar vertical
    for j in range(coluna):
        count = 0
        for i in range(linha):
            if matriz[i][j] == jogador:
                count += 1
            else:
                processar_sequencia(count)
                count = 0
        processar_sequencia(count)

    # Verifica diagonal principal
    for i in range(linha - 4):
        for j in range(coluna - 4):
            count = 0
            for k in range(5):
                if (matriz[i+k][j+k] == jogador):
                    count += 1
                else: 
                    processar_sequencia(count)
                    count = 0
            processar_sequencia(count)

    # Verifica diagonal secundária
    for i in range(4, linha):
        for j in range(coluna - 4):
            count = 0
            for k in range(5):
                if (matriz[i-k][j+k] == jogador):
                    count += 1
                else: 
                    processar_sequencia(count)
                    count = 0
            processar_sequencia(count)

    return seq_tamanhos





def minimax(estado, profundidade, jogador_max, alfa, beta):
    if profundidade == 0 or jogo_final(estado):
        return valor_heuristico(estado, jogador_max)
    
    if jogador_max:
        valor_max = float("-inf")
        for filho in gerar_filhos(estado):
            valor = minimax(filho, profundidade-1, False, alfa, beta)
            valor_max = max(valor_max, valor)
            alfa = max(alfa, valor_max)
            if beta <= alfa:
                break
        return valor_max
    else:
        valor_min = float("inf")
        for filho in gerar_filhos(estado):
            valor = minimax(filho, profundidade-1, True, alfa, beta)
            valor_min = min(valor_min, valor)
            beta = min(beta, valor_min)
            if beta <= alfa:
                break
        return valor_min

matrix = [
    [1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
]

num = 1

print(obter_sequencias(matrix, num)) 