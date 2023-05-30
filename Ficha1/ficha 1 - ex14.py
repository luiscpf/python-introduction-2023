# Escreva um programa em Python que pede ao utilizador que lhe forneça um número e que escreve a tabuada da multiplicação para esse número. 

valor_int = eval(input("Indique a tabuada que necessita: "))
controlo = 0

while controlo <=10:
    
    print(valor_int, "x", controlo, "=",valor_int * controlo)
    controlo += 1