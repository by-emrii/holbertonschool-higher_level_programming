#!/usr/bin/python3
"""
This is the "11-student.py" module.
"""


class Student:
    """
    Student class with attributes: first name, last name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dict rep of a student instance.
        If attrs is a list of strings, only return those keys if they exist
        """
        if attrs is None:
            return self.__dict__

        filtered = {}
        for attr in attrs:
            if hasattr(self, attr):  # check if obj has that attr
                # get value of the attr by name
                filtered[attr] = getattr(self, attr)
        return filtered

    def reload_from_json(self, json):
        """
        Replaces/Updates all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
