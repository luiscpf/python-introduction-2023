def remove_multiplos(tuplo, numero):
    resultado = ()
    for indice in tuplo:
        if (indice % numero) != 0:
            resultado += (indice,)
    return resultado

print(remove_multiplos((2,3,5,9,12,33,34,45),3))