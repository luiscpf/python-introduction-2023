# Escreva um programa que lê um número inteiro e determina quantas vezes aparecem dois zeros seguidos. Por exemplo,
# Escreva um inteiro
# ? 98007640003
# O número tem 3 zeros seguidos

num = eval(input("Escreva um inteiro: "))
count = 0

while num != 0:
    digito = num % 100
    if digito == 0:
        count += 1
    num = num // 10
print(count)