def cria_lista_multiplos(numero, numero2):
    if (numero % 1) != 0 or numero <= 0:
        return 'Número inválido!'
    else:
        tuplo = ()
        countador = 0
        indice = 0
        while countador < numero2:
            if (indice % numero) == 0:
                countador += 1
                tuplo += (indice,)
            indice += 1
        return tuplo
    
num_intr = eval(input('Insira um número inteiro positivo: '))
num_ped = eval(input('Insira o número de multiplos que quer: ')) 
print(cria_lista_multiplos(num_intr, num_ped))