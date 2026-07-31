#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited,
    directly or indirectly, from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
