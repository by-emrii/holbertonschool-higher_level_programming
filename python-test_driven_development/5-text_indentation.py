#!/usr/bin/python3
"""
This is the "text_indentation" module.

The text_indentation module supplies one function, text_indentation().
For example,

text = "Hi. What's ur name?"
>>> text_indentation(text)
Hello.

What's ur name?
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""  # init empty string to add char to
    for char in text:
        string += char
        if char in ".?:":
            print(string.strip(), end="\n\n")
            string = ""

    if string:
        print(string.strip(), end="")
