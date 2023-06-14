#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """Function

    Args:
        filename: filename
        text : text

    Raises
        Exception when file unopenable

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
