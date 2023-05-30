def juntos(t):
    counter = 0
    for i in range (len(t), -1, 1):
        if t[i] == t[i+1]:
                counter += 1
            
    return counter

tuplo = (1,2,2,3,4)
print(juntos(tuplo))