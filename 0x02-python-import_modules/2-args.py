#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
pl = (len(argv))
print(f"{(pl - 1):d} arguments")
for x in range(1, pl):
    print(f"{x:d} : {argv[x]}")
