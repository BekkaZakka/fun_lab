arr =    [[3, 6, 9],
          [2, 4, 8],
          [1, 2, 3]]

def matrix(arr):
    rotated_matrix = [list(reversed(row)) for row in zip(*arr)]
    return rotated_matrix

nine_matrix = matrix(arr)
print(nine_matrix)
