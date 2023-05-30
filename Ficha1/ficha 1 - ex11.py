# Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o ordenado semanal tendo em conta as horas extraordinárias. O salário é calculado do seguinte modo: se o número de horas for menor que 40, então o salário é dado pelo produto do número de horas pelo salário hora, em caso contrário recebe horas extraordinárias as quais são pagas a dobrar. 

sal_horas = eval(input("Coloque quanto recebe por hora: "))
num_horas = eval(input("Coloque quantas horas trabalhou: "))

if (num_horas > 40):
    num_horas_ex = num_horas - 40
    hor_extra = num_horas_ex * (sal_horas * 2)
    total = (sal_horas * 40) + hor_extra
    print("Vai receber: ", total)

else:
    print("Vai receber: ", sal_horas * num_horas)

