#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :.
"""


def text_indentation(text):
    """Prints text, adding 2 new lines after each ., ? or : character.

    Args:
        text: string to format and print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip() for line in result.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    print("\n".join(lines), end="")
