a = [1,2,3,4,5]
print(a)
a[0] = a[0] - 1
print(a)
a[len(a) - 1] = a[len(a) - 1] + 4
print(a)
a[int(len(a)/2)] = a[int(len(a)/2)] * 2
print(a)