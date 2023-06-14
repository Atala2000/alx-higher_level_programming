#!/usr/bin/python3
"""Module contains function
rep
"""
import json


def save_to_json_file(my_obj, filename):
    """Function for JSON

    Args:
        my_obj: object
        filename: file

    Raises:
        Exception: unencoded object

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
