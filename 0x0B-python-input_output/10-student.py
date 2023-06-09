#!/usr/bin/python3
"""Module def student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Method to init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns descr"""
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for x in range(len(attrs)):
                for y in obj:
                    if attrs[x] == y:
                        d_list[y] = obj[y]
            return d_list

        return obj
                
