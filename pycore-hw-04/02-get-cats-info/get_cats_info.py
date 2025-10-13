
def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Creates a list of dictionaries with cat info from a file using read_file().
    The file must have one cat info per line, formatted as: '<Id>,<Name>,<Age>'

    Args:
        path (str): The path to the data file.

    Returns:
        list: A list containing dictionaries with cat infos.
    """

    # Read the list of clean lines from the file
    data_lines = read_file_to_list(path)

    cat_info_list = []

    # Process the lines in order to extract salaries
    for line in data_lines:
        parts = line.split(',')
        if len(parts) == 3:
            cat_info = {"id" : parts[0], "name" : parts[1], "age" : parts[2]}
            cat_info_list.append(cat_info)
        else:
            print(f"Warning: Line format error (missing columns): '{line}'")

    return cat_info_list


def read_file_to_list(path: str) -> list[str]:
    """
    Reads a file and returns a list of its lines, stripped of whitespaces.
    Function was copied from the previous task :)
    """
    lines = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    lines.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: File not found at path: {path}")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

    return lines

def main():
    for file_type in ("provided", "correct", "broken", "non-existent"):
        file_name = f"cats_data_{file_type}.txt"

        print(f"\nProcessing the {file_type} data file ({file_name}):")
        # print each item from new line
        for cat in get_cats_info(f"data_files/{file_name}"):
            print(cat)


if __name__ == "__main__":
    main()

