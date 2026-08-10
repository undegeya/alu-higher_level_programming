#!/usr/bin/python3
"""This module prints text with indentation after special characters."""


def text_indentation(text):
    """Prints a text with two new lines after ., ? and : characters.

    Args:
        text (str): The text to format.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == " ":
            continue

        skip_space = False
        result += char

        if char in ".?:":
            print(result.strip())
            print()
            result = ""
            skip_space = True

    if result.strip():
        print(result.strip(), end="")
