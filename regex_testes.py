import re

'''
Este arquivo é igual o regex.py, mas com os prints para debug
'''

regras_jogador1 = {
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

regras_jogador2 = {
    1: {'regex': ['20{4}', '020{3}', '0{3}20', '0{4}2'], 'pontos': 10**1},
    2: {'regex': ['0{2}20{2}'], 'pontos': 10**2},
    3: {'regex': ['2{2}00+', '02{2}00+', '0{3}2{2}0', '0{4}2{2}', '20200+', '020200+', '0{2}2020', '0{3}202'], 'pontos': 10**3},
    4: {'regex': ['0+2{2}0+', '0+2020+', '0{2}20{2}20{2}'], 'pontos': 10**4},
    5: {'regex': ['2{3}00+', '02{3}0', '0{2}2{3}', '2{2}020{2}', '02{2}020', '0{2}2{2}02', '202{2}00+', '0202{2}0', '0{2}202{2}'], 'pontos': 10**5},
    6: {'regex': ['0+2{3}0+', '0+2{2}020+', '0+202{2}0+'], 'pontos': 10**6},
    7: {'regex': ['02{4}0', '2{4}00+', '0{2}2{4}', '2{4}0', '02{4}', '02{3}020', '2{3}0200+', '0{2}2{3}02', '2{3}020', '02{3}02', '0202{3}0', '0{2}202{3}', '202{3}00+', '0202{3}', '202{3}0'], 'pontos': 10**7},
    8: {'regex': ['0+2{4}0+'], 'pontos': 10**8},
    9: {'regex': ['2{5}'], 'pontos': 10**9}
}


def calcular_pontuacao(lista_de_strings, regras): 
    pontuacao_total = 0
    sem_match = []
    for string in lista_de_strings:
        for regra in regras.values():
            for regex in regra['regex']:    
                matches = re.findall(regex, string)
                if matches:      
                    print(f'REGEX.PY/calcular_pontuacao -> string: {string}')
                    print(f'REGEX.PY/calcular_pontuacao -> regra: {regex}')
                    print(f'REGEX.PY/calcular_pontuacao -> Matches: {matches}')
                    print(f"REGEX.PY/calcular_pontuacao -> Pontos: {regra['pontos']}")
                    pontuacao_total += regra['pontos'] 
                    print(f"REGEX.PY/calcular_pontuacao -> Pontuação total: {pontuacao_total}") 
                    print(" ")
                else:
                    sem_match.append(string)
    return pontuacao_total




