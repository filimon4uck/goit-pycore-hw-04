import json


def contacts_add(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact with name {name} is exist"
    contacts[name] = phone
    return 'Contact added'


def contacts_change(args, contacts):
    name, new_phone = args
    if not name in contacts:
        return f"Contact with name {name} not found"
    else:
        contacts[name] = new_phone
        return "Contact updated"


def phone(args, contacts):
    name = args[0]
    if not name in contacts:
        return f"Contact with name {name} not found"
    else:
        return contacts[name]
