import argparse
import sys
from typing import Final

# Only lines with these log levels will be counted and
# printed (if allowed), other levels will be ignored and skipped
SUPPORTED_LOG_LEVELS: Final[list[str]] = ["INFO", "DEBUG", "WARNING", "ERROR"]

def parse_cmd_args() -> tuple[str, list[str]]:
    """
    Parses command-line arguments for a log file name and optional log levels.
    """
    parser = argparse.ArgumentParser()

    # Add the mandatory positional argument (file name)
    parser.add_argument(
        'filename',
        type=str,
        help='The path and name of the log file to process.'
    )

    # Add the optional argument for log levels
    parser.add_argument(
        '--levels',
        nargs='*', # 0 or more arguments
        default=[], # ensures the variable is an empty list if no levels
        metavar='LEVEL',
        help=(
            'Optional list of log levels to show (e.g., DEBUG INFO WARNING ERROR).\n'
            'If provided, the script will only filter and print these levels.\n'
            'Example: --levels ERROR WARNING'
        )
    )

    # Parse and return the arguments
    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"An error occurred during argument parsing: {e}", file=sys.stderr)
        sys.exit(1)

    return args.filename, args.levels

def validate_log_levels(levels_to_print: list[str]) -> list[str]:
    """
    Validates user provided log levels against SUPPORTED_LOG_LEVELS.
    Removes unsupported levels if they found
    """
    if levels_to_print in SUPPORTED_LOG_LEVELS:
        return levels_to_print
    else:
        unsupported_levels = set(levels_to_print) - set(SUPPORTED_LOG_LEVELS)
        print(f"Warning: Unsupported log levels provided: {', '.join(unsupported_levels)} \n")
        return list(set(SUPPORTED_LOG_LEVELS) & set(levels_to_print))

def pretty_print_counters(level_counter):
    """
    Prints the counters into a formatted table, sorting them in descending order.
    """
    print(f"\n{'Log level':<10} | {'Count':<5}")
    print("-" * 20)
    for level, count in sorted(level_counter.items(), key=lambda x: x[1], reverse=True):
        if count > 0:
            print(f"{level:<10} | {count:<5}")

def log_analyzer() -> None:
    log_file_name, levels_to_print = parse_cmd_args()
    levels_to_print: list[str] = validate_log_levels(levels_to_print)

    level_counter: dict[str, int] = {x: 0 for x in SUPPORTED_LOG_LEVELS}

    # Iterate through the lines of the file
    try:
        with open(log_file_name, "r") as log_file:
            for line in log_file:
                stripped_line: str = line.strip()
                _, _, level, *_ = stripped_line.upper().split()
                if level in level_counter:
                    level_counter[level] += 1
                    if level in levels_to_print:
                        print(stripped_line)
    except FileNotFoundError:
        print(f"Error: File not found at path: {log_file_name}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

    # Output the counters in a table format
    pretty_print_counters(level_counter)


if __name__ == '__main__':
    log_analyzer()