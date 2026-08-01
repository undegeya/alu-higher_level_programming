#!/usr/bin/python3
"""Module generating Pascal's triangle."""


def pascal_triangle(n):
    """Returns Pascal's triangle containing n rows."""
    if n <= 0:
        return []

    triangle = []

    for row_number in range(n):
        row = [1]

        if triangle:
            previous = triangle[-1]

            for index in range(len(previous) - 1):
                row.append(previous[index] + previous[index + 1])

            row.append(1)

        triangle.append(row)

    return triangle
