#!/usr/bin/python3
"""
This is the "0-lookup" module.
"""


def lookup(obj):
    """ Returns the list of available atts and methods of an obj """
    return dir(obj)
