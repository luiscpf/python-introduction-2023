def substitui(lista_recebida, velho, novo):
    indice = 0
    
    while indice < len(lista_recebida):
        if lista_recebida[indice] == velho:
            lista_recebida[indice] = novo
        indice += 1
    return lista_recebida           

print(substitui ([1, 2, 3, 2, 4], 2, 'a'))