# Gomoku-Pygame
# Projeto Gomoku

Este projeto consiste na aplicação do algoritmo Minimax no jogo Gomoku. O objetivo era otimizar o desempenho do jogo e isso foi alcançado através de várias melhorias implementadas ao longo do desenvolvimento.

## Sobre o Projeto

O jogo foi totalmente codificado em Python. Para a parte visual, utilizamos a biblioteca Pygame. A otimização foi auxiliada pelo uso de expressões regulares (Regex).

A implementação do algoritmo Minimax foi realizada sem o auxílio de qualquer biblioteca de inteligência artificial. Isso significa que todo o código foi escrito e otimizado manualmente para garantir o melhor desempenho possível.

## Estrutura do Código

O código do projeto é dividido em vários arquivos para facilitar a manutenção e a compreensão do código. Os principais arquivos são:

- `gomoku.py`: Arquivo principal com a implementação do jogo, todo o visual foi feito com a biblioteca PyGames.

- `minimax.py`: Este arquivo contém a implementação do algoritmo Minimax. Ele inclui funções para calcular o valor heurístico de um estado, gerar filhos de um estado, verificar se um jogo chegou ao fim, e fazer uma jogada usando o algoritmo Minimax.

- `matrizes.py`: Este arquivo contém funções para manipular matrizes, que são usadas para representar o estado do jogo. Ele inclui funções para obter as linhas, colunas e diagonais de uma matriz, converter as linhas de uma matriz em strings, remover zeros de uma matriz, calcular a pontuação de um estado, verificar se uma jogada é válida, e diminuir o tamanho de uma matriz.

- `regex.py`: Este arquivo contém as regras para calcular a pontuação de um estado. As regras são expressões regulares que correspondem a padrões específicos na matriz do jogo.

## Links Úteis

- [Artigo sobre o projeto](https://dev.to/vinipetra/como-fizemos-uma-ia-jogar-gomoku-48mk)


## Nota

O código da implementação do jogo com o Pygame não está incluído neste README, pois não é necessário para entender a lógica do algoritmo Minimax e as otimizações que foram feitas. No entanto, você pode encontrar o código completo no repositório do GitHub mencionado acima.
