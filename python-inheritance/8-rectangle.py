#!/usr/bin/python3
"""
This is the "8-rectangle" class module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry class """
    def __init__(self, width, height):
        """
        Initialisation of a new Rectangle instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
