#!/usr/bin/python3
"""
Rectangle class that inherits from Base class
"""


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
