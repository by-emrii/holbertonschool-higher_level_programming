#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # use truthiness - true if the list if empty or use len()
    return (max(my_list))
