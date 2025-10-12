import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Returns a sorted list of unique random numbers between min and max.

    :param min: minimum number (not less than 1)
    :param max: maximum number (not greater than 1000)
    :param quantity: number of numbers to return
    :return: list of unique randomly drawn numbers
    """

    # 1. Input validation
    is_valid_input_params = (
            # min is int and greater or equal to 1
            isinstance(min, int) and min >= 1 and
            # max is int and less or equal to 1000
            isinstance(max, int) and max <= 1000 and
            # range is int as well
            isinstance(quantity, int) and
            # range is large enough to pick enough of unique numbers
            0 < quantity <= max - min + 1
    )

    if not is_valid_input_params:
        return []

    # 2. Number generation based on inclusive range of possible numbers
    range_of_possible_numbers = range(min, max + 1)

    # Use random.sample to select 'quantity' unique numbers from the range
    randomly_drawn_numbers = random.sample(range_of_possible_numbers, quantity)

    # 3. Sort the generated result and return it
    return sorted(randomly_drawn_numbers)

def main():
    # Valid test cases
    valid_draw_1 = get_numbers_ticket(1, 49, 6)
    print(f"Valid Draw (1-49, 6 numbers): {valid_draw_1}")

    valid_draw_2 = get_numbers_ticket(10, 20, 5)
    print(f"Valid Draw (10-20, 5 numbers): {valid_draw_2}")

    valid_draw_3 = get_numbers_ticket(100, 500, 10)
    print(f"Valid Draw (100-500, 10 numbers): {valid_draw_3}")


    # Invalid test cases
    invalid_min = get_numbers_ticket(0, 49, 6)
    print(f"Invalid Draw (min < 1): {invalid_min}")

    invalid_max = get_numbers_ticket(1, 1001, 6)
    print(f"Invalid Draw (max > 1000): {invalid_max}")

    invalid_quantity_for_range = get_numbers_ticket(1, 5, 6)
    print(f"Invalid Draw (quantity > range): {invalid_quantity_for_range}")

    invalid_quantity_zero = get_numbers_ticket(1, 10, 0)
    print(f"Invalid Draw (quantity = 0): {invalid_quantity_zero}")

    invalid_quantity_negative = get_numbers_ticket(1, 10, -5)
    print(f"Invalid Draw (quantity = -5): {invalid_quantity_negative}")

    invalid_range = get_numbers_ticket(50, 30, 6)
    print(f"Invalid Draw (min > max): {invalid_range}")


if __name__ == '__main__':
    main()
