def duplica_elementos(lista):
    resultado = ()
    for indice in lista:
        resultado += (indice,indice)
    return resultado

print(duplica_elementos(['a', ['b', 'c'], 5]))