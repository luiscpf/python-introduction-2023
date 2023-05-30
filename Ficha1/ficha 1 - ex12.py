#1 pedir numero 

valor_int = eval(input("Escreva um inteiro \n? "))
resultado = ""

#2 descobrir pares ou impar

while valor_int > 0:
    
    #2.1 isolar digito

    digito = valor_int % 10
    
    #2.2 testar digito
    #2.2.1 testar par ou impar
    
    if digito % 2 != 0:
        
        #2.2.2 guardar digito impar
        
        resultado = str(digito) + resultado # ou resultado += str(digito) (é a mesma coisa)
     
    #2.3 eliminar digito   
        
    valor_int = valor_int // 10     # ou valor_int // 10 (é a mesma coisa)
    
#3 retornar resultado
#3.1 mostrar resultado
#3.2 inverter resultado

print("Resultado :", resultado) #[::-1] inverter o texto
