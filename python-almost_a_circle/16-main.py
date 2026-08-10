#!/usr/bin/python3
"""Test JSON string to dictionary conversion."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    values = [{"id": 89, "width": 10, "height": 4},
              {"id": 7, "width": 1, "height": 7}]
    encoded = Rectangle.to_json_string(values)
    print("[{}] {}".format(type(values), values))
    print("[{}] {}".format(type(encoded), encoded))
    print("[{}] {}".format(type(Rectangle.from_json_string(encoded)),
                             Rectangle.from_json_string(encoded)))
