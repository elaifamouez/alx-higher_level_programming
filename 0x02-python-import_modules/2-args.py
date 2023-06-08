#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    if size > 2:
        print("{:d} arguments:".format(size - 1))
    elif size == 1:
        print("0 arguments.")
    else:
        print("1 argument:")
    for i in range(1, size):
        print("{:d}: {:s}".format(i, argv[i]))
