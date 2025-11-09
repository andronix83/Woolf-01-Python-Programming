type SalaryStats = tuple[int, float]

def total_salary(path: str) -> SalaryStats:
    """
    Calculates the total and average salary from a file.
    The file must have one employee per line, formatted as: '<Name>,<Salary>'

    Args:
        path (str): The path to the data file.

    Returns:
        SalaryStats: A tuple containing (total_salary, average_salary).
               Returns (0, 0) if no valid salaries are found.
    """
    # Read the list of clean lines from the file
    data_lines = read_file_to_list(path)

    total: int = 0
    count: int = 0

    # Process the lines in order to extract salaries
    for line in data_lines:
        try:
            parts = line.split(',')
            if len(parts) == 2:
                # Attempt to convert the salary string to an integer
                salary: int = int(parts[1].strip())
                total += salary
                count += 1
            else:
                print(f"Warning: Line format error (no comma found): '{line}'")
        except ValueError:
            print(f"Warning: Could not parse salary (empty or not an integer): '{line}'")
            continue

    # Calculate the average salary or just return 0
    average = total / count if count > 0 else 0

    return total, round(average, 2)


def read_file_to_list(path: str) -> list[str]:
    """
    Reads a file and returns a list of its lines, stripped of whitespaces.
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


def main() -> None:
    for file_type in("provided", "correct", "broken", "non-existent"):
        file_name = f"employee_data_{file_type}.txt"
        print(f"\nProcessing the {file_type} data file ({file_name}):")

        total, average = total_salary(f"data_files/{file_name}")
        print(f"Total amount of salary: {total}")
        print(f"Average salary: {average}")


if __name__ == "__main__":
    main()