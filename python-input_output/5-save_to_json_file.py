#!/usr/bin/python3
"""Module that writes an Object to a text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of my_obj to filename."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
