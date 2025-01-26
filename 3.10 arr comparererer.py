x = [4,36,12,28,9,44,5]
y = [5,1,36]
z = []
a = -1



for i in range(len(x)):
    a = a + 1
    if x[a] not in y:
        z.append(x[a])




print(z)

