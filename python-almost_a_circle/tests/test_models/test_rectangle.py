#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class behavior."""

    def tearDown(self):
        """Remove any Rectangle.json file created during tests."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

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

    def test_width_str(self):
        """Rectangle("1", 2) raises TypeError for width."""
        with self.assertRaises(TypeError) as e:
            Rectangle("1", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_float(self):
        """Rectangle(1.5, 2) raises TypeError for width."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_width_none(self):
        """Rectangle(None, 2) raises TypeError for width."""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_width_zero(self):
        """Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_negative(self):
        """Rectangle(-10, 2) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_str(self):
        """Rectangle(1, "2") raises TypeError for height."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_zero(self):
        """Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_negative(self):
        """Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_str(self):
        """Rectangle(1, 2, "3") raises TypeError for x."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "3")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_dict(self):
        """Rectangle(1, 2, {}) raises TypeError for x."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {})

    def test_x_negative(self):
        """Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_str(self):
        """Rectangle(1, 2, 3, "4") raises TypeError for y."""
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_negative(self):
        """Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area_exists(self):
        """Test area() method exists and is callable."""
        r = Rectangle(3, 2)
        self.assertTrue(callable(r.area))

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area with different dimensions."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str_exists(self):
        """Test __str__ produces a string."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertIsInstance(str(r), str)

    def test_str(self):
        """Test the __str__ method output format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_exists(self):
        """Test display() method exists and is callable."""
        r = Rectangle(2, 2)
        self.assertTrue(callable(r.display))

    def test_display_no_x_y(self):
        """Test display() with default x=0, y=0."""
        r = Rectangle(2, 3)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n##\n")

    def test_display_no_y(self):
        """Test display() with x given, y default 0."""
        r = Rectangle(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_display_full(self):
        """Test display() with both x and y given."""
        r = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_update_args_none(self):
        """Test update() with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_args_1(self):
        """Test update() with 1 argument (id)."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_2(self):
        """Test update() with 2 arguments (id, width)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_args_3(self):
        """Test update() with 3 arguments (id, width, height)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_args_4(self):
        """Test update() with 4 arguments (id, width, height, x)."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args_5(self):
        """Test update() with all 5 arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs_height(self):
        """Test update() with height kwarg only."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_kwargs_width_x(self):
        """Test update() with width and x kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/10")

    def test_update_kwargs_all(self):
        """Test update() with all kwargs, order independent."""
        r = Rectangle(10, 10, 10, 10, 99)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_update_kwargs_full_set(self):
        """Test update() with x, height, y, width kwargs."""
        r = Rectangle(10, 10, 10, 10, 99)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (99) 1/3 - 4/2")

    def test_to_dictionary_exists(self):
        """Test to_dictionary() exists and returns a dict."""
        r = Rectangle(10, 2, 1, 9)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_values(self):
        """Test to_dictionary() returns correct values."""
        r = Rectangle(10, 2, 1, 9, 55)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 55, "width": 10,
                             "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_roundtrip(self):
        """Test to_dictionary() output can rebuild an equal Rectangle."""
        r1 = Rectangle(10, 2, 1, 9, 44)
        d = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(str(r1), str(r2))

    def test_save_to_file_exists(self):
        """Test save_to_file() creates a file."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """Test save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_content(self):
        """Test save_to_file() writes correct JSON content."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 10', content)
        self.assertIn('"width": 2', content)

    def test_load_from_file_no_file(self):
        """Test load_from_file() returns [] when file doesn't exist."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_roundtrip(self):
        """Test load_from_file() rebuilds saved Rectangles correctly."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 2)
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))


if __name__ == "__main__":
    unittest.main()
