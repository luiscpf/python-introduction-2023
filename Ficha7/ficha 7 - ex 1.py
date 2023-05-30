#Escreva a função agrupa_por_chave que dada uma lista de pares chave valor (k, v) (representados por tuplos de dois elementos) devolve um dicionário que a cada chave k associa uma lista com os valores v, para essa chave encontrados na lista passada como argumento.

def agrupa_por_chave (lista_recebida):
    lista_retorno = {}
    for elemento in lista_recebida:
        chave = elemento[0]
        valor = elemento[1]
        if chave in lista_retorno:
            lista_retorno[chave] += [valor]
        else:
            lista_retorno[chave] = [valor]

    return lista_retorno
        
print(agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)]))