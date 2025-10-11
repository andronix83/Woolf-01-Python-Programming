import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a user-provided phone number based on specific rules.

    :param phone_number: raw phone number to normalize.
    :return: The normalized phone number string.
    """
    # 1. Strip extra whitespaces (if present)
    cleaned_phone_number = phone_number.strip()

    # 2. Remove all extra symbols except digits and the plus sign
    cleaned_phone_number = re.sub(r'[^\d+]', '', cleaned_phone_number)

    # 3. Apply normalization rules from the requirements
    if cleaned_phone_number.startswith('+'):
        # if the number starts with plus - we assume it is correct and complete
        normalized_number = cleaned_phone_number
    elif cleaned_phone_number.startswith('380'):
        # if the cleaned number starts with 380 - we only add plus
        normalized_number = '+' + cleaned_phone_number
    elif cleaned_phone_number.startswith('0'):
        # if the cleaned number starts with 0,
        # we assume it is a Ukrainian number and add +38
        normalized_number = '+38' + cleaned_phone_number
    else:
        # Fallback for other unexpected formats, for robust code
        normalized_number = cleaned_phone_number

    return normalized_number


def test_normalize_phone(phone_list: list) -> None:
    """
    Runs the validation examples for the normalize_phone function.
    """

    all_tests_passed = True

    for provided, expected in phone_list:
        normalized = normalize_phone(provided)
        passed = normalized == expected
        status = "✅ PASSED" if passed else "❌ FAILED"

        if not passed:
            all_tests_passed = False

        # Print the test result in a clear format
        print(f"Provided:   '{provided}'")
        print(f"Expected:   '{expected}'")
        print(f"Actual:     '{normalized}'")
        print(f"Result:     {status}")
        print("-" * 30)

    if all_tests_passed:
        print("\nAll tests passed successfully! 🎉")
    else:
        print("\nSome tests failed. 🛑")


if __name__ == "__main__":

    # first set of phone numbers from the task description section
    phone_numbers_1 = [
        ("    +38(050)123-32-34",   "+380501233234"),
        ("     0503451234",         "+380503451234"),
        ("(050)8889900",            "+380508889900"),
        ("38050-111-22-22",         "+380501112222"),
        ("38050 111 22 11   ",      "+380501112211")
    ]

    # second set of phone numbers from the task examples section
    phone_numbers_2 = [
        ("067\\t123 4567",          "+380671234567"),
        ("(095) 234-5678\\n",       "+380952345678"),
        ("+380 44 123 4567",        "+380441234567"),
        ("380501234567",            "+380501234567"),
        ("    +38(050)123-32-34",   "+380501233234"),
        ("     0503451234",         "+380503451234"),
        ("(050)8889900",            "+380508889900"),
        ("38050-111-22-22",         "+380501112222"),
        ("38050 111 22 11   ",      "+380501112211"),
    ]

    # run the tests
    test_normalize_phone(phone_numbers_1)
    test_normalize_phone(phone_numbers_2)