def posicoes_lista(lista, elemento):
    indice = 0
    
    while indice < len(lista):
        if lista[indice] == elemento:
            lista[indice] = indice
        indice += 1
    return lista         

print(posicoes_lista (['a', 2, 'b', 'a'], 'a'))
          