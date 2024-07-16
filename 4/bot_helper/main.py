from pathlib import Path
from command_parser import parse_input
from contacts import contacts_add, contacts_change, phone
import json

current_dir = Path(__file__).parent


def main():
    contacts_file = current_dir / "contacts.txt"
    if contacts_file.exists():
        with open(file=current_dir / "contacts.txt", mode='r', encoding='utf-8') as reader:
            contacts = json.load(reader)

    else:
        contacts = {}
    try:
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            elif command == 'add':
                print(contacts_add(args, contacts))
            elif command == 'change':
                print(contacts_change(args, contacts))
            elif command == "phone":
                print(phone(args, contacts))
            elif command == 'all':
                for name, number in contacts.items():
                    print(name, number)
            else:
                print("Invalid command.")
            with open(current_dir / "contacts.txt", 'w', encoding='utf-8') as file:
                json.dump(contacts, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("File not found")


if (__name__ == "__main__"):
    main()
