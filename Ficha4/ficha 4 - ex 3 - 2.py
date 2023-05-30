def filtra_pares (tuplo_recebido):
    if type(tuplo_recebido) != tuple:
        print("Não é um tuplo")
        return -1
    tuplo_filtrado = ()
    for elemento_do_tuplo in tuplo_recebido:
        if elemento_do_tuplo % 2 == 0:
            tuplo_filtrado += (elemento_do_tuplo,) # tem de ter virgula no fim
    return tuplo_filtrado

tuplo = (1, 5, 6, 7, 2, 3, 2, 4, 5, 6, 7)
print(filtra_pares(tuplo))

