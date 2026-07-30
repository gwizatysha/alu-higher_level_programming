#!/usr/bin/python3
"""Module that defines a Rectangle class with a string representation."""


class Rectangle:
    """Represents a rectangle defined by its width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle. Must be an integer
                greater than or equal to 0.
            height: The height of the rectangle. Must be an integer
                greater than or equal to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with validation.

        Args:
            value: The new width. Must be an integer greater than or
                equal to 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with validation.

        Args:
            value: The new height. Must be an integer greater than or
                equal to 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current perimeter of the rectangle.

        Returns 0 if either the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle printed with the '#' character.

        Returns an empty string if either the width or the height
        is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)
