#!/usr/bin/python3
"""Module that prints a square with the character #.
"""


def print_square(size):
    """Prints a square of size x size using the '#' character.

    Args:
        size: integer, the length of the square's sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
