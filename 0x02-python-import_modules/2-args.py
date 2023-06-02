#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
pl = (len(argv))
if pl == 2:
    print(f"{(pl - 1):d} argument:")
    print(f"{(pl - 1):d}: {argv[1]}")
elif pl == 1:
    print(f"{(pl - 1):d} arguments.")
else:
    print(f"{(pl - 1):d} arguments:")
    for x in range(1, pl):
        print(f"{x:d}: {argv[x]}")
