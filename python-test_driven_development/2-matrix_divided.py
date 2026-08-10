#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): List of lists of integers/floats.
        div (int or float): Divisor.

    Returns:
        list: A new matrix with divided values rounded to 2 decimals.

    Raises:
        TypeError: If matrix or div is invalid.
        ZeroDivisionError: If div is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(error)

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
