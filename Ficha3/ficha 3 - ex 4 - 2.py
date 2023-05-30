valor = eval(input(" Indique o valor a trocar: "))

moedas_e_notas = (50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01)

for moeda_ou_nota in moedas_e_notas:
    devolve = 0
    
    while valor >= moeda_ou_nota:
        devolve += 1
        valor -= moeda_ou_nota
        
    if moeda_ou_nota > 2:
        print("Devolve", devolve, "nota(s) de", moeda_ou_nota, "euro(s)")
    elif moeda_ou_nota >= 1:
        print("Devolve", devolve, "moeda(s) de", moeda_ou_nota, "euro(s)")
    else:
        print ("Devolve", devolve,"modeda(s) de", moeda_ou_nota*100, "centimos")