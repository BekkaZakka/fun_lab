def matrix_operation(matrix1, matrix2, operation):
    rows = len(matrix1)  # Количество строк в матрицах
    cols = len(matrix1[0])  # Количество столбцов в матрицах

    # Проверяем, что размеры матриц одинаковы для операций сложения и вычитания
    if operation in ('+', '-'):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Размеры матриц не совпадают")

    result = [[0] * cols for _ in range(rows)]  # Создаем матрицу-результат

    # Выполняем операцию сложения, вычитания или умножения
    for i in range(rows):
        for j in range(cols):
            if operation == '+':
                result[i][j] = matrix1[i][j] + matrix2[i][j]
            elif operation == '-':
                result[i][j] = matrix1[i][j] - matrix2[i][j]
            elif operation == '*':
                result[i][j] = 0
                for k in range(cols):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
            else:
                raise ValueError("Неподдерживаемая операция")

    return result  # Возвращаем результат операции

# Пример использования функции
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Матрица 1:")
for row in matrix1:
    print(row)

print("Матрица 2:")
for row in matrix2:
    print(row)

operation = '*'  # Задаем операцию: +, -, или *

result = matrix_operation(matrix1, matrix2, operation)
print("Результат операции {}:".format(operation))
for row in result:
    print(row)
