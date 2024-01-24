#!/usr/bin/python3
"""
Log parsing interview question
"""

import sys


if __name__ == '__main__':
    total_file_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in status_codes}

    def display_stats(stats: dict, file_size: int) -> None:
        """
        Displays file size and status code
        """
        print("File size: {:d}".format(total_file_size))
        for code, count in sorted(stats.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            line_count += 1
            line_data = line.split()
            try:
                line_status_code = line_data[-2]
                if line_status_code in status_code_counts:
                    status_code_counts[line_status_code] += 1
            except BaseException:
                pass
            try:
                line_file_size = int(line_data[-1])
                total_file_size += line_file_size
            except BaseException:
                pass
            if line_count % 10 == 0:
                display_stats(status_code_counts, total_file_size)
        display_stats(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        display_stats(status_code_counts, total_file_size)
        raise
