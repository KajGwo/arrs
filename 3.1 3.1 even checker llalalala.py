x = [34,7,19,4,21,8]
z = []
y = 0


while y < len(x):
    if x[y] % 2 == 0:
        z.append(x[y])
        y = y+1
    elif x[y] % 2 == 1:
        y = y+1
    elif y == len(x):
        break
    

print(z, len(z))