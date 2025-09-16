#!/usr/bin/python3
"""
This is the "5-square.py" class module.
"""


class Square:
    """
    Square with private size attr
    """
    def __init__(self, size=0):
        """
        Initialisation of a new instance from class Square

        Args:
            size (int): size of the square

        Raises:
            TypeError if instance is not an int
            ValueError if size is a negative int
        """

        # check for errors first, then initialise
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        prints in stdout the square with '#'
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
