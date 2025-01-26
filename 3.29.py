rows = 3
cols = 5


def arrayer(x, y):
    array = []
    for _ in range(x):
        row = [0] * y
        array.append(row)
    return array


array = arrayer(rows, cols)
for row in array:
    print(row)

