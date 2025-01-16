###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
y = -1 
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Second to last value', arr[len(arr) - 2])
print('sum of first and second', arr[(len(arr) - 1)] + arr[(len(arr) - len(arr))])
print('mid val', arr[int(len(arr)/2)])
for i in range(len(arr)):
    y+=2
    arr.insert(y, " ")
    
print(arr)

