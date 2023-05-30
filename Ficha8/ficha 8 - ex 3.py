def triplica(tuplo):
    res = ()
    for indice in tuplo:
        res += (indice, indice, indice)
    return res
print(triplica((2,0)))
