#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
fl = dir(hidden_4)
ll = len(fl)
for x in range(0, ll):
    if fl[x][0:2] != "__":
        print(fl[x])
