#Usando um ciclo for, escreva uma função em Python que recebe uma quantia em Euros e calcula o número de notas de 50€, 20€, 10€, 5€ e moedas de 2€, 1€, 50 cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos e 1 cêntimo, necessário para perfazer, essa quantia, utilizando sempre o máximo número de notas e moedas para cada quantia, da mais elevada para a mais baixa.

def dinheiro(x):
    euros = int(x)
    centimos = round((x - euros)*100)
    
    for e in (50,20,10,5,2,1):
        n = euros // e
        euros = euros % e
        if e == 1:
            print(n,"moeda(s) de",e,"euro")
        if e == 2:
            print(n,"moeda(s) de",e,"euros")            
        else:
            print(n,"nota(s) de",e,"euros")
            
    for e in (50,20,10,5,2,1):
        n = centimos // e
        centimos = centimos % e
        if e == 1:
            print(n,"moeda(s) de",e,"centimo")
        else:
            print(n,"nota(s) de",e,"centimos")
    return dinheiro
        
valor = eval(input('Introduza um valor: '))
print("O troco é: ")
dinheiro(valor)
print("Volte sempre e compre mais!")