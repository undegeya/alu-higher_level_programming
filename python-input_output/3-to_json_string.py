#!/usr/bin/python3
"""Module converting Python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """Returns JSON representation of an object."""
    return json.dumps(my_obj)
