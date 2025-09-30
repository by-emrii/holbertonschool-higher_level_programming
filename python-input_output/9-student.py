#!/usr/bin/python3
"""
This is the "9-student.py" module.
"""


class Student:
    """
    Student class with attributes: first name, last name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return dict rep of a student instance
        """
        return self.__dict__
