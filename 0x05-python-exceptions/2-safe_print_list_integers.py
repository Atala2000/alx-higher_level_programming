#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    intp = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            intp += 1
        except (ValueError, TypeError):
            continue
    print()
    return intp
