def repete (tuplo_recebido, repeticoes):
    if type(tuplo_recebido) != tuple:
        print("Não é um tuplo")
        return -1
    
    tuplo_duplicado = ()
    
    for elemento_do_tuplo in tuplo_recebido:
        for e in range (repeticoes):
            tuplo_duplicado += (elemento_do_tuplo,)
    return tuplo_duplicado

tuplo = (1, 2, 3)
repeticoes = 10
print(repete(tuplo, repeticoes))