#!/usr/bin/python3
"""
_is_kind_of_class funct
"""


def inherits_from(obj, a_class):
    """True if obj is inst"""
    return (issubclass(type(obj, a_class) and type(obj) != a_class)
