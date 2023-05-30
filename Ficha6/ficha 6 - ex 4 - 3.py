def cria_lista_multiplos (numero):
    if isinstance(numero, int) and numero > 0:
        lista_retorno = []
        for indice in range(10):
            lista_retorno += [elemento*numero]
        return lista_retorno
    else:
        raise ValueError ("O número indicado não é inteiro positivo")