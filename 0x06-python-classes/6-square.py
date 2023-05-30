#!/usr/bin/python3
"""Square mod"""

class Square():
    """Square def"""

    def __init__(self, size=0, position=(0, 0)):
        """Square object

        Args:
            size (int): Size of edge
            position (tuple): square corrd
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Square pos"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1])is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Current square"""
        return self.__size ** 2

    def my_print(self):
        """Returns square"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
