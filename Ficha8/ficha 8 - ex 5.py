def soma_quadrados_valores (dicionario):
    resultado = 0
    
    for valor in dicionario:
        resultado +=  dicionario[valor] * dicionario[valor]
    return resultado

print(soma_quadrados_valores ({"a" : 2, "b" : 5, "c" : 3}))
    