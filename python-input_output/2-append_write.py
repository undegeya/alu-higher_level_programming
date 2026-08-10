#!/usr/bin/python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Appends text to a file and returns characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
