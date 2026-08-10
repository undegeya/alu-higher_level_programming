#!/usr/bin/python3
"""Test the Rectangle class and all required behavior."""

import unittest
from io import StringIO
from contextlib import redirect_stdout

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle construction, validation, display, and updates."""

    def test_constructor_and_properties(self):
        """Test constructor values and public properties."""
        rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(rect.id, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.area(), 20)

    def test_width_validation(self):
        """Test validation of width values."""
        rect = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.width = "1"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.width = 0

    def test_height_validation(self):
        """Test validation of height values."""
        rect = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.height = "1"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.height = 0

    def test_x_validation(self):
        """Test validation of the x position."""
        rect = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.x = {}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.x = -1

    def test_y_validation(self):
        """Test validation of the y position."""
        rect = Rectangle(1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.y = []
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.y = -1

    def test_display(self):
        """Test display output with x and y offsets."""
        rect = Rectangle(2, 3, 2, 1)
        output = StringIO()
        with redirect_stdout(output):
            rect.display()
        self.assertEqual(output.getvalue(), "\n  ##\n  ##\n  ##\n")

    def test_string(self):
        """Test the required Rectangle string representation."""
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test positional Rectangle updates in the required order."""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test keyword Rectangle updates and positional precedence."""
        rect = Rectangle(10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(rect.height, 1)
        rect.update(width=4, x=3, y=2, id=89)
        self.assertEqual(str(rect), "[Rectangle] (89) 3/2 - 4/1")
        rect.update(7, width=99)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 4)

    def test_to_dictionary(self):
        """Test Rectangle dictionary representation."""
        rect = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(
            rect.to_dictionary(),
            {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        )


if __name__ == "__main__":
    unittest.main()

