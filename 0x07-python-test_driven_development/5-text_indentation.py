#!/usr/bin/python3
"""
"5-test_indentation" module
5=text-indentatin module has one function, text_indentation(text)
"""


def text_indentation(text):
    """splits a text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if a == ' ':
            continue
        else:
             flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                 print(a, end="")
