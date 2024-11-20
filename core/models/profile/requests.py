import re

from pydantic import BaseModel, field_validator
from fastapi import HTTPException


class NewProfile(BaseModel):
    phone: int
    username: str
    password: str
    email: str

    @field_validator("phone")
    def validate_phone(cls, value):
        number_str = str(value)
        regex = r"^\d{10}$|^\d{11}$"
        if re.match(regex, number_str):
            return value
        raise HTTPException(status_code=422, detail="Неправильно набран номер телефона")
