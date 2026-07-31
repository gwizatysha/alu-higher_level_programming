#!/usr/bin/python3
"""Module that defines a function to list an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.
    """
    return dir(obj)
