#!/usr/bin/python3
"""
Rectangle class that inherits from Base class
"""
from models.base import Base


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

    @property
    def width(self):
        """
            function getter
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
           setter function
           Args:
                value (int): set value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            function getter
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
           setter function
           Args:
                value (int): set value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            function getter
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
           setter function
           Args:
                value (int): set x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property        
    def y(self):
        """
            function getter
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
           setter function
           Args:
                value (int): set y
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")

        self.__y = value

    def area(self):
        """
            returns area of rectangle
        """
        return (self.__height * self.__height)

    def display(self):
        """
            return area
        """
        rectangle = "#"
        print_symbol = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            return a string representation
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            assigns values to attributes
            Args:
                *args: variable
                **kwargs - kwrgs
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            return dict
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"), 'id': getattr(self, "id"), 'height': getattr(self, "height"), 'width': getattr(self, "width")}