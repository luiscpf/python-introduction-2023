def posicoes_lista(lista, elemento):
    posicao = ()
    for indice in range(0,len(lista)):
        if lista[indice] == elemento:
            posicao += (indice,)
    return posicao
print(posicoes_lista (['a', 2, 'b', 'a'], 'a'))