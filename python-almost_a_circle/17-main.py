#!/usr/bin/python3
"""Test dictionary to instance conversion."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(3, 5, 1)
    r2 = Rectangle.create(**r1.to_dictionary())
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

