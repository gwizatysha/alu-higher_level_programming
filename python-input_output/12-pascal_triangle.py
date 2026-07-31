#!/usr/bin/python3
"""Module that defines a function to compute Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's Triangle.

    Args:
        n (int): number of rows of the triangle.

    Returns:
        list: an empty list if n <= 0, otherwise the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
