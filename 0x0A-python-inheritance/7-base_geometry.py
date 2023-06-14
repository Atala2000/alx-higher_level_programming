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
