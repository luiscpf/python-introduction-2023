#a
for i in range (1,6):
    for j in range (1,4):
        if (i % j) == 1:
            print(i + j)
            
#b
i = 20
while i > 5:
    print(4*i)
    i = i-2
    
#c
for i in range (1):
    for j in range (3,5):
        for k in range (5,1,-2):
            if (i + j) % 2 == 0:
                print(i,j,k)
        