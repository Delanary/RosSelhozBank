import re


def handle_passport(message: str):
    message = message.strip()
    if message.find(" ") != -1:
        message = ''.join(message.split())
    for digit in message:
        if not digit.isdigit():
            raise ValueError("Not a digit")
    return message[:10]


def handle_name(message: str):
    message = message.split()
    if len(message) > 3:
        raise ValueError("Not a name")
    elif len(message) == 3:
        name, surname, last_name = message
        return name, surname, last_name
    elif len(message) == 2:
        name, surname = message
        return name, surname
    else:
        raise ValueError("Submit full information")


def handle_birth_date(message: str):
    message = message.strip()
    if ':' in message:
        message = message.split(':')
    elif '.' in message:
        message = message.split('.')
    else:
        message = message.split(' ')
    try:
        lst = list(map(int, message))
        if len(lst) != 3:
            raise ValueError
        return ':'.join(message)
    except ValueError:
        raise ValueError("Not a datetime")


def handle_mobile_number(message: str):
    message = message.strip()
    message = message.replace(' ', '')
    message = message.replace('(', '')
    message = message.replace(')', '')
    message = message.replace('-', '')
    if len(message) == 11:
        for digit in message:
            if not digit.isdigit():
                raise ValueError("Not a phone number")
        return message
    elif len(message) == 12:
        if message[0] != '+':
            raise ValueError("Not a phone number")
        if message[1] == '7':
            message = message[0] + '8' + message[2:]
        for digit in message[1:]:
            if not digit.isdigit():
                raise ValueError("Not a phone number")
            return message[1:]
    raise ValueError("Not a phone number")


def handle_email(message):
    print("hmmm")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", message):
        raise ValueError("Not a email")
    return message
