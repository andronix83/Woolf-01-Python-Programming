from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # TODO: implementation
		pass

class Phone(Field):
    # TODO: implementation
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # TODO: implementation

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # TODO: implementation
		pass


def main():
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

    # Should print out: 5555555555
    print(f"{john.name}: {found_phone}")

    # Should print out: Jane's contact record
    address_book.delete("Jane")


if __name__ == "__main__":
    main()