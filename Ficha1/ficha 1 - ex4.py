#Escreva um programa em Python que lê os valores correspondentes a uma distância percorrida (em Km) e o tempo necessário para a percorrer (em minutos), e calcula a velocidade média em: 

k = eval(input("Digite a distancia percorrida em Km: "))
t = eval(input("Digite o tempo necessário para percorrer em minutos: "))

a = t / 60 
b = k / a

c = b / 3.6

print("A velocidade média em Km /h é:", b, "e em m/s é:",c);