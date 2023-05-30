def substitui(t,old,new):
    res = ()
    for i in t:
        if i == old:
            res += (new,)
        else:
            res += (i,)
    return res

lista = (1,2,3,2,2,5)
print(substitui(lista,2,'a'))