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

            if jogador.num_peca == 1:
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

def obter_sequencias(estado)


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
