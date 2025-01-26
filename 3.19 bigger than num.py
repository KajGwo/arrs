arr = [7,9,2,4,5,6]

x = int(input("givnum "))

y = sum(1 for num in arr if num > x)

print("array",arr)
print("Threshold", x)
print("Number of elements greater than" ,x, "=", y)