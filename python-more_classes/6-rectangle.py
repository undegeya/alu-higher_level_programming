#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""

        for row in range(self.__height):
            rectangle += "#" * self.__width

            if row != self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(
            self.__width,
            self.__height
        )

    def __del__(self):
        """Delete a rectangle instance."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
