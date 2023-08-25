import logging
import argparse

logging.basicConfig(filename='matrix_operations.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

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
        else:
            logger.error("Ошибка при сложении матриц")
            raise ValueError("Матрицы должны иметь одинаковые размеры для сложения")

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
        else:
            logger.error("Ошибка при умножении матриц")
            raise ValueError("Несовместимое умножение матриц")

    def print(self):
        """
        Выводит матрицу на печать.
        """
        for row in self.data:
            print(" ".join(map(str, row)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Матричные операции')
    parser.add_argument('--rows1', type=int, default=2, help='Количество строк матрицы 1')
    parser.add_argument('--cols1', type=int, default=3, help='Количество столбцов матрицы 1')
    parser.add_argument('--rows2', type=int, default=2, help='Количество строк матрицы 2')
    parser.add_argument('--cols2', type=int, default=3, help='Количество столбцов матрицы 2')
    parser.add_argument('--scalar', type=float, default=2, help='Скаляр для умножения')
    args = parser.parse_args()

    matrix1 = Matrix(args.rows1, args.cols1)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(args.rows2, args.cols2)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    print("Матрица 1:")
    matrix1.print()

    print("Матрица 2:")
    matrix2.print()

    try:
        matrix_sum = matrix1 + matrix2
        print("Сумма матриц:")
        matrix_sum.print()
    except ValueError as e:
        print(e)

    try:
        matrix_scaled = matrix1 * args.scalar
        print("Умножение матрицы на скаляр:")
        matrix_scaled.print()
    except ValueError as e:
        print(e)

    try:
        matrix_mult = matrix1 * matrix2
        print("Умножение матриц:")
        matrix_mult.print()
    except ValueError as e:
        print(e)

    print("Сравнение матриц:")
    print(matrix1 == matrix2)  # Должно быть False
    print(matrix1 == matrix1)  # Должно быть True

# Перехожу в директорию: (venv) pc@pc-desktop:~/PycharmProjects/lesson15/venv$
# Запускаю командой: python matrix_operations.py --rows1 2 --cols1 3 --rows2 2 --cols2 3 --scalar 2
