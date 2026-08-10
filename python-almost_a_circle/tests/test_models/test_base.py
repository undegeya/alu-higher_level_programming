#!/usr/bin/python3
"""Test the Base class and its serialization methods."""

import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test Base construction, JSON conversion, and file persistence."""

    def test_id_generation(self):
        """Test automatic and supplied identifiers."""
        first = Base()
        second = Base()
        supplied = Base(42)
        self.assertEqual(second.id, first.id + 1)
        self.assertEqual(supplied.id, 42)

    def test_to_json_string(self):
        """Test conversion of dictionaries to JSON strings."""
        data = [{"id": 1, "width": 2}]
        self.assertEqual(Base.to_json_string(data), json.dumps(data))
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test conversion of JSON strings to dictionaries."""
        data = [{"id": 1, "width": 2}]
        encoded = json.dumps(data)
        self.assertEqual(Base.from_json_string(encoded), data)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_save_and_load_rectangle(self):
        """Test saving and loading Rectangle instances."""
        filename = "Rectangle.json"
        try:
            r1 = Rectangle(4, 5, 1, 2, 10)
            r2 = Rectangle(2, 3, 4, 5, 11)
            Rectangle.save_to_file([r1, r2])
            loaded = Rectangle.load_from_file()
            self.assertEqual(len(loaded), 2)
            self.assertIsInstance(loaded[0], Rectangle)
            self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
            self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_none(self):
        """Test saving None as an empty JSON list."""
        filename = "Rectangle.json"
        try:
            Rectangle.save_to_file(None)
            with open(filename, "r", encoding="utf-8") as file:
                self.assertEqual(file.read(), "[]")
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_missing(self):
        """Test that a missing JSON file returns an empty list."""
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Square.load_from_file(), [])

    def test_create_rectangle(self):
        """Test creating a Rectangle from a dictionary."""
        data = {"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}
        obj = Rectangle.create(**data)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.to_dictionary(), data)

    def test_create_square(self):
        """Test creating a Square from a dictionary."""
        data = {"id": 89, "size": 4, "x": 1, "y": 2}
        obj = Square.create(**data)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.to_dictionary(), data)


if __name__ == "__main__":
    unittest.main()
