from matrix import Matrix, IncompatibleMatrixError, DimensionMismatchError

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

# Тестирование сложения
try:
    matrix_sum = matrix1 + matrix2
    print("Сумма матриц:")
    print(matrix_sum)
except DimensionMismatchError as e:
    print("Ошибка сложения:", e)

# Тестирование умножения на скаляр
scalar = 2
matrix_scaled = matrix1 * scalar
print("Матрица, умноженная на скаляр:")
print(matrix_scaled)

# Тестирование умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

try:
    matrix_scaled = matrix1 * matrix3
    print("Результат умножения матриц:")
    print(matrix_scaled)
except IncompatibleMatrixError as e:
    print("Ошибка умножения матриц:", e)

# Тестирование равенства матриц
print("Проверка равенства матриц:")
print(matrix1 == matrix2)  # Должно быть False
print(matrix1 == matrix1)  # Должно быть True
