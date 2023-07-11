import sys

def print_stats(file_size, status_codes):
    """
    Prints the current statistics for file size and status codes.

    :param file_size: The total file size.
    :type file_size: int
    :param status_codes: A dictionary containing the number of lines for each status code.
    :type status_codes: dict
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def process_log():
    """
    Processes the log data from standard input.
    """
    file_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            file_size += int(parts[-1])
            code = parts[-2]
            if code not in status_codes:
                status_codes[code] = 0
            status_codes[code] += 1
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)

if __name__ == '__main__':
    process_log()
