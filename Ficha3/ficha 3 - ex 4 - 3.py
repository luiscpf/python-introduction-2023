def calcula_troco(moedas_e_notas, valor):
    
    """
    Função que calcula o troco
    Input:
         -moedas_e_notas: tuplo com a sequencia de notas e moedas
         -valor: flot com o valor a testar
    Output:
         -devolucoes: tuplo com a quatidade de moedas e notas pela sequancia de moedas_e_notas
    """
    
    devolucoes = ()
    for moeda_ou_nota in moedas_e_notas:
        devolve = 0
        while valor >= moeda_ou_nota:
            devolve += 1
            valor -= moeda_ou_nota
        devolucoes += (devolve,)
    return devolucoes

def mostra_resultado (moedas_e_notas, moedas_e_notas_a_imprimir): 
    for moeda_ou_nota_indice in range (0, len(moedas_e_notas), 1):
        if moedas_e_notas [moeda_ou_nota_indice] > 2:
            print ("Devolve ", moedas_e_notas_a_imprimir[moeda_ou_nota_indice], "nota(s) de ", moedas_e_notas[moeda_ou_nota_indice] )
        elif moedas_e_notas [moeda_ou_nota_indice] >= 1:
            print("Devolve ", moedas_e_notas_a_imprimir[moeda_ou_nota_indice], "moeda(s) de ", moedas_e_notas[moeda_ou_nota_indice] )
        else:
            print("Devolve ", moedas_e_notas_a_imprimir[moeda_ou_nota_indice], "moeda(s) de ", moedas_e_notas [moeda_ou_nota_indice] *100, "centimos")
        return
    
valor_a_testar = eval(input("Indique o valor a trocar: "))

moedas_e_notas_a_testar = (50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)

mostra_resultado(moedas_e_notas_a_testar, calcula_troco(moedas_e_notas_a_testar, valor_a_testar))
