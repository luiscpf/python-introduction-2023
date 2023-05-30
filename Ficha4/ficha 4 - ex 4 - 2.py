def duplica (tuplo_recebido):
    if type(tuplo_recebido) != tuple:
        print("Não é um tuplo")
        return -1
    tuplo_duplicado = ()
    for elemento_do_tuplo in tuplo_recebido:
        tuplo_duplicado += (elemento_do_tuplo,elemento_do_tuplo)
    return tuplo_duplicado

tuplo = (1, 2, 3)
print(duplica(tuplo))