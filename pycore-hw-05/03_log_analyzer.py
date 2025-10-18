import argparse
import sys


# Only lines with these log levels will be counted and
# printed (if allowed), other levels will be ignored and skipped
SUPPORTED_LOG_LEVELS = ("INFO", "DEBUG", "WARNING", "ERROR")

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

def pretty_print_counters(level_counter):
    # TODO: Implement output in the table
    # Skip the items with zero occurrences
    print(level_counter)


def log_analyzer():
    log_file_name, levels_to_print = parse_cmd_args()
    level_counter = {x: 0 for x in SUPPORTED_LOG_LEVELS}

    # Iterate through the lines of the file
    # TODO: Handle missing or incorrect file
    with open(log_file_name, "r") as log_file:
        for line in log_file:
            # TODO: Handle incorrect line format
            _, _, level, *_ = line.strip().split()
            level_counter[level.upper()] += 1
            # TODO: Validate provided levels
            if level in levels_to_print:
                print(line.strip())

        # Output the counters in a table format
        pretty_print_counters(level_counter)


if __name__ == '__main__':
    log_analyzer()