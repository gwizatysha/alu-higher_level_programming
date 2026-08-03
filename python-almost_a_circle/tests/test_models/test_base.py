#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base instantiation and id management."""

    def test_id_assigned(self):
        """Test that a given id is assigned correctly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        """Test that id auto-increments when not provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_explicit(self):
        """Test passing None explicitly still auto-increments."""
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_none(self):
        """Test to_json_string with None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with a valid list of dicts."""
        list_input = [{"id": 1}]
        output = Base.to_json_string(list_input)
        self.assertEqual(output, '[{"id": 1}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string returns []."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_string = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(json_string), [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
