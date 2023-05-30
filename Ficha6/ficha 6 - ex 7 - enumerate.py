def posicoes_lista(lista, elemento):
    posicao = ()        
    for indice, pos in enumerate (lista):
        if pos == elemento:
            posicao += (indice,)
    return posicao
   
print(posicoes_lista(['a', 2, 'b', 'a'], 'a'))
