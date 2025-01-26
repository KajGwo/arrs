arr = [2, 3, 2, 5, 8, 1, 9, 8]
z = []
y = []


for i in range(len(arr)):
    if arr[i] not in z:
        z.append(arr[i])
    else:
        y.append(arr[i])
    
y = set(y)
arr = set(arr)
    


        
print(arr - y)