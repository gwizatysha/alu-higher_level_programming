#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import io
import sys
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Tests for Square class behavior."""

    def tearDown(self):
        """Remove any Square.json file created during tests."""
        try:
            os.remove("Square.json")
        except IOError:
            pass

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

    def test_id_passed(self):
        """Test id passed explicitly."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.id, 12)

    def test_size_str(self):
        """Square("1") raises TypeError."""
        with self.assertRaises(TypeError) as e:
            Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_zero(self):
        """Square(0) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_size_negative(self):
        """Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_str(self):
        """Square(1, "2") raises TypeError for x."""
        with self.assertRaises(TypeError) as e:
            Square(1, "2")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_negative(self):
        """Square(1, -2) raises ValueError for x."""
        with self.assertRaises(ValueError) as e:
            Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_str(self):
        """Square(1, 2, "3") raises TypeError for y."""
        with self.assertRaises(TypeError) as e:
            Square(1, 2, "3")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_negative(self):
        """Square(1, 2, -3) raises ValueError for y."""
        with self.assertRaises(ValueError) as e:
            Square(1, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area_exists(self):
        """Test area() exists and is callable."""
        s = Square(5)
        self.assertTrue(callable(s.area))

    def test_area(self):
        """Test the area method for a square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str_exists(self):
        """Test __str__ produces a string."""
        s = Square(3, 1, 3, 12)
        self.assertIsInstance(str(s), str)

    def test_str(self):
        """Test the __str__ method output format."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(str(s), "[Square] (12) 1/3 - 3")

    def test_display_exists(self):
        """Test display() exists and is callable."""
        s = Square(5)
        self.assertTrue(callable(s.display))

    def test_display_no_x_y(self):
        """Test display() with default x=0, y=0."""
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_x_y(self):
        """Test display() with x and y both given."""
        s = Square(3, 1, 3)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n\n ###\n ###\n ###\n")

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

    def test_size_setter_invalid_value(self):
        """Test size setter raises ValueError for non-positive value."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

    def test_update_args_1(self):
        """Test update() with 1 argument (id)."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_args_2(self):
        """Test update() with 2 arguments (id, size)."""
        s = Square(5, id=1)
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_update_args_3(self):
        """Test update() with 3 arguments (id, size, x)."""
        s = Square(5, id=1)
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")

    def test_update_args_4(self):
        """Test update() with all 4 arguments."""
        s = Square(5, id=1)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs_x(self):
        """Test update() with x kwarg only."""
        s = Square(5, id=1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")

    def test_update_kwargs_size_y(self):
        """Test update() with size and y kwargs."""
        s = Square(5, id=1)
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 0/1 - 7")

    def test_update_kwargs_all(self):
        """Test update() with all kwargs."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary_exists(self):
        """Test to_dictionary() exists and returns a dict."""
        s = Square(10, 2, 1)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_values(self):
        """Test to_dictionary() returns correct values."""
        s = Square(10, 2, 1, 77)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 77, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_roundtrip(self):
        """Test to_dictionary() output can rebuild an equal Square."""
        s1 = Square(10, 2, 1, 66)
        d = s1.to_dictionary()
        s2 = Square(1)
        s2.update(**d)
        self.assertEqual(str(s1), str(s2))

    def test_save_to_file_exists(self):
        """Test save_to_file() creates a Square.json file."""
        s = Square(5)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_none(self):
        """Test save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_no_file(self):
        """Test load_from_file() returns [] when file doesn't exist."""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_roundtrip(self):
        """Test load_from_file() rebuilds saved Squares correctly."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(str(squares[0]), str(s1))
        self.assertEqual(str(squares[1]), str(s2))

    def test_inherits_rectangle(self):
        """Test that Square is a subclass of Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)


if __name__ == "__main__":
    unittest.main()
