import unittest
from matrix.matrix import Matrix


class TestMatrixMethods(unittest.TestCase):
    def test_matrix_creation(self):
        matrix = Matrix(2, 2)
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.cols, 2)

    def test_matrix_addition(self):
        matrix1 = Matrix(2, 2)
        matrix2 = Matrix(2, 2)
        result = matrix1 + matrix2
        expected = Matrix(2, 2)
        self.assertEqual(result, expected)

    def test_matrix_multiplication(self):
        matrix1 = Matrix(2, 3)
        matrix2 = Matrix(3, 2)
        result = matrix1 * matrix2
        expected = Matrix(2, 2)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
