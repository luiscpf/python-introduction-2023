def duplica(t):
    tf = ()
    for i in range (0,len(t)):
        tf += (t[i],t[i],)
        
    return tf
        
tuplo = (1,2,3)
print(duplica(tuplo))