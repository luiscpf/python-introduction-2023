#Escreva uma função em Python, com o nome conta_menores que recebe um tuplo contendo números inteiros e um número inteiro e que devolve o número de elementos do tuplo que são menores do que esse inteiro.


def conta_menores (lista, menor):
    num_menores = 0
    indice = 0
    while indice < (len(lista)):
        if lista[indice] < menor:
            num_menores += 1
        indice += 1
    return num_menores

print (conta_menores([3, 4, 5, 6, 7,], 5))
