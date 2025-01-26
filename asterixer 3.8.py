x = [2, 6, 4, 9, 7]
y = 0
z = []

def star(n):
    res = len(n)
    return res

for i in range(0, (len(x))):
    y = y+1
    z.append("*"*x[y - 1])
    print(z[y - 1], star(z[y - 1]))




     
