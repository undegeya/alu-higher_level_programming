#!/usr/bin/python3
"""Module defining filtered Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns selected attributes as dictionary."""
        if isinstance(attrs, list):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }

        return self.__dict__
