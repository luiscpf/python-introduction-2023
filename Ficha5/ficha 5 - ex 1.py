#Um número inteiro, n, diz-se triangular se existir um inteiro m tal que n = 1 +2 + ...+ (m-1)+ m. Escreva uma função chamada triangular que recebe um número inteiro positivo n, e cujo valor é True apenas se o número for triangular. No caso de n ser 0 deverá devolver False.

def triangular (numero_a_testar):
    soma = 0
    for numero in range (numero_a_testar + 1):
        soma += numero
        if soma == numero_a_testar:
            return True
        elif soma > numero_a_testar:
            return False
    return False