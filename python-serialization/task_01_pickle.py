#!/usr/bin/env python3
"""
This is the "task_01_pickle.py" module.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attr in a format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of obj and save to provided file
        using the pickle module
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of the CustomObject
        using pickle module
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
