#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    length = len(file)
    for n in range(0, length):
        if file[n][0:2] != "__":
            print(file[n])
