#!/usr/bin/python3
"""Module that returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return a dictionary description of obj using simple data structures."""
    return obj.__dict__
