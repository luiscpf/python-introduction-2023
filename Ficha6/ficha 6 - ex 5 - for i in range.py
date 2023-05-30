def substitui(lista_recebida, velho, novo):
            
    for indice in range (len(lista_recebida)):
        if lista_recebida[indice] == velho:
            lista_recebida[indice] = novo
    return lista_recebida

print(substitui ([1, 2, 3, 2, 4], 2, 'a'))