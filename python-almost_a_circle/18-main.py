#!/usr/bin/python3
"""Test loading instances from JSON files."""
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    rectangles = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
    Rectangle.save_to_file(rectangles)
    for rect in Rectangle.load_from_file():
        print(rect)

    squares = [Square(5), Square(7, 9, 1)]
    Square.save_to_file(squares)
    for square in Square.load_from_file():
        print(square)

