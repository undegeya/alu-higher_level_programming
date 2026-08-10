#!/usr/bin/python3
"""Test Square update."""
from models.square import Square

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    for args in ((10,), (1, 2), (1, 2, 3), (1, 2, 3, 4)):
        s1.update(*args)
        print(s1)
    s1.update(x=12)
    print(s1)
    s1.update(size=7, y=1)
    print(s1)
    s1.update(size=7, id=89, y=1)
    print(s1)

