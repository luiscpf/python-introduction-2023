def substitui(lista_recebida, velho, novo):
            
    for indice, elemento in enumerate (lista_recebida):
        if elemento == velho:
            lista_recebida[indice] = novo
    return lista_recebida
   
print(substitui ([1, 2, 3, 2, 4], 2, 'a'))