def crossover(lista):
    lista1 = []
    lista2 = []
    listaFinal = []
    tamanho = len(lista)

    for i in range(tamanho):
        lista1.append(lista[i][0])
        lista2.append(lista[i][1])

    for item in lista1:
        for item2 in lista2:
            listaFinal.append([item,item2])
    
    return listaFinal



con = [
    [0,1],
    [2,3],
    [4,5],
    [6,7],
    [8,9]
        ]
  
print(crossover(con))
    