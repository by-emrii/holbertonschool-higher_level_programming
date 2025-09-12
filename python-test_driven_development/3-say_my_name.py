#!/usr/bin/python3
"""
This is the "say_my_name" module.

The say_my_name module supplies one function, say_my_name().
For example,

>>> say_my_name("John", "Smith")
My name is John Smith$
"""


def say_my_name(first_name, last_name=""):
    """
    Return a string of first and last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
