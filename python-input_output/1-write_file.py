#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a str into text file
    and returns num of char
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
