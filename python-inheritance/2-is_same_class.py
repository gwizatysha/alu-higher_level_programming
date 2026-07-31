#!/usr/bin/python3
"""Module that defines a function to check exact class membership."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return type(obj) is a_class
