#!/usr/bin/python3
"""
Function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    func that returns an obj from json str
    """
    python_obj = json.loads(my_str)
    return python_obj
