#!/usr/bin/python3
"""
Module fot the function print_all
"""
from sys import stdin


def print_all(size, codes):
    """
    Function that prints all, duh!

    Args:
        size (int): size of file
        codes (dict): codes dictionnary
    """

size = 0
count = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
try:
    for line in stdin:
        lines = line.split()
        try:
            size += int(lines[-1])
        except (IndexError, ValueError):
            pass
        try:
            for key in codes:
                if key == lines[-2]:
                    codes[key] += 1
        except IndexError:
            pass
        count += 1
        if count == 10:
            print("File size: {}".format(size))
            for key in codes:
                if codes[key] != 0:
                    print("{}: {}".format(key, codes[key]))
            count = 0
except KeyboardInterrupt:
    print("File size: {}".format(size))
    for key in codes:
        if codes[key] != 0:
            print("{}: {}".format(key, codes[key]))
    raise
