#!/usr/bin/python3
"""Definiton of a base class"""


class Base:
    """This is the base model
    Attributes:
        __nb_objects (int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """New base

        Args:
            id (int): Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
