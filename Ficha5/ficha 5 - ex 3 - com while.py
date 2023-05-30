# Escreva uma função em Python com o nome soma_quadrados que recebe um número inteiro positivo, n, e tem como valor a soma dos quadrados de todos os números inteiros de 1 até n.

def soma_quadrados (numero_a_testar):
    resultado = 0
    teste = 1
    while teste <= numero_a_testar:
        resultado += teste ** 2
        teste += 1
    return soma

valor = eval(input("Introduza um valor: "))
print(soma_quadrados(valor))