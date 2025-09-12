#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module supplies one function, matrix_divided().
For example,

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix
    """
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required "
                        "argument: 'matrix'")
    if div is None:
        raise TypeError("matrix_divided() missing 1 required argument: 'div'")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # divide all elems and round to 2 decimals
    new_matrix = [[round(elem / div, 2)for elem in row] for row in matrix]
    return new_matrix
