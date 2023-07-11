#!/usr/bin/python3
"""Web Request Stats module"""


iteration = 1
while True:
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    total_size = 0
    line_count = 0
    try:
        line = input()
        while line:
            file_size = int(line[line.rfind(" ") + 1:])
            status_code = int(line[line.rfind(" ", 0,
                                              line.rfind(" ") - 1) +
                                   1:line.rfind(" ")])
            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1
            if line_count == 10 * iteration:
                print("File size:", total_size)
                for key, value in status_codes.items():
                    if value:
                        print("{}:".format(key), value)
                break
            new_line = input()
        iteration += 1
    except KeyboardInterrupt:
        print("File size:", total_size)
        for key, value in status_codes.items():
            if value:
                print("{}:".format(key), value)
