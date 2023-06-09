#!/usr/bin/python3
"""
"4-print_square" module.
4-print_square module uses one function,print_square(size)
"""


def print_square(size):
    """prints a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
