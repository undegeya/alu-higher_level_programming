#!/usr/bin/python3
"""Test Rectangle attribute validation."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    tests = [
        lambda: Rectangle(10, "2"),
        lambda: setattr(Rectangle(10, 2), "width", -10),
        lambda: setattr(Rectangle(10, 2), "x", {}),
        lambda: Rectangle(10, 2, 3, -1),
    ]
    for test in tests:
        try:
            test()
        except Exception as error:
            print("[{}] {}".format(type(error).__name__, error))

