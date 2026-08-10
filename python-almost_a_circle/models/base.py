#!/usr/bin/python3
"""Provide the Base class used by all shape models."""

import json


class Base:
    """Represent the base model and manage unique object identifiers."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a supplied or generated id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON string representing a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save object dictionaries as JSON in a class-named file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_dictionaries = []
        else:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance initialized from a dictionary of values."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load and return instances from the class-named JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        dictionaries = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in dictionaries]
