def conta_menores (lista, menor):
    num_menores = 0
    for i in range (len(lista)):
        if lista[i] < menor:
            num_menores += 1
    return num_menores

print (conta_menores([3, 4, 5, 6, 7,], 5))
