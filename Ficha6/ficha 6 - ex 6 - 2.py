def remove_repetidos (lista):
    for i in range (len(lista) -1, 0 -1):
        if lista [i] in lista [0:i]:
            del (lista[i])
    return lista
        