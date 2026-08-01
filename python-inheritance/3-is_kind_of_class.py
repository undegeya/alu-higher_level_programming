#!/usr/bin/python3
"""This module defines a function that checks whether an object
is an instance of a class or one of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if isinstance(obj, a_class), otherwise False.
    """
    return isinstance(obj, a_class)
