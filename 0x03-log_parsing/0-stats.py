#!/usr/bin/python3

"""
 a script that reads stdin line by line and computes metrics
"""


import sys
import signal


# Initialize metrics
total_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_metrics():
    """
    Print the computed metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """
    Handle keyboard interruption and print metrics.
    """
    print_metrics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue

        ip_address = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]

        # Validate and update metrics
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        total_size += int(file_size)
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()
    except Exception:
        continue

# Print final metrics
print_metrics()
