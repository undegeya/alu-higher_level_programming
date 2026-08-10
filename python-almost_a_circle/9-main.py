#!/usr/bin/python3
"""Test Square construction and inherited behavior."""
from models.square import Square

if __name__ == "__main__":
    for square in (Square(5), Square(2, 2), Square(3, 1, 3)):
        print(square)
        print(square.area())
        square.display()
        if square.x == 0 and square.y == 0:
            print("---")

