#!/usr/bin/python3
"""pascatl t"""


def pascal_triangle(n=4500):
    """pascal print"""
    pascal = [[0]*i for i in range(1, n+1)]
    ct = 0
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for y in range(0, i//2):
            pascal[i][y+1] = pascal[i-1][y] + pascal[i-1][y+1]
            pascal[i][i-y-1] = pascal[i-1][y] + pascal[i-1][y+1]
    return pascal
