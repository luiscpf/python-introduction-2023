#Defina uma função, junta_ordenados, que recebe dois tuplos contendo inteiros, ordenados por ordem crescente, e devolve um tuplo também ordenado com os elementos dos dois tuplos.

def junta_ordenados(t1,t2):
    indice_t1 = 0
    indice_t2= 0
    resultado = ()
    
    while indice_t1 < len (t1) and indice_t2 < len (t2):
        if t1[indice_t1] <= t2[indice_t2]:
            resultado += (t1[indice_t1],)
            indice_t1 += 1
        else:
            resultado += (t2[indice_t2],)
            indice_t2 += 1  
    resultado = resultado + t1[indice_t1:] + t2[indice_t2:]
    return resultado