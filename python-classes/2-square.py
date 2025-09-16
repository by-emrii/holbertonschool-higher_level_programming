#!/usr/bin/python3
"""
This is the "2-square.py" class module.
"""


class Square:
    """
    Initialisation of a new instance from class Square
    with size private attribute.
    Raise TypeError if instance is not an int
    Raise ValueError if size is a negative int

    Args:
        size (int): size of the square
    """

    def __init__(self, size=0):

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
