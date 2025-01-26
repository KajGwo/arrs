arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]


def find_smallest_largest(array):
    min_value = int()
    max_value = int()
    min_position = (-1, -1)
    max_position = (-1, -1)

    for row_idx, row in enumerate(array):
        for col_idx, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_position = (row_idx, col_idx)
            if value > max_value:
                max_value = value
                max_position = (row_idx, col_idx)

    return min_value, max_value, min_position, max_position



min_value, max_value, min_position, max_position = find_smallest_largest(arr)
print(f"Tsmallest is {min_value} at {min_position[0]}, {min_position[1]}.")
print(f"laargeset {max_value} at {max_position[0]}, {max_position[1]}.")
