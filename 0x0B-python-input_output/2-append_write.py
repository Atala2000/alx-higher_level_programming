#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Function

    Args:
        filename: filename
        text : text

    Raises
        Exception when file unopenable

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
