def juntos(t):
    counter = 0
    for i in range (0,len(t)):
        if i < len(t) - 1:
            if t[i] == t[i+1]:
                counter += 1
            
    return counter

tuplo = (1,2,2,3,4)
print(juntos(tuplo))