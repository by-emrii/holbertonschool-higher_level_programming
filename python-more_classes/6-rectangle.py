#!/usr/bin/python3
"""
This is the "6-rectangle" class module.
"""


class Rectangle:
    """
    Rectangle with width and height attr
    """
    number_of_instances = 0

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
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        # increment when instance/obj is created
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

    def __str__(self):
        """ Returns a str representation of the rect using # """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = '#' * self.__width
        rectangle = "\n".join([row for _ in range(self.__height)])
        return rectangle

    def __repr__(self):
        """
        Return official str representation of rect that
        can be used to recreate an instance using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Delete instance """
        # decrement when an instance is deleted
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
