#!/usr/bin/python3
def safe_print_division(a, b):

    try:
        rsp = a / b
    except ZeroDivisionError:
        rsp = None
    finally:
        print("Inside result: {}".format(rsp))

    return rsp
