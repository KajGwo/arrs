arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


def swap(array):
     for row in array:
        row[0], row[-1] = row[-1], row[0]




print("Arr before")
for row in arr:
    print(row)

swap(arr)

print("\nArr after")
for row in arr:
    print(row)
