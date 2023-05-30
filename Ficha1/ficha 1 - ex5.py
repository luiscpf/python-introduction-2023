# Escreva um programa em Python que pede ao utilizador que lhe forneça um inteiro correspondente a um número de segundos e que calcula o número de dias correspondentes a esse número em segundos. O seu programa deve permitir a interação: 
# Escreva um número em segundos
# ? 65433998
# O número de dias correspondentes é 757.3263657407407


s = int(input("Escreva um número em segundos: "))

dias = s / 86400

print(dias,"dias");