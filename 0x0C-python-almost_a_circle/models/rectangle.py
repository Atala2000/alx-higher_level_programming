#!/usr/bin/python3
"""
Rectangle class that inherits from Base class
"""


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


class Rectangle(Base):
    """
        REctangle class that inherits from BAse
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            INIT A CLASS INSTANCE
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
