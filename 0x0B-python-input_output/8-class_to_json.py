#!/usr/bin/python3
"""Module returns dictionary
"""


def class_to_json(obj):
    """ Return dict descr"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
