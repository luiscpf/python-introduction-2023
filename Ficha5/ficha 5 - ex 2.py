#Um número d é divisor de n se o resto da divisão de n por d for 0. Escreva uma função com o nome num_divisores que recebe um número inteiro positivo n, e tem como valor o número de divisores de n. No caso de n ser 0 deverá devolver 0.

def num_divisores(numero_a_testar):
    soma_divisores = 0 
    for indice in range(1, numero_a_testar + 1):
        if indice == 0:
            raise ZeroDivisionError("Está a dividir por zero")
        if (numero_a_testar % indice) == 0:
            soma_divisores += 1
    return soma_divisores