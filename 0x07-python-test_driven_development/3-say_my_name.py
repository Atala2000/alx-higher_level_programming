#!/usr/bin/python3
"""
"3-say_my_name_" module.
3-say_my_name module uses one function, say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Prints my name is followed by the names"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
