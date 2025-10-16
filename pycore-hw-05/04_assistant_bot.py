from typing import Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"❌ Please enter enough arguments for the command!"
        except (KeyError, IndexError) as e:
            return e.args[0] # Message from the original error
    return inner

def parse_input(user_input: str) -> tuple[str, list[str]]:
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args # raises ValueError if not enough arguments
    if contacts.get(name):
        raise KeyError(f"❌ Contact '{name}' already exists! Enter another name.")
    contacts[name] = phone
    return f"✅ Contact '{name}' with the phone '{phone}' was added."

@input_error
def change_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args # raises ValueError if not enough arguments
    if not contacts.get(name):
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    contacts[name] = phone
    return f"✅ Contact '{name}' ws updated with the new phone: '{phone}'."

@input_error
def show_phone(args: str, contacts: dict[str, str]) -> str:
    name, = args # raises ValueError if no arguments provided
    if not contacts.get(name):
        raise KeyError(f"❌ Contact '{name}' doesn't exists! Enter another name.")
    phone = contacts[name]
    return phone

@input_error
def show_all(contacts: dict[str, str]) -> list[str]:
    return [f"{name}: {phone}" for name, phone in contacts.items()]

def print_all_contacts(contacts: dict[str, str]) -> None:
    if contacts:
        for i, contact in enumerate(show_all(contacts)):
            print(f"{i + 1}. {contact}")
    else:
        print("No contacts to show!")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command ➡️ ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print_all_contacts(contacts)
        else:
            print("❌ Invalid or empty command!")


if __name__ == "__main__":
    main()
