"""
This is the "task_03_countediterator.py" class module.
"""


class CountedIterator:
    def __init__(self, iterable):
        """ Initialise with an iterable and counter set to 0 """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """ Return iterator obj itself """
        return self

    def __next__(self):
        """ Fetch next item and increment counter """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """ Return the num of times fetched """
        return self.count
