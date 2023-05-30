# Elabore um programa que peça ao utilizador para introduzir sucessivas vezes um número inferior a 100 e que vá calculando o respectivo somatório, o qual vai ser escrito no ecrã, até que o valor desse somatório atinja ou ultrapasse o valor 500. Uma vez terminado esse ciclo deve ser escrito no ecrã a média dos valores válidos introduzidos.


cont = 0
contagem = 0

while cont < 500:
    numero_introduzido = eval(input("Introduza um número inferior a 100: "))
    if numero_introduzido >= 1 and numero_introduzido <= 100:
        cont += numero_introduzido
        print("\nValor acomulado:", cont)
        contagem += 1

        
    else:
        print("Numero não aceite")
        
print("A média é de:", cont / contagem)
        
        
             
