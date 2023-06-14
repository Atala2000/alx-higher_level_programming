#!/usr/bin/python3
"""
Contain BaseGeom
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep of a rectangle"""
    def __init__(self, width, height):
        """instance of rec"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
