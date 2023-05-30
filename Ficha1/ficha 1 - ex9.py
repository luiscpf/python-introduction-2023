# Escreva um programa em Python que lê três números e que diz qual o maior dos números lidos. 

prim = int(input("Introduza o primeiro número: "))
segu = int(input("Introduza o segundo número: "))
terc = int(input("Introduza o terceiro número: "))

if (prim > segu and prim > terc):
    print("O maior número é o:", prim)

elif (segu > prim and segu > terc):
    print("O maior número é o:", segu)
        
else:
    print("O maior número é o:", terc)        