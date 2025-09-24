#!/usr/bin/python3
"""
This is the "task_02_verboselist.py" class module.
"""


class VerboseList(list):
    """ VerboseList subclass from list superclass"""
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        item_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{item_count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
