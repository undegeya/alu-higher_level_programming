#!/usr/bin/python3
"""This module defines a Square class with size property."""


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
