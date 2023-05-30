#!/usr/bin/python3
"""Class definition"""

class Square:
    """Rep square
    Attributes:
        __size (int): Square size
    """
    def __init__(self, size=0):
        """square init
        Args:
            size (int): size of square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Area
        Returns:
            Square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """size
        Returns:
            Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size
        Args:
            value (int): square size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
