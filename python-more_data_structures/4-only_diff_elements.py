#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first = set_1.difference(set_2)
    second = set_2.difference(set_1)
    final = first | second
    return final
