#!/usr/bin/python3
"""This module defines a Square class that can print itself."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
