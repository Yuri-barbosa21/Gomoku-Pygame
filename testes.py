import re

regras = {
    1: {'regex': ['0+10+'], 'pontos': 10},
    2: {'regex': ['0+1{2}0+', '0+1010+'], 'pontos': 20},
    3: {'regex': ['0+1{3}0+', '0+1{2}010+', '0+101{2}0+'], 'pontos': 30},
    4: {'regex': ['0+1{4}0+', '0+1{3}010+', '0+101{3}0+', '0+1{2}01{2}0+'], 'pontos': 40}
}

caso = ['0+1{3}0+', '0*1{5}0*']
string = ["001110101110000"]

regras_teste = {
    1: {'regex': ['0+1{3}0+'], 'pontos': 30},
}

def calcular_pontuacao(lista_de_strings, regras):
    pontuacao_total = 0
    num_matches = []
    for string in lista_de_strings:
        passed = 0
        for dados in regras.values():
            for regex in dados['regex']:
                matches = re.findall(regex, string)
                passed += len(matches)
                pontuacao_total += dados['pontos'] * passed
        num_matches.append(passed)
    return pontuacao_total, num_matches

# def calcular_pontuacao(lista_de_strings, regras):
#     pontuacao_total = 0
#     for string in lista_de_strings:
#         for dados in regras.values():
#             for regex in dados['regex']:
#                 if re.search(regex, string) is not None:
#                     pontuacao_total += dados['pontos']
#                     break
#     return pontuacao_total


import matrizes
import pandas as pd

strings = matrizes.obter_linhas_string(matrizes.matriz_teste)
pontuacao, num_matches = calcular_pontuacao(strings, regras)

for item in strings:
    if re.fullmatch('0+', item) is None:
        print("------------------")
        print(item)
        print(num_matches[strings.index(item)])
        print("------------------")
