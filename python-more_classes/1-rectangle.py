#!/usr/bin/python3
"""
This is the "1-rectangle" class module.
"""


class Rectangle:
    """
    Rectangle with width and height attr
    """
    def __init__(self, width=0, height=0):
        """
        Initialisation of a new instance from class Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError if width is not an int
            ValueError if width is a negative int
            TypeError if height is not an int
            ValueError if height is a neg int
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ Getter for with """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
