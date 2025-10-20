from collections import UserDict


class PhoneFormatError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Field:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other: 'Field') -> bool:
        return self.value == other.value

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
            raise PhoneFormatError("Phone number should contain digits only!")
        if len(phone) != 10:
            raise PhoneFormatError("Phone number should contain exactly 10 digits!")


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

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
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name):
        del self.data[name]


def main():
    """
    This whole scenario was copied from the homework description
    """
    # Create a new AddressBook instance
    address_book = AddressBook()

    # Create a contact for John and add it to address book
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    address_book.add_record(john_record)

    # Create a contact for Jane and add it to address book
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    address_book.add_record(jane_record)

    # Printing the entire address book content
    for name, record in address_book.data.items():
        print(record)

    # Find John in the address book and change his phone
    john = address_book.find("John")
    john.edit_phone("1234567890", "1112223333")

    # Should print out: Contact name: John, phones: 1112223333; 5555555555
    print(john)

    # Find a specified phone number in John's contact
    found_phone = john.find_phone("5555555555")

    # Should print out: John: 5555555555
    print(f"{john.name}: {found_phone}")

    # Should delete Jane's contact record from the address book
    address_book.delete("Jane")

    # Bonus 1: test validation of phone length
    for invalid_phone in ("5x555555x5", "55555"):
        try:
            john.edit_phone("5555555555", invalid_phone)
        except PhoneFormatError as e:
            print(f"Expected error: {e}")

    # Bonus 2: test phone removal
    john.remove_phone("5555555555")


if __name__ == "__main__":
    main()