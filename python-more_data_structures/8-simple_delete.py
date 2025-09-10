#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    # delete key if it exits, otherwise return None without raising an error
    return a_dictionary
