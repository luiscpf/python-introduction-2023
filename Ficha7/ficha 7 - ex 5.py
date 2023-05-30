#Escreva uma função em Pyhton que recebe um dicionário cujos valores associados às chaves correspondem a lista de inteiros e que devolve o dicionário que se obtém "invertendo" o dicionário recebido no qual as chaves são os inteiros que correspondem aos valores do dicionário original e os valores são as chaves do dicionário original às quais os valores estão associados.

dic = {"a" : [1, 2], "b" : [1], "c" : [3], "d" : [4]}

def inverter (dicionario):
    novo_dicionario = {}
    
    for chave in dicionario:
        for valor in dicionario[chave]:
            if valor not in novo_dicionario:
                novo_dicionario[valor] = [chave]
            else:
                novo_dicionario[valor] += [chave]
    return novo_dicionario

def imprime_dicionario (dicionario):
    
    for chave in dicionario:
        print (chave, ":", dicionario[chave])
    
imprime_dicionario(inverter(dic))