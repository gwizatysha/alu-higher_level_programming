#!/usr/bin/python3
"""Module that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append text to filename (UTF8), creating it if needed.

    Returns:
        int: the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
