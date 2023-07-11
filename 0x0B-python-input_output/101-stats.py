#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
from sys import stdin


def print_statistics(file_size, status_codes):
    """prints statistics"""
    print("File size: {}".format(file_size))
    for key in status_codes.keys():
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


def main():
    """Reads stdin and computes metrics"""

    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    num_lines = 0

    try:
        for line in stdin:
            splited_line = line.rstrip().split("HTTP/1.1\" ")
            scode_fsize = splited_line[-1].split(" ")

            status_codes[scode_fsize[0]] += 1
            file_size += int(scode_fsize[-1])

            num_lines += 1
            if num_lines >= 10:
                print_statistics(file_size, status_codes)
                num_lines = 0
    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)


main()
