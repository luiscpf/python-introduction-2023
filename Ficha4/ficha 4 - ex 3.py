def filtra_pares(t):
    tf = ()
    for i in range (0,len(t)):
        if (t[i] % 2) == 0:
            tf += (t[i],)
            
    return tf

tuplo = (1,2,2,3,3,3,7,9,4)
print(filtra_pares(tuplo))