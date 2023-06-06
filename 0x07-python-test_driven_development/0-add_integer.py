#!/usr/bin/python3
"""

"0-add_integer" module.
0-add_integer module uses a function that us ass_integer(a, b)
"""


def add_integer(a, b=98):
    """Returns a value equal to the sum of two integers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
