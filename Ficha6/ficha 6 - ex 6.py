def remove_repetidos (lista):
    res = []
    
    for i in lista:
        if i not in res:
            res += [i]
    return res

print(remove_repetidos ([2, 4, 3, 2, 2, 2, 3]))