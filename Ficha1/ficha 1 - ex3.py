#Escreva um programa em Python que pede ao utilizador que lhe forneça dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y). O seu programa deve gerar uma interação como a seguinte: 
# Vou pedir-lhe dois números
# Escreva o primeiro número, x =5
# Escreva o segundo número, y=6
# O valor de (x + 3 * y) * (x - y) é: -23


print("Vou pedir-lhe dois números")
x = eval(input("Escreva o primeiro número: "))
y = eval(input("Escreva o segundo número: "))

c = (x + 3 * y) * (x - y)

print("O resultado da conta (",x,"+ 3 *",y,") * (",x,"-",y,") é:",c);