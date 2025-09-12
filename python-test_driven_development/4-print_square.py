#!/usr/bin/python3
"""
This is the "print_square" module.

The print_square module supplies one function, print_square().
For example,

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Prints a square with '#' of the 'size'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        # _ when variable is not needed for loop
        print("#" * size)
