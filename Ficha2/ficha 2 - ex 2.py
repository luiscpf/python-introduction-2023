# Implemente um programa em Python que lê duas notas introduzidas pelo utilizador e imprime uma mensagem indicativa se o aluno foi aprovado ou não, juntamente com a média obtida. O aluno fica aprovado se a média for superior ou igual a 9.5. O seu programa deverá gerar uma interação como a seguinte (exemplo): 

n1 = eval(input("Escreva a primeira nota: "))
n2 = eval(input("Escreva a segunda nota: "))

media = (n1+n2) / 2

if media >= 9.5:
    print("Aprovado com média de:", media)
    
else:
    print("Reprovado com média de:", media)