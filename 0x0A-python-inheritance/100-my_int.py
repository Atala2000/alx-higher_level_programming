#!/usr/bin/python3
"""
Contains class
"""


class MyInt(int):
    """integer"""
    def __new__(cls, *args, **kwargs):
        """create new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what"""
        return int(self) != other

    def __ne__(self, other):
        """que sera sera"""
        return int(self) == other
