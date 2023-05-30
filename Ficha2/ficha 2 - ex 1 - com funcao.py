# Escreva um programa em Python que aplique o Teorema de Pitágoras (h2=c2 + c2) para calcular a hipotenusa de um triângulo rectângulo a partir dos comprimentos dos dois catetos introduzidos pelo utilizador. 

from math import sqrt
def calculo_hipotenusa(cateto_1, cateto_2): 
    """
    função que calcula a hipotenusa com o teorema de pitagoras 
    input: dois catetos
    output: valor da hipotenusa
    """
    
    return sqrt((cateto_1 ** 2) + (cateto_2 ** 2))

c1 = eval(input("Introduza o valor do primeiro cateto: "))
c2 = eval(input("Introduza o valor do segundo cateto: "))

print("O valor da hipotenusa é:", calculo_hipotenusa(c1, c2))