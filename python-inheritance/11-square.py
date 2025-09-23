#!/usr/bin/python3
"""
This is the "9-rectangle" class module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Subclass of Rectangle class """
    def __init__(self, size):
        """
        Initialisation of a new Square instance
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the area of the Square """
        return (self.__size * self.__size)

    def __str__(self):
        """ Returns a str representation of the square """
        return (f"[Square] {self.__size}/{self.__size}")
