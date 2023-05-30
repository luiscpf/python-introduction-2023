#Escreva uma função em Python com o nome soma_quadrados que recebe um número inteiro positivo, n, e tem como valor a soma dos quadrados de todos os números inteiros de 1 até n.

def soma_quadrados (numero_a_testar):
    soma = 0
    
    for i in range (1, numero_a_testar + 1, 1):
        soma = i ** 2
    return soma

valor = eval(input("Introduza um valor: "))
print(soma_quadrados(valor))
