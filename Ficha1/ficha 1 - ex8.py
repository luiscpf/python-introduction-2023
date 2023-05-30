# Faça um programa, que peça ao utilizador um número entre 1 e 5. Se o utilizador introduzir um número diferente, o programa retorna a mensagem “Número não aceite!” e solicita nova introdução de um número. Se a introdução for correcta, mostra no ecrã o número introduzido.

num = int(input("Introduza um número entre 1 e 5: "))

if (num >= 1 and num <= 5):
    print("O número introduzido foi:",num)   
else: 
    print("Número não aceite")
    


         
         