#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """String initializer"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Atttribute setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area is returned"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
