arr1 = [1, 2, 3,]
arr2 = [1, 2, 3, 4, 5]
z = []
y = -1

for i in arr1:
    y = y+1
    if arr1[y] == arr2[y]:
        z.append(arr1[y])
    

if arr1 == z:
    print("yippee") 
else:
    print("AAAAAA")