#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Represents a square defined by its size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The length of one side of the square. Must be an
                integer greater than or equal to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation.

        Args:
            value: The new size. Must be an integer greater than or
                equal to 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
