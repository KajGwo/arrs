x = [8, 2, 5, 1, 9,]
z = []
y = 0


for i in range(0, len(x)):
    x[y] = x[y] * x[y]
    y = y+1

print(x) 