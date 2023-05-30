# Implemente um programa em Python, que recebe dois valores e verifica qual é o maior

def valores(n1, n2):
    if n1 > n2:
        print("O maior valor é: ", n1)
    
    else:
        print("O maior valor é: ", n2)
    return

n1 = eval(input("Digite o primeiro valor: "))
n2 = eval(input("Digite o segundo valor: "))

valores(n1, n2)