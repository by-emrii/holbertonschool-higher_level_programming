#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    returns json rep of an obj
    """
    json_string = json.dumps(my_obj)
    return json_string
