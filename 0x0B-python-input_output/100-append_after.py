#!/usr/bin/python3
"""Module that exectutes"""


def append_after(filename="", search_string="", new_string=""):
    """Appends new line

    Args:
        filename: file
        search_string: string
        new_string: string

    """

    r_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            r_line += [line]
            if line.find(search_string) != -1:
                r_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(r_line))
