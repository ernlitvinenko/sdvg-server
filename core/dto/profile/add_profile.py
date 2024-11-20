from pydantic import BaseModel, field_validator
from fastapi import HTTPException
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


class NewProfile(BaseModel):
    phone: int
    username: str
    password: str
    email: str

    @field_validator("phone")
    def validate_phone(cls, value):
        if phone_validation(value):
            return value
        raise HTTPException(status_code=422, detail="Неправильно набран номер телефона")