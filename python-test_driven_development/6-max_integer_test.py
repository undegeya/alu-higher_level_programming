#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function."""

    def test_positive_numbers(self):
        """Test maximum value from positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test maximum value from an unsorted list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_numbers(self):
        """Test maximum value from negative integers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_one_element(self):
        """Test a list containing one element."""
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_large_number(self):
        """Test maximum value with large integers."""
        self.assertEqual(max_integer([1000, 5000, 2000]), 5000)
