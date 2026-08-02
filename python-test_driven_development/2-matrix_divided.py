#!/usr/bin/python3
"""Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of integers or floats
        div: integer or float divisor

    Returns:
        list of lists: new matrix with divided values

    Raises:
        TypeError: if matrix is not a valid matrix of ints/floats,
            if rows are not the same size, or div is not a number
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) == 0 or not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
