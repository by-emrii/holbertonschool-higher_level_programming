#!/usr/bin/python3
"""
This is the "task_00_abc.py" class module.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """ Animal abstract Class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """ Dog Subclass of Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """ Cat subclass of Animal"""
    def sound(self):
        return "Meow"
