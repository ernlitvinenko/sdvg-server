"""Data validation module"""


import re


def phone_validation(number: int) -> bool:
    """Validates if the given phone number meets certain criteria.

    Args:
        number (int): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise."""
    number_str = str(number)
    regex = r"^\d{10}$|^\d{11}$"
    if re.match(regex, number_str):
        return True
    return False


def username_validation(username: str):
    """Validates if the given username meets certain criteria.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise."""
    latyn_regex = r"^[a-zA-Z]+(\s[a-zA-Z]+){1,2}$"
    cyrilic_regex = r"^[а-яА-Я]+(\s[а-яА-Я]+){1,2}$"

    if re.match(latyn_regex, username) or re.match(cyrilic_regex, username):
            return True
    return False


def email_validation(email: str):
    """Validates if the given email meets certain criteria.

    Args:
        email (str): The email to validate.

    Returns:
        bool: True if the email is valid, False otherwise."""
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
    if re.match(regex, email):
        return True
    return False


def password_validation(password:str):
    """Validates if the given password meets certain criteria.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, False otherwise."""
    regex = r"^[a-zA-Zа-яА-Я0-9_+=-@.,/]{8,16}"
    if re.match(regex, password):
        return True
    return False