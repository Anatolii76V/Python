import pytest
from matrix.matrix import Matrix


def test_matrix_creation():
    matrix = Matrix(2, 2)
    assert matrix.rows == 2
    assert matrix.cols == 2


def test_matrix_addition():
    matrix1 = Matrix(2, 2)
    matrix2 = Matrix(2, 2)
    result = matrix1 + matrix2
    expected = Matrix(2, 2)
    assert result == expected


def test_matrix_multiplication():
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(3, 2)
    result = matrix1 * matrix2
    expected = Matrix(2, 2)
    assert result == expected
