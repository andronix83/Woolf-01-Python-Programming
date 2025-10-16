import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator:
    """
    A generator function that takes a string of text and yields all found
    numbers as floats, one by one.
    """

    # Regex pattern to find numbers (both positive and negative)
    # This pattern matches numbers like "100", "3.14", "-5", "+1.2" etc.
    number_pattern = r'[+-]?\d+(?:\.\d+)?'

    # Find all matches in the text
    for match in re.finditer(number_pattern, text):
        # Yields rounded float, that represents some amount of money
        yield float(match.group(0))

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

def main():
    text = """Загальний дохід працівника складається з декількох частин: 1000.01 як \
основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""

    total_income = sum_profit(text, generator_numbers)

    # Expected value: 1351.46
    print(f"Загальний дохід: {round(total_income, 2)}")


if __name__ == '__main__':
    main()