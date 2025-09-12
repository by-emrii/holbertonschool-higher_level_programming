#!/usr/bin/python3
"""
This is the "add_integer" module.

The add_integer module supplies one function, add_integer().  For example,

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    Return the sum of the two integers (a, b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        result = int(a) + int(b)
    except OverflowError:
        raise OverflowError("integer value too big")
    return result
