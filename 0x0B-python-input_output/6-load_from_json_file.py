#!/usr/bin/python3
"""Module contains function
rep
"""
import json


def load_from_json_file(filename):
    """Function for JSON

    Args:
        filename: file

    Raises:
        Exception: unencoded object

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
