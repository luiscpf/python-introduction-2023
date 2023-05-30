# Implemente um programa em Python, recorrendo ao ciclo while, que pede ao utilizador um número inteiro entre 1 e 15 e que mostra a contagem crescente do número até 15 a partir do número introduzido pelo utilizador

num = eval(input(" Insira um número entre 1 e 15: "))
cont = num

while cont <= 15:
    print("n =", cont)
    cont += 1