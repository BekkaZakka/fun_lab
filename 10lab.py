# 1 есеп unique

# input_string = input("Введите строку: ")
# unique_chars = []
# for char in input_string:
#     if char not in unique_chars:
#         unique_chars.append(char)
# unique_chars.sort()
# print("Уникальные символы в алфавитном порядке:", ''.join(unique_chars))
   

# 2 есеп any and all

# num = [1, 2, 3, 4, 5, 6]
# words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# number_5 = any(n > 5 for n in num)
# print("хотя бы одно число, больше 5?", number_5)

# all_num = all(n % 2 == 0 for n in num)
# print("Все четные?", all_num)

# c_word = any(word.startswith('c') for word in words)
# print("хотя бы одно слово, начинающееся на букву 'c'?", c_word)

# long_3 = all(len(word) > 3 for word in words)
# print("Все слова в списке длиннее 3 символов?", long_3)


# 3 есеп zip, list, reversed

# arr =    [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# def matrix(arr):
#     rotated_matrix = [list(reversed(row)) for row in zip(*arr)]
#     return rotated_matrix

# nine_matrix = matrix(arr)
# print(nine_matrix)


# 4 есеп enumerate, len, max

# ves = [3, 2, 4, 1]
# values = [5, 3, 8, 2]
# max_ves = 3

# def rukzak(ves, values, max_ves):
#     n = len(ves)
#     dp = [0] * (max_ves + 1)
#     for i, v in enumerate(ves):
#         for j in reversed(range(v, max_ves + 1)):
#             dp[j] = max(dp[j], dp[j - v] + values[i])
#     return dp[max_ves];

# max_value = rukzak(ves, values, max_ves)
# print("Max value:", max_value)


# 5 есеп

matrix1 = [[1, 2], [4, 5], [7, 8]]
matrix2 = [[9, 8], [6, 5], [3, 2]]

def matrix_operation(matrix1, matrix2, operation):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Матрицы имеют разные размеры"

    result = []
    for i, row1 in enumerate(matrix1):
        row_res = []
        for j, (elem1, elem2) in enumerate(zip(row1, matrix2[i])):
            if operation == "+":
                row_res.append(elem1 + elem2)
            elif operation == "-":
                row_res.append(elem1 - elem2)
            elif operation == "*":
                elem_res = sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))])
                row_res.append(elem_res)
        result.append(row_res)
    return result

result = matrix_operation(matrix1, matrix2, "+")
print(result)  

result = matrix_operation(matrix1, matrix2, "-")
print(result) 

result = matrix_operation(matrix1, matrix2, "*")
print(result) 

