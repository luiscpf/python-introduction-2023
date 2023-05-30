# Utilizando a função area_circulo do exercício anterior, escreva uma função com o nome area_coroa que recebe dois argumentos, r1 e r2, e tem como valor a área da coroa circular de raio interior r1 e raio exterior r2. A sua função deverá gerar um erro de valor (ValueError) se o valor de r1 for maior que o valor de r2

from ficha3_ex2 import area_circulo

def area_coroa (r_1, r_2):
    if r_1 > r_2:
        raise ValueError ("O raio interior é maior que o raio exterior")
    else:
        area_coroa = area_circulo (r_2) - area_circulo (r_1)
    return area_coroa
    
area_ext = eval(input("Insira raio exterior: "))
area_int = eval(input("Insira raio interior: "))

# 0.1 numero de casas (decimais)
# % dados
# f virgula flutuante

print("Area da coroa é: %0.01f" %area_coroa(area_int, area_ext))