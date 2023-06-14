#!/usr/bin/python3
"""Module contains function
rep
"""
import json


def to_json_string(my_obj):
    """Function for JSON

    Args:
        my_obj: object

    Raises:
        Exception: unencoded object

    """
    return json.dumps(my_obj)
