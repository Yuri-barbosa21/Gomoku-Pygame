import re

regexes_dict = {
    1 : ['0+1010+'],
    2 : ['0+1{2}010+', '0+1{3}0+'],
    3 : ['0+1{2}010+', '0+1{2}010+', '0+1{3}0+'],
    4 : ['0{2}1{2}01{2}0{2}', '0{2}101{3}0{2}', '0{2}1{3}010{2}', '0{2}1{4}0{2}']
}

regexes = [r'0+1010+', r'0+1{2}010+', r'0+1{3}0+',r'0+1{2}010+', r'0+1{2}010+', r'0+1{3}0+', 
           r'0{2}1{2}01{2}0{2}', r'0{2}101{3}0{2}', r'0{2}1{3}010{2}', r'0{2}1{4}0{2}']


import re

def contar_correspondencias(strings, regexes_dict):
    correspondencias = {}
    for string in strings:
        correspondencias[string] = {}
        for chave, regexes in regexes_dict.items():
            correspondencias[string][chave] = 0
            for regex in regexes:
                correspondencias[string][chave] += len(re.findall(regex, string))
        if sum(correspondencias[string].values()) == 0:
            del correspondencias[string]
    return correspondencias


import minimax, matrizes
matches = contar_correspondencias(matrizes.obter_linhas_string(minimax.matrix), regexes_dict)
print(matches)



