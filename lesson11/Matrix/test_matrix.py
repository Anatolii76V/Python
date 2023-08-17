from matrix import Matrix

# Создание матриц
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Вывод матриц
print("Матрица 1:")
print(matrix1)

print("Матрица 2:")
print(matrix2)

# сложение
matrix_sum = matrix1 + matrix2
print("Сумма матриц:")
print(matrix_sum)

# умножение
scalar = 2
matrix_scaled = matrix1 * scalar
print("Умножение")
print(matrix_scaled)

# умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix_mult = matrix1 * matrix3
print("Результат умножения матриц:")
print(matrix_mult)

# Сравнение матриц
print("Сравнение матриц:")
print(matrix1 == matrix2)  # Должно быть False
print(matrix1 == matrix1)  # Должно быть True
