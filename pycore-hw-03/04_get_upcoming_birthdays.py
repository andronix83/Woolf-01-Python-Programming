from datetime import datetime, timedelta


# Increase this number if no results returned!
NUMBER_OF_UPCOMING_DAYS = 7
DATE_FORMAT = '%Y.%m.%d'

def get_upcoming_birthdays(users: list) -> list:
    """
    Returns a list of users with upcoming birthdays within the next NUMBER_OF_UPCOMING_DAYS days.

    :param users: list of dictionaries, each containing 'name' and 'birthday' (in 'YYYY.MM.DD' format)
    :return: Ordered list of dictionaries, each containing user's 'name' and 'congratulation_date'
    """

    today_date = datetime.today().date()
    end_date = today_date + timedelta(days=NUMBER_OF_UPCOMING_DAYS)

    users_with_upcoming_birthdays = []

    for current_user in users:
        try:
            # Parse the original (physical) birthday date from formatted string
            physical_bd = datetime.strptime(current_user['birthday'], DATE_FORMAT).date()

            # Adjust the birthday year to the current year
            this_or_next_year_bd = physical_bd.replace(year=today_date.year)

            # If the birthday has already occurred this year, get the next year's birthday
            if this_or_next_year_bd < today_date:
                this_or_next_year_bd = this_or_next_year_bd.replace(year=today_date.year + 1)

            # Check if the upcoming birthday is within the next NUMBER_OF_UPCOMING_DAYS days
            if today_date <= this_or_next_year_bd <= end_date:
                congratulation_date = this_or_next_year_bd
                # Move the birthday to the next Monday if it falls on a weekend
                if this_or_next_year_bd.weekday() in (5, 6):
                    days_to_next_monday = 7 - this_or_next_year_bd.weekday()
                    congratulation_date = (this_or_next_year_bd + timedelta(days=days_to_next_monday))

                users_with_upcoming_birthdays.append({
                    "name": current_user['name'],
                    "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
                })
        except ValueError as e:
            print(f"Skipping user {current_user['name']} due to invalid date format: {e}")

    # BONUS for convenience: sort the list by congratulation_date approaching
    users_with_upcoming_birthdays.sort(key=lambda x: x['congratulation_date'])

    return users_with_upcoming_birthdays


if __name__ == '__main__':
    test_users_data = [
        {"name": "Eleanor Vance", "birthday": "1963.07.19"},
        {"name": "Arthur Pinter", "birthday": "1998.02.05"},
        {"name": "Sophia Clarke", "birthday": "1975.11.30"},
        {"name": "Ethan Wright", "birthday": "1989.04.12"},
        {"name": "Olivia Miller", "birthday": "2001.09.23"},
        {"name": "Liam Scott", "birthday": "1955.08.08"},
        {"name": "Ava Hayes", "birthday": "1994.12.01"},
        {"name": "Noah Davis", "birthday": "1982.03.17"},
        {"name": "Isabella Flores", "birthday": "1970.06.28"},
        {"name": "Lucas Chen", "birthday": "2004.01.10"},
        {"name": "Mia Reynolds", "birthday": "1967.10.19"},
        {"name": "Jackson Ward", "birthday": "1991.05.22"},
        {"name": "Charlotte Baker", "birthday": "1958.02.14"},
        {"name": "Alexander King", "birthday": "1986.11.07"},
        {"name": "Amelia Nelson", "birthday": "2003.07.03"},
        {"name": "Henry Gomez", "birthday": "1978.09.15"},
        {"name": "Evelyn Ross", "birthday": "1996.04.29"},
        {"name": "Daniel Carter", "birthday": "1960.01.26"},
        {"name": "Harper Morris", "birthday": "1984.12.11"},
        {"name": "James Perry", "birthday": "2000.03.06"},
        {"name": "Abigail Reed", "birthday": "1973.10.18"},
        {"name": "Benjamin Cox", "birthday": "1999.08.25"},
        {"name": "Elizabeth Long", "birthday": "1965.10.17"},
        {"name": "Samuel Foster", "birthday": "1980.02.09"},
        {"name": "Ella Hughes", "birthday": "2005.06.13"},
        {"name": "Joseph Ramirez", "birthday": "1952.11.20"},
        {"name": "Scarlett White", "birthday": "1992.01.01"},
        {"name": "Matthew Brooks", "birthday": "1977.04.05"},
        {"name": "Grace Gray", "birthday": "1988.07.24"},
        {"name": "David Morgan", "birthday": "1969.09.02"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(test_users_data)

    print(f"List of users with upcoming birthdays (next {NUMBER_OF_UPCOMING_DAYS} days):")
    for index, user in enumerate(upcoming_birthdays):
        print(f"{index+1}. {user}")