#!/usr/bin/python3
"""
_is_kind_of_class funct
"""


class BaseGeometry:
    """class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation of value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".fornat(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rep of a rectangle"""
    def __init__(self, width, height):
        """instance of rec"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """string rep of rec"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
