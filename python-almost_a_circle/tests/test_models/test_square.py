#!/usr/bin/python3
"""Test the Square class and inherited Rectangle behavior."""

import unittest
from io import StringIO
from contextlib import redirect_stdout

from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Square construction, validation, display, and updates."""

    def test_constructor(self):
        """Test Square dimensions, position, and id."""
        square = Square(5, 2, 3, 12)
        self.assertEqual(square.id, 12)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_string_and_area(self):
        """Test Square string representation and inherited area."""
        square = Square(5, 2, 3, 12)
        self.assertEqual(str(square), "[Square] (12) 2/3 - 5")
        self.assertEqual(square.area(), 25)

    def test_size_property(self):
        """Test getting and setting size."""
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.size = "9"

    def test_size_validation(self):
        """Test inherited dimension validation through size."""
        square = Square(1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.size = 0

    def test_display(self):
        """Test Square display with inherited Rectangle behavior."""
        square = Square(2, 1, 2)
        output = StringIO()
        with redirect_stdout(output):
            square.display()
        self.assertEqual(output.getvalue(), "\n\n ##\n ##\n")

    def test_update_args(self):
        """Test Square positional updates in the required order."""
        square = Square(5)
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test Square keyword updates and positional precedence."""
        square = Square(5)
        square.update(size=7, y=1, id=89)
        self.assertEqual(str(square), "[Square] (89) 0/1 - 7")
        square.update(10, size=99)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)

    def test_to_dictionary(self):
        """Test Square dictionary representation."""
        square = Square(10, 2, 1, 1)
        self.assertEqual(
            square.to_dictionary(),
            {"id": 1, "size": 10, "x": 2, "y": 1}
        )


if __name__ == "__main__":
    unittest.main()
