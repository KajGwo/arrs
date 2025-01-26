x = [-15, 8, -31, 47, -2, 19]


for i in range(len(x) - 1):
     s = False
     for y in range(0, len(x) - i - 1):
          if x[y] > x[y + 1]:
               temp = x[y]
               x[y] = x[y + 1]
               x[y + 1] = temp
               s = True
     if not s:
          break
     
print(x[0], x[(len(x) - 1)])