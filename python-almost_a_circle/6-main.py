#!/usr/bin/python3
"""Test Rectangle display with offsets."""
from models.rectangle import Rectangle

if __name__ == "__main__":
    Rectangle(2, 3, 2, 2).display()
    print("---")
    Rectangle(3, 2, 1, 0).display()
