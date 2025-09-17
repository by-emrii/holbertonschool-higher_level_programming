#!/usr/bin/python3
"""
This is the "7-rectangle" class module.
"""


class Rectangle:
    """
    Rectangle with width and height attr
    """
    number_of_instances = 0
    print_symbol = '#'

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
        """ Returns a str representation of the rect using print_symbol att """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = str(self.print_symbol) * self.__width
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the rectangle with biggest area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = Rectangle.area(rect_1)
        area_2 = Rectangle.area(rect_2)
        if area_1 > area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2
        elif area_1 == area_2:
            return rect_1
