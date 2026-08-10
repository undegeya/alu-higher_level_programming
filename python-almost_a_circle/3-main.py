#!/usr/bin/python3
"""Test Rectangle area."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    print(Rectangle(3, 2).area())
    print(Rectangle(2, 10).area())
    print(Rectangle(8, 7, 0, 0, 12).area())

