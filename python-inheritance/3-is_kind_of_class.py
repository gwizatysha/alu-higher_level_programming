#!/usr/bin/python3
"""Module that defines a function to check class membership including
inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a class that
    inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return isinstance(obj, a_class)
