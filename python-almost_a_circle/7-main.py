#!/usr/bin/python3
"""Test Rectangle positional update."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)
    for args in ((89,), (89, 2), (89, 2, 3), (89, 2, 3, 4),
                 (89, 2, 3, 4, 5)):
        r1.update(*args)
        print(r1)
