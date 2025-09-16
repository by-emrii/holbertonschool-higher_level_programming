#!/usr/bin/python3
"""
This is the "1-square.py" class module.
"""


class Square:
    """
    Initialisation of a new instance from class Square
    with size private attribute

    Args:
        size (int): size of the square
    """

    def __init__(self, size):
        self.__size = size
