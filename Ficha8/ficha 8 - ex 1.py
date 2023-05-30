def pedir_numero(numero):
    if numero < 1 or numero > 20:
        return "Número inválido!"
    else:
        return "Número aceite!"
    
numero = eval(input('Introduza um número entre 1 e 20: '))

print(pedir_numero())