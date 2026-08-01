#!/usr/bin/python3
"""Module defining serializable Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes student information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of student."""
        if isinstance(attrs, list):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }

        return self.__dict__

    def reload_from_json(self, json):
        """Replaces student attributes using dictionary data."""
        for key, value in json.items():
            setattr(self, key, value)
