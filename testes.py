import re

# regras = {
#     1: {'regex': ['0+10+'], 'pontos': 1},
#     2: {'regex': ['0{2}10{2}'], 'pontos': 10},
#     3: {'regex': ['0+1{3}0+', '0+1{2}010+', '0+101{2}0+'], 'pontos': 10**2},
#     4: {'regex': ['0+1{4}0+', '0+1{3}010+', '0+101{3}0+', '0+1{2}01{2}0+'], 'pontos': 10**3}
# }

regras = {
    1: {'regex': ['10{4}', '010{3}', '0{3}10', '0{4}1'], 'pontos': 10**1},
    2: {'regex': ['0{2}10{2}'], 'pontos': 10**2},
    3: {'regex': ['1{2}00+', '01{2}00+', '0{3}1{2}0', '0{4}1{2}', '10100+', '010100+', '0{2}1010', '0{3}101'], 'pontos': 10**3},
    4: {'regex': ['0+1{2}0+', '0+1010+', '0{2}10{2}10{2}'], 'pontos': 10**4},
    5: {'regex': ['1{3}00+', '01{3}0', '0{2}1{3}', '1{2}010{2}', '01{2}010', '0{2}1{2}01', '101{2}00+', '0101{2}0', '0{2}101{2}'], 'pontos': 10**5},
    6: {'regex': ['0+1{3}0+', '0+1{2}010+', '0+101{2}0+'], 'pontos': 10**6},
    7: {'regex': ['01{4}0', '1{4}00+', '0{2}1{4}', '1{4}0', '01{4}', '01{3}010', '1{3}0100+', '0{2}1{3}01', '1{3}010', '01{3}01', '0101{3}0', '0{2}101{3}', '101{3}00+', '0101{3}', '101{3}0'], 'pontos': 10**7},
    8: {'regex': ['0+1{4}0+'], 'pontos': 10**8},
    9: {'regex': ['1{5}'], 'pontos': 10**9}
}

# caso = ['0+1{3}0+', '0*1{5}0*']
# string = ["001110101110000"]

# regras_teste = {
#     1: {'regex': ['0+1{3}0+'], 'pontos': 30},
# }

#ESSE FUNCIONA
# def calcular_pontuacao(lista_de_strings, regras):
#     pontuacao_total = 0
#     num_matches = []
#     for string in lista_de_strings:
#         passed = 0
#         for dados in regras.values():
#             for regex in dados['regex']:
#                 matches = re.findall(regex, string)
#                 passed += len(matches)
#                 pontuacao_total += dados['pontos'] * passed
#         num_matches.append(passed)
#     return pontuacao_total, num_matches

# def calcular_pontuacao(lista_de_strings, regras):
#     pontuacao_total = 0
#     for string in lista_de_strings:
#         for dados in regras.values():
#             passed = 0
#             for regex in dados['regex']:
#                 matches = re.findall(regex, string)
#                 if matches:
#                     print(matches)
#                 passed += len(matches)
#         pontuacao_total += dados['pontos'] * passed
#     return pontuacao_total

# def calcular_pontuacao(lista_de_strings, regras):
#     pontuacao_total = 0
#     for string in lista_de_strings:
#         for dados in regras.values():
#             for regex in dados['regex']:
#                 if re.search(regex, string) is not None:
#                     pontuacao_total += dados['pontos']
#                     break
#     return pontuacao_total

def calcular_pontuacao(lista_de_strings, regras): 
    pontuacao_total = 0
    controle = 0
    for string in lista_de_strings:
        for regra in regras.values():
            for regex in regra['regex']:
                if re.findall(regex, string):
                    print(string)
                    print(re.findall(regex, string))
                    #print(regra['pontos'])
                    pontuacao_total += regra['pontos'] #* len(re.findall(regex, string))
                    controle += 1
    print(controle)
    return pontuacao_total

import matrizes

strings = matrizes.obter_linhas_string(matrizes.matriz_teste)
pontuacao = calcular_pontuacao(strings, regras)

print(pontuacao)

# for item in strings:
#     if re.fullmatch('0+', item) is None:
#         print("------------------")
#         print(item)
#         print(num_matches[strings.index(item)])
#         print("------------------")

