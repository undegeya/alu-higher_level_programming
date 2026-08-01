#!/usr/bin/python3
"""Module converting class objects to dictionaries."""


def class_to_json(obj):
    """Returns dictionary description of an object."""
    return obj.__dict__
