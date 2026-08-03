#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Tests for Square class behavior."""

    def test_size_assignment(self):
        """Test that size sets both width and height."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test default x and y values."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y_passed(self):
        """Test passing x and y explicitly."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_area(self):
        """Test the area method for a square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test the __str__ method."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(str(s), "[Square] (12) 1/3 - 3")

    def test_size_getter(self):
        """Test the size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid_type(self):
        """Test size setter raises TypeError for non-integer."""
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update_args(self):
        """Test update with *args for id, size, x, y."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with **kwargs."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary returns correct dict."""
        s = Square(10, 2, 1, 77)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 77, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict type."""
        s = Square(10, 2, 1)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_inherits_rectangle(self):
        """Test that Square is a subclass of Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)


if __name__ == "__main__":
    unittest.main()
