#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum1 = []
    for x in argv:
        if x.lstrip("-").isdigit():
            sum1.append(int(x))
    print(sum(sum1))
