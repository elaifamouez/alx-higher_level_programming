#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys


def print_stats(total_size, status_counts):
    """prints the stats"""
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_counts.items()):
        print("{}: {:d}".format(key, value))
    sys.stdout.flush()


total_size = 0
valid_status = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {}
count = 0
try:  # read lines from stdin
    for line in sys.stdin:
        # Process the line here
        if count == 10:
            print_stats(total_size, status_counts)
            count = 1
        else:
            count += 1
        items = line.rstrip().split()  # remove newline character and split
        try:
            total_size += int(items[-1])
        except (ValueError, IndexError):
            pass
        try:
            status = items[-2]
            if status in valid_status:
                if status in status_counts:
                    status_counts[status] += 1
                else:
                    status_counts[status] = 1
        except IndexError:
            pass
    print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
