import os
import signal


def compute_metrics():
    # Dictionary to store total file size and count of lines by status code
    metrics = {'total_size': 0, 'status_codes': {}}

    try:
        line_count = 0
        for line in iter(input, ''):
            line_count += 1
            ip, date, request, status_code, file_size = parse_line(line)
            
            # Update total file size
            metrics['total_size'] += file_size

            # Update count of lines by status code
            if status_code not in metrics['status_codes']:
                metrics['status_codes'][status_code] = 0
            metrics['status_codes'][status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(metrics)

    except (KeyboardInterrupt, EOFError):
        print_statistics(metrics)


def parse_line(line):
    parts = line.strip().split()
    ip = parts[0]
    date = parts[2].strip('[]')
    request = parts[4][1:]
    status_code = parts[5]
    file_size = int(parts[6])
    return ip, date, request, status_code, file_size


def print_statistics(metrics):
    print("Total file size: File size:", metrics['total_size'])

    # Sort and print count of lines by status code in ascending order
    sorted_status_codes = sorted(metrics['status_codes'].items(), key=lambda x: x[0])
    for code, count in sorted_status_codes:
        print(f"{code}: {count}")


def signal_handler(signum, frame):
    # Handle the keyboard interruption (Ctrl + C)
    print()
    os._exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    compute_metrics()
