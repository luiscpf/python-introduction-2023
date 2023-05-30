#Escreva uma função em Python, com o nome conta_menores que recebe um tuplo contendo números inteiros e um número inteiro e que devolve o número de elementos do tuplo que são menores do que esse inteiro.

def conta_menores (tuplo, valor_a_testar):
    contagem = 0
    for elemento in tuplo:
        if elemento < valor_a_testar:
            contagem += 1
    return contagem

print (conta_menores([3, 4, 5, 6, 7,], 5))
    