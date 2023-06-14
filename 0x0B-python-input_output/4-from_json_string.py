#!/usr/bin/python3
"""Module contains function
rep
"""
import json


def from_json_string(my_str):
    """Function for JSON

    Args:
        my_str: object

    Raises:
        Exception: unencoded object

    """
    return json.loads(my_str)
