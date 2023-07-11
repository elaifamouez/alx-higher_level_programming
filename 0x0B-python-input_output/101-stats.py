#!/usr/bin/python3
"""
Reads lines from stdin and prints status codes
and number of times status code occured after every 10 lines
"""

if __name__ == '__main__':
    import fileinput
    import sys

    def print_dict(status, size):
        """Prints a dictionary in sorted order"""
        print("File size: {}".format(size))
        status = dict(sorted(status.items()))
        for elem in status:
            print("{}: {}".format(elem, status[elem]))

    try:
        i = 0
        file_size = 0
        status_code = {}
        new_list = [200, 301, 400, 401, 403, 404, 405, 500]
        for line in fileinput.input():
            if i % 10 == 0 and i != 0:
                print_dict(status_code, file_size)
            line = line.split()
            if len(line) < 2:
                continue
            tmp = line[-2]
            if ord(tmp[0]) not in list(range(48, 57)):
                raise
                continue
            code = line[-2]
            size = line[-1]
            if not code:
                continue
            if int(code) not in new_list:
                continue
            if code not in status_code:
                status_code[code] = 1
            else:
                status_code[code] += 1
            file_size += int(size)
            i += 1
        print_dict(status_code, file_size)
    except (IndexError, KeyboardInterrupt):
        print_dict(status_code, file_size)
        sys.exit(1)
