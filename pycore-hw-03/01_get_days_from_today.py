from datetime import datetime, timedelta


def get_days_from_today(date: str) -> int:
    """
    Function to get the number of days from specific date till today.

    :param date: input date in the format YYYY-MM-DD
    :return: the number of days between the input date and today.
             A positive number means the date is in the past.
             A negative number means the date is in the future.
             Zero means the date is today.
    :raises ValueError: if the input date string is not in the 'YYYY-MM-DD' format.
    """
    try:
        # Convert the provided date string into a datetime object
        input_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        # Raise an exception if the date format is incorrect or the date is invalid (e.g., 2023-02-30)
        raise ValueError(f"Incorrect date format or invalid date! Please use YYYY-MM-DD. Details: {e}")

    # Get the current date (and time), then normalize it to only the date part
    # to ensure the calculation is purely based on the day difference, not time.
    today_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    # Also normalize the input date to only the date part for a clean day count.
    input_date = input_date.replace(hour=0, minute=0, second=0, microsecond=0)

    # Calculate the difference between the dates
    date_difference: timedelta = today_date - input_date

    return date_difference.days


if __name__ == '__main__':
    print("How many days have passed from several important events:")
    print("===================================================")
    print(f"1. {get_days_from_today("1983-12-30")} days since Andrii Pererva's birthday :)")
    print(f"2. {get_days_from_today("1991-08-24")} days since the Independence of Ukraine")
    print(f"3. {get_days_from_today("2014-02-22")} days since the Revolution of Dignity")
    print(f"4. {get_days_from_today("2019-01-05")} days since granting of the Tomos to Ukrainian Church")
    print(f"5. {get_days_from_today("2022-02-24")} days since full-scale ruzzian invasion to Ukraine")
    print(f"BONUS. {abs(get_days_from_today("2026-01-01"))} days before the new 2026 year!")
