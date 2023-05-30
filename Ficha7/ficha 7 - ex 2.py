# Uma carta de jogar é caracterizada por um naipe (espadas, copas, ouros e paus) e por um valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). Uma carta pode ser representada por um dicionário com duas chaves, 'np', e 'vlr', sendo um conjunto de cartas representado por uma lista de cartas.
# a. Escreva uma função em Pyhton que devolve uma lista contendo todas as cartas de um baralho.
# b. Recorrendo à função random (), a qual produz um número aleatório no intervalo [0,1[, escreva a função baralha, que recebe uma lista correspondente a um baralho de cartas e baralha aleatoriamente essas cartas, devolvendo a lista que corresponde às cartas baralhadas. Sugestão: percorra sucessivamente as cartas do baralho trocando cada uma delas por uma outra carta selecionada aleatoriamente.

from random import random

def baralho ():
    lista_retornar = []
    for naipe in ["espadas", "copas", "ouros", "paus"]:
        for valor in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            lista_retornar += [{"naipe":naipe, "valor":valor}]
    return lista_retornar

def baralha (lista_baralhar):
    
    for indice_atual in range (len(lista_baralhar)):
        
        numero_aleatorio = int(random()*len(lista_baralhar))
        lista_baralhar[indice_atual], lista_baralhar[numero_aleatorio] = lista_baralhar[numero_aleatorio], lista_baralhar[indice_atual]
        
    return lista_baralhar

print(baralha(baralho()))

def imprime_lista_cartas (lista_imprimir_dicionarios):
    
    for carta in lista_imprimir_dicionarios:
        print (carta["naipe"], "-", carta["valor"])
    
imprime_lista_cartas(baralha(baralho()))