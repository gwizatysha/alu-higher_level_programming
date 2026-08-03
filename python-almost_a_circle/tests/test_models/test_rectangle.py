#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class behavior."""

    def test_width_height_default(self):
        """Test default x, y and auto id."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id_passed(self):
        """Test id passed explicitly."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_not_int(self):
        """Test TypeError when width is not an integer."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_negative(self):
        """Test ValueError when width <= 0."""
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_zero(self):
        """Test ValueError when width == 0."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_x_not_int(self):
        """Test TypeError when x is not an integer."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, {})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_negative(self):
        """Test ValueError when y < 0."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with different dimensions."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with *args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_full(self):
        """Test update with all *args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 99)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (99) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test to_dictionary returns correct dict."""
        r = Rectangle(10, 2, 1, 9, 55)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 55, "width": 10,
                             "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        """Test to_dictionary returns a dict type."""
        r = Rectangle(10, 2, 1, 9)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
