# Escreva um programa em Python que aplique o Teorema de Pitágoras (h2=c2 + c2) para calcular a hipotenusa de um triângulo rectângulo a partir dos comprimentos dos dois catetos introduzidos pelo utilizador. 

from math import sqrt

c1 = eval(input("Introduza o valor do primeiro cateto: "))
c2 = eval(input("Introduza o valor do segundo cateto: "))

resul = sqrt((c1 ** 2) + (c2 ** 2))

print("O valor da hipotenusa é:", resul)