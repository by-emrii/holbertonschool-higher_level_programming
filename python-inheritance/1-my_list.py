#!/usr/bin/python3
"""
This is the "1-my_list" module.
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """ Prints the list, sorted in asc order """
        print(sorted(self))
