#!/usr/bin/python3
"""
This is the "task_01_duck_typing.py" class module.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ Shape Abstract Class """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ Circle subclass of Shape """
    def __init__(self, radius):
        """
        Initialisation of Circle instance

        Args:
        radius (int): radius of circle
        """
        self.radius = radius

    def area(self):
        return (math.pi * (self.radius ** 2))

    def perimeter(self):
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """ Rectangle subclass of Shape """
    def __init__(self, width, height):
        """
        Initialisation of Rectangle instance

        Args:
        width (int): width of rect
        height (int): height of rect
        """
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return ((self.width * 2) + (self.height * 2))


def shape_info(arg1):
    print(f"Area: {arg1.area()}")
    print(f"Perimeter: {arg1.perimeter()}")
