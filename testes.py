import re
import matrizes
import minimax

regex1 = re.compile(r'0+1{4}0+')
regex2= re.compile(r'0+1{3}010+')
regex3 = re.compile(r'0+101{3}0+')
regex4 = re.compile(r'0+1{2}01{2}0+')

regex_vencedor = re.compile(r'1{5}')

valores =["00111100", "001110100", "001011100", "001101100"]

regexes = [regex1, regex2, regex3, regex4]

tudo = matrizes.obter_linhas_string(minimax.matrix)

# resultado = []
# for regex in regexes:
#     for valor in tudo:
#         res = re.findall(regex, valor)
#         if res != []:
#             resultado.append(res)

# for item in tudo:
#     print(re.findall(regex_vencedor, item))

# r_vencedor = re.compile(r'1{5}')

for item in tudo:
    if re.search("11111", item):
        print("achei")
        break


