#!/usr/bin/python3
"""Provide the Square class, a specialized Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square using the validated Rectangle attributes."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square with equal width and height."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the formatted string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return the square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Validate and set both square dimensions to the given size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square attributes from positional or keyword arguments."""
        attributes = ("id", "size", "x", "y")
        if args:
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the square attributes as a new dictionary."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

