#!/usr/bin/python3
"""
This is the "8-class_to_json.py" module.
"""


def class_to_json(obj):
    """
    function that returns dict description
    for json serialization
    """
    return obj.__dict__
