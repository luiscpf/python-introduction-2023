def remove_multiplos(tuplo, numero):
    resultado = []
    for indice in range (len(tuplo)):
        if tuplo[indice] % numero != 0:
            resultado += [tuplo[indice]]
    return resultado

print(remove_multiplos((2,3,5,9,12,33,34,45),3)) 