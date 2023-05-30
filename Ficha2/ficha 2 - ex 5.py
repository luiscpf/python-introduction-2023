# Partindo do programa realizado anteriormente, crie um novo programa que calcula a soma de todos os números apresentados ao utilizador

num = eval(input(" Insira um número entre 1 e 15: "))
cont = num
soma = 0

while cont <= 15:
    print("n =", cont)
    soma += cont
    cont += 1

print("O resultado total é:", soma)