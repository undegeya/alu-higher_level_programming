#!/usr/bin/python3
"""Test JSON persistence."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])
    with open("Rectangle.json", "r", encoding="utf-8") as file:
        print(file.read())
