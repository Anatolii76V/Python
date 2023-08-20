class MatrixError(Exception):
    """Базовый класс для исключений, связанных с матрицами."""
    pass


class IncompatibleMatrixError(MatrixError):
    """Исключение, вызываемое при попытке выполнить некомпатибельное умножение матриц."""

    def __init__(self, message="Несовместимое умножение матриц"):
        self.message = message
        super().__init__(self.message)


class DimensionMismatchError(MatrixError):
    """Исключение, вызываемое при попытке сложения матриц разных размеров."""

    def __init__(self, message="Матрицы должны иметь одинаковые размеры для сложения"):
        self.message = message
        super().__init__(self.message)


class PositiveMatrixError(MatrixError):
    """Исключение, вызываемое при попытке создать матрицу с отрицательными значениями."""

    def __init__(self, message="Матрица должна содержать только положительные значения"):
        self.message = message
        super().__init__(self.message)


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def set_value(self, row, col, value):  # метод set_value, проверяет значение перед записью.
        if value <= 0:
            raise PositiveMatrixError()
        self.data[row][col] = value

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        raise DimensionMismatchError()

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        elif isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
            return result
        raise IncompatibleMatrixError()

    def print(self):
        """
        Выводит матрицу на печать.
        """
        for row in self.data:
            print(" ".join(map(str, row)))
