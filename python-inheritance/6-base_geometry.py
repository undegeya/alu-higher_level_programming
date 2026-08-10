#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """Represent the base class for geometry."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
