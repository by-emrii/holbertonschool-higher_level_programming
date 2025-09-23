#!/usr/bin/python3
"""
This is the "2-is_same_class" module.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of
    the specified class ; otherwise False.
    """
    return type(obj) is a_class
