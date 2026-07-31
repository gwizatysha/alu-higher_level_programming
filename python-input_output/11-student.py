#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and
reload."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names to retrieve.
                If not a list of strings, all attributes are retrieved.
        """
        valid = isinstance(attrs, list)
        if valid:
            valid = all(isinstance(attr, str) for attr in attrs)
        if valid:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a
        dictionary.

        Args:
            json (dict): dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
