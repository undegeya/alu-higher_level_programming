#!/usr/bin/python3
"""This module prints a square using the # character."""


def print_square(size):
    """Prints a square of a given size using # characters.

    Args:
        size (int): The size of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
