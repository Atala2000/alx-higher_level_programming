#!/usr/bin/python3
"""
sbclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep of square"""
    def __init__(self, size):
        """inst of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """sqare area"""
        return self.__size ** 2
