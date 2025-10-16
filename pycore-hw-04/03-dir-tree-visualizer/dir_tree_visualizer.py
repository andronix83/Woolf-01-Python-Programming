import argparse
import os
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Define color constants for Colorama
FOLDER_COLOR = Fore.BLUE + Style.BRIGHT
FILE_COLOR = Fore.YELLOW + Style.BRIGHT
ERROR_COLOR = Fore.RED + Style.BRIGHT

# Safety limit to avoid very deep trees
MAX_RECURSION_LEVEL = 100


def visualize_directory_tree(path: Path, prefix: str = '', level: int = 0):
    """
    Recursively prints the directory tree structure with colored output.

    :param path: The current directory or file Path object.
    :param prefix: The string prefix for proper indentation and lines.
    :param level: The current depth level (used for recursion limit).
    """

    # Protecting the script from stack overflow :)
    if level > MAX_RECURSION_LEVEL:
        print(f"{prefix}{ERROR_COLOR}--- Recursion limit reached ---")
        return

    try:
        # Get a sorted list of all contents (files and directories)
        contents = sorted(list(path.iterdir()))
    except PermissionError:
        print(f"{prefix}{ERROR_COLOR}[Permission Denied]")
        return
    except FileNotFoundError:
        # This shouldn't happen if the initial validation is correct
        return

    # Determine the visual components for the tree lines
    pointers = ['├── '] * (len(contents) - 1) + ['└── ']

    for i, item in enumerate(contents):
        # Determine the pointer for the current item
        pointer = pointers[i]

        # Determine the display color
        if item.is_dir():
            display_name = '📂' + FOLDER_COLOR + item.name + os.sep
        else:
            display_name = '📜' + FILE_COLOR + item.name

        # Print the current line: prefix + pointer + colored name
        print(f"{prefix}{pointer}{display_name}")

        # If the item is a directory, recurse into it
        if item.is_dir():
            # Calculate the new prefix for the sub-items
            extension = '│   ' if i < len(contents) - 1 else '    '
            new_prefix = prefix + extension

            # Recursive call
            visualize_directory_tree(item, prefix=new_prefix, level=level + 1)

def get_dir_path_from_args() -> str:
    # Read and parse the provided argument with the root path
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory_path",
        type=str,
        help="The path to the root directory to visualize."
    )
    return parser.parse_args().directory_path

def validate_path(target_path: Path):
    # Validate Input Path using pathlib
    if not target_path.exists():
        print(f"{ERROR_COLOR}Error: Path '{target_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not target_path.is_dir():
        print(f"{ERROR_COLOR}Error: Path '{target_path}' is not a directory.", file=sys.stderr)
        sys.exit(1)


def main():
    target_path = Path(get_dir_path_from_args())

    validate_path(target_path)

    # Print the root directory, which is guaranteed to be a directory here
    print(f"\n📦{FOLDER_COLOR}{target_path.resolve()}{os.sep}{Style.DIM}")

    # Start the recursive visualization
    visualize_directory_tree(target_path)
    print()


if __name__ == "__main__":
    main()