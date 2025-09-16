#!/usr/bin/python3
"""
This is the "6-square.py" class module.
"""


class Square:
    """
    Square with private size attr
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialisation of a new instance from class Square

        Args:
            size (int): size of the square
            position (tuple): the position of the square

        Raises:
            TypeError if instance is not an int
            ValueError if size is a negative int
            TypeError if position is not a tuple of pos int
        """

        # check for errors first, then initialise
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(num, int) and
                    num >= 0 for num in position)):
            raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size with validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for position with validation """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and
                    num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        Prints in stdout the square with '#'
        considering the position
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
