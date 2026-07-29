#!/usr/bin/python3
"""This module defines a Square class with size validation."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
