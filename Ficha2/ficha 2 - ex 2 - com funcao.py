# Implemente um programa em Python que lê duas notas introduzidas pelo utilizador e imprime uma mensagem indicativa se o aluno foi aprovado ou não, juntamente com a média obtida. O aluno fica aprovado se a média for superior ou igual a 9.5. O seu programa deverá gerar uma interação como a seguinte (exemplo): 

def verifica_aprovacao(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    if media >= 9.5:
        print("Aprovado com média de:", media)
        
    else:
        print("Reprovado com média de:", media)
    return

n1 = eval(input("Escreva a primeira nota: "))
n2 = eval(input("Escreva a segunda nota: "))

verifica_aprovacao(n1, n2)