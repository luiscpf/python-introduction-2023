# Escreva um programa que deve calcular o desconto a efectuar e o montante a pagar após o desconto, supondo que uma empresa vende um produto, cujo preço base por unidade é fornecido pelo utilizador. No entanto, se a quantidade comprada atingir ou ultrapassar as 500 unidades, será efectuado um desconto de 5% e, se essa quantidade ultrapassar as 1000 unidades, o desconto é de 8%. A quantidade a comprar é um dado pedido ao utilizador.

def desconto(quantidade):
    if (quantidade >= 500 and quantidade <= 1000):
        print("\nGanhou um desconto de 5%.\nCom o desconto incluido o preço fica:", (preco_base*quantidade) * 0.95,"€")
        
    elif (quantidade > 1000):
        print("Ganhou um desconto de 8%.\nCom o desconto incluido o preço fica:", (preco_base*quantidade) * 0.92,"€")
            
    else:
        print("O valor fica:", preco_base*quantidade)
    return

preco_base = eval(input("Digite o preço base: "))
quantidade = eval(input("Digite a quantidade que deseja: "))

desconto(quantidade)