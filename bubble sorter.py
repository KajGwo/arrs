arr = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
#bank_transactions = [-150, -20, 300, -45, -60, 500, -120]




for i in range(len(arr) - 1):
     s = False
     for y in range(0, len(arr) - i - 1):
          if arr[y] > arr[y + 1]:
               temp = arr[y]
               arr[y] = arr[y + 1]
               arr[y + 1] = temp
               s = True
     if not s:
          break

    
          

   
     
     


     
print((arr))