#!/usr/bin/python3
"""Class define"""


class Square:
    """Square rep
    Attributes:
        __size (int): square size
    """
    def __init__(self, size=0):
        """square init
        Args:
            size (int): square size
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Area calculation
        Returns:
            Area of square
        """
        return (self.__size) ** 2
