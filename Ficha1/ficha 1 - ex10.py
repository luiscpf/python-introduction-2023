# Escreva um programa em Python que pede ao utilizador que lhe forneça um número correspondente a um ano e que indica se o ano é bissexto. Um ano é bissexto se for divisível por 4 e não for divisível por 100, a não ser que seja também divisível por 400. Por exemplo, 1984 é bissexto, 1100 não é, e 2000 é bissexto. O seu programa deve gerar uma interação como a seguinte:
# Escreva um ano para eu dizer se é bissexto
# Ano -> 1984
# O ano 1984 é bissexto 

ano = int(input("Escreva um ano para eu dizer se é bissexto: "))

if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
    print("É Bissexto")
else:
    print("Não é Bissexto")