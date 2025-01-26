
arr1 = []
x = int(input("lenght?"))
for i in range(x):
     y = int(input("num?"))
     arr1.append(y)
     

n = len(arr1)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

print(arr1)