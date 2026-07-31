#!/usr/bin/python3
"""Module that defines a Square class with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, built on top of Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The length of each side. Must be a positive
                integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description: [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
