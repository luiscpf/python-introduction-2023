def soma_quadrados_while(tuplo):
    soma = 0
    indice = 0
    while indice < len(tuplo):
        soma += tuplo[indice] ** 2
        indice += 1
    return soma

print(soma_quadrados_while((1,2,3)))
