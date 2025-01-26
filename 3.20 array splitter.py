arr = [7,9,2,4,5,6]
x = []
z=[]
y = -1

for i in arr:
    y = y+1
    if arr[y] % 2 == 0:
        z.append(i)
    else:
        x.append(i)



print(z + x)