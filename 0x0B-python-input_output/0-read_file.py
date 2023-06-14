#!/usr/bin/python3
"""Module that has a function"""


def read_file(filename=""):
    """Function

    Args:
        filename: filename

    Raises
        Exception when file unopenable

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
