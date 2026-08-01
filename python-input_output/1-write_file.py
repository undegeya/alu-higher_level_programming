#!/usr/bin/python3
"""Module for writing files."""


def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
