import pickle, sys
from collections import UserDict
from datetime import datetime, timedelta
from typing import Callable


NUMBER_OF_UPCOMING_DAYS = 20
DATE_FORMAT = '%d.%m.%Y'
ADDRESS_BOOK_FILE_NAME = 'data_files/addressbook.pkl'

class PhoneFormatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Field:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'Field') -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str):
        self.__validate_phone(value)
        super().__init__(value)

    def __validate_phone(self, phone):
        if not phone.isdigit():
            raise PhoneFormatError("❌ Phone number should contain digits only!")
        if len(phone) != 10:
            raise PhoneFormatError("❌ Phone number should contain exactly 10 digits!")

class Birthday(Field):
    def __init__(self, date: str):
        try:
            super().__init__(datetime.strptime(date, DATE_FORMAT).date())
        except ValueError:
            raise ValueError("❌ Invalid date format! Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime(DATE_FORMAT)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def add_birthday(self, date: str) -> None:
        self.birthday = Birthday(date)

    def find_phone(self, phone_str: str) -> Phone | None:
        for phone in self.phones:
            if phone.value == phone_str:
                return phone
        return None

    def edit_phone(self, old_phone_str: str, new_phone_str: str) -> None:
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_str:
                self.phones[i] = Phone(new_phone_str)

    def remove_phone(self, phone_str: str) -> None:
        self.phones.remove(Phone(phone_str))

    def __str__(self):
        result_str = f"Contact name: {self.name.value}, phone(s): {', '.join(p.value for p in self.phones)}"
        if self.birthday:
            result_str += f", birthday: {self.birthday}"
        return result_str


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.get(name)

    def delete(self, name):
        del self.data[name]

    def get_upcoming_birthdays(self) -> list[tuple]:
        today_date = datetime.today().date()
        end_date = today_date + timedelta(days=NUMBER_OF_UPCOMING_DAYS)
        contacts_with_upcoming_birthdays = []

        for contact in self.data.values():
            if not contact.birthday:
                continue
            physical_bd = contact.birthday.value
            this_or_next_year_bd = physical_bd.replace(year=today_date.year)
            if this_or_next_year_bd < today_date:
                this_or_next_year_bd = this_or_next_year_bd.replace(year=today_date.year + 1)
            if today_date <= this_or_next_year_bd <= end_date:
                congratulation_date = this_or_next_year_bd
                if this_or_next_year_bd.weekday() in (5, 6):
                    days_to_next_monday = 7 - this_or_next_year_bd.weekday()
                    congratulation_date = (this_or_next_year_bd + timedelta(days=days_to_next_monday))
                contacts_with_upcoming_birthdays.append((contact, congratulation_date))
            contacts_with_upcoming_birthdays.sort(key=lambda x: x[1])
        return contacts_with_upcoming_birthdays

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"❌ Please enter enough arguments for the command!"
        except (KeyError, IndexError, PhoneFormatError) as e:
            return e.args[0] # Message from the original error
    return inner

def parse_input(user_input: str) -> tuple[str, list[str]]:
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list[str], address_book: AddressBook) -> str:
    name, phone, *_ = args
    record = address_book.find(name)
    message = f"✅ Contact '{name}' was updated."
    if record is None:
        record = Record(name)
        address_book.add_record(record)
        message = f"✅ Contact '{name}' was added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args: list[str], address_book: AddressBook) -> str:
    name, old_phone, new_phone = args # raises ValueError if not enough arguments
    found_record = address_book.find(name)
    if not found_record:
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    found_record.edit_phone(old_phone, new_phone)
    return f"✅ Contact '{name}' ws updated with the new phone: '{new_phone}'."

@input_error
def show_phones(args: str, address_book: AddressBook) -> str:
    name, = args # raises ValueError if no arguments provided
    found_record = address_book.find(name)
    if not found_record:
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    return ', '.join(p.value for p in found_record.phones)

@input_error
def show_all(address_book: AddressBook) -> list[str]:
    return [f"{record}" for record in address_book.data.values()]

def print_all_contacts(address_book: AddressBook) -> None:
    if address_book.data:
        for i, contact in enumerate(show_all(address_book)):
            print(f"{i + 1}. {contact}")
    else:
        print("No contacts to show!")

@input_error
def add_birthday(args: list[str], address_book: AddressBook) -> str:
    name, birthday = args
    found_record = address_book.find(name)
    if not found_record:
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    found_record.add_birthday(birthday)
    return f"✅ Contact '{name}' ws updated with birthday: '{birthday}'."

@input_error
def show_birthday(args: list[str], address_book: AddressBook) -> str:
    name, = args
    found_record = address_book.find(name)
    if not found_record:
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    return found_record.birthday

def print_upcoming_birthdays(address_book: AddressBook):
    if address_book.data:
        upcoming_birthdays = address_book.get_upcoming_birthdays()
        if upcoming_birthdays:
            print(f"List of contacts with upcoming birthdays (next {NUMBER_OF_UPCOMING_DAYS} days):")
            for i, (record, cong_date) in enumerate(upcoming_birthdays):
                print(f"{i + 1}. {record.name} - birthday: {record.birthday}, congratulation date: {cong_date.strftime(DATE_FORMAT)}")
        else:
            print("No contacts with upcoming birthdays!")
    else:
        print("No contacts to show!")

def save_data(address_book, filename):
    with open(filename, "wb") as f:
        pickle.dump(address_book, f)

def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # when open for the first time
        return AddressBook()

def main():
    address_book = load_data(ADDRESS_BOOK_FILE_NAME)

    print("Welcome to the assistant bot!")

    try:
        while True:
            user_input = input("Enter a command ➡️ ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(address_book, ADDRESS_BOOK_FILE_NAME)
                print("Address book saved. Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, address_book))
            elif command == "change":
                print(change_contact(args, address_book))
            elif command == "phone":
                print(show_phones(args, address_book))
            elif command == "all":
                print_all_contacts(address_book)
            elif command == "add-birthday":
                print(add_birthday(args, address_book))
            elif command == "show-birthday":
                print(show_birthday(args, address_book))
            elif command == "birthdays":
                print_upcoming_birthdays(address_book)
            else:
                print("❌ Invalid or empty command!")

    except KeyboardInterrupt:
        print("\nAssistant bot was interrupted by user (Ctrl+C).")
        print(f"Saving Address book state to the file: {ADDRESS_BOOK_FILE_NAME}")
        save_data(address_book, ADDRESS_BOOK_FILE_NAME)
        sys.exit(0) # Exit gracefully after saving

if __name__ == "__main__":
    main()