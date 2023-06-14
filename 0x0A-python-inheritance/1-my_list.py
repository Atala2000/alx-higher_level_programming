#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """init n obj"""
        super().__init__()

    def print_sorted(self):
        """prints list"""
        print(sorted(self))
