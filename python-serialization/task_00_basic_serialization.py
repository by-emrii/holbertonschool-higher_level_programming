#!/usr/bin/env python3
"""
This is the "task_00_basic_serialization.py" module.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the python dict (data) to JSON and save it to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a json file and deserializes it back to a
    data struct (dict)
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
