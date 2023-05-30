#Escreva uma função em Python com o nome junta_ordenadas que recebe como argumentos duas listas ordenadas por ordem crescente e devolve uma lista também ordenada com os elementos das duas listas. Não é necessário validar os argumentos da sua função.

def junta_ordenadas(l1,l2):
    indice_l1 = 0
    indice_l2= 0
    resultado = []
    
    while indice_l1 < len (l1) and indice_l2 < len (l2):
        if l1[indice_l1] <= l2[indice_l2]:
            resultado += (l1[indice_l1],)
            indice_l1 += 1
        else:
            resultado += (l2[indice_l2],)
            indice_l2 += 1  
    resultado = resultado + l1[indice_l1:] + l2[indice_l2:]
    return resultado