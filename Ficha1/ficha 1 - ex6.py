# Escreva um número que lê um número inteiro correspondente a um certo número de segundos e que escreve o número de dias, horas, minutos e segundos correspondentes a esse número. Por exemplo
#Escreva o número de segundos 345678
# dias: 4 horas: 0 mins: 1 segs: 18

seg = int(input("Escreva o número em segundos: "))
          
dias = seg // 86400
seg_rest = seg % 86400
horas = seg_rest // 3600
seg_rest = seg_rest % 3600
minutos = seg_rest // 60
seg_rest = seg_rest % 60

print(seg_rest);