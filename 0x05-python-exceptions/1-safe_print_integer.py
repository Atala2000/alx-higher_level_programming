#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if type(value) is int:
            print("{}".format(value))
            return True
        else:
            return False
    except Exception as e:
        return e
