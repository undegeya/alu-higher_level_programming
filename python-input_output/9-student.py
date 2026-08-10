#!/usr/bin/python3
"""Module defining Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of student."""
        return self.__dict__
