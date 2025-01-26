def comp(n,y):
    z = 0
    if len(n) != len(y):
        return False
    for i in range(len(n)):
         z = z+1
    if n[z - 1] != y[z - 1]:
        return False
    else:
        return True

a = input("enterr array n1")
b = input("enterr array n2")

print(a, b, comp(a,b))


