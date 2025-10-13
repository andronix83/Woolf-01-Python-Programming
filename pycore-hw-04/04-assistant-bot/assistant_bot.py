def parse_input(user_input: str) -> tuple[str, str]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args
    if not contacts.get(name):
        contacts[name] = phone
        return "Contact added."
    else:
        return f"Contact '{name}' already exists."

def change_contact(args: str, contacts: dict[str, str]) -> str:
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return f"Contact '{name}' updated."
    else:
        return "Contact not found."

def show_phone(args: str, contacts: dict[str, str]) -> str:
    name, = args
    phone = contacts[name]
    return phone

def show_all(contacts: dict[str, str]) -> list[str]:
    return [f"{name}: {phone}" for name, phone in contacts.items()]


def main():
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
            for contact in show_all(contacts):
                print(f" - {contact}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
