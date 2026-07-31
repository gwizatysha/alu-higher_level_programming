#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an integer validator."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception, since area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: The name of the value being validated, used in any
                error message raised.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
