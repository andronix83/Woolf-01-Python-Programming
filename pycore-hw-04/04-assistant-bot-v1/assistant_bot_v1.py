def parse_input(user_input: str) -> tuple[str, list[str]]:
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args
    if not contacts.get(name):
        contacts[name] = phone
        return f"Contact '{name}' added."
    else:
        return f"ERROR: Contact '{name}' already exists!"

def change_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return f"Contact '{name}' updated."
    else:
        return f"ERROR: Contact '{name}' not found!"

def show_phone(args: str, contacts: dict[str, str]) -> str:
    name, = args
    if contacts.get(name):
        phone = contacts[name]
        return phone
    else:
        return f"ERROR: Contact '{name}' not found!"

def show_all(contacts: dict[str, str]) -> list[str]:
    return [f"{name}: {phone}" for name, phone in contacts.items()]

def print_all_contacts(contacts: dict[str, str]) -> None:
    if contacts:
        for i, contact in enumerate(show_all(contacts)):
            print(f"{i + 1}. {contact}")
    else:
        print("No contacts to show!")


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
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
            print("Invalid or empty command!")


if __name__ == "__main__":
    main()
