#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """Test with a list in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list in random order"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test with a list in descending order"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test with no argument passed (default empty list)"""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)

    def test_mixed_positive_negative(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 3, -5, 2]), 3)

    def test_duplicate_max(self):
        """Test with the max value appearing more than once"""
        self.assertEqual(max_integer([4, 2, 4, 1]), 4)


if __name__ == "__main__":
    unittest.main()
