import re

from pydantic import BaseModel, field_validator, EmailStr
from fastapi import HTTPException


class CreateProfileRequest(BaseModel):
    phone: int
    username: str
    password: str
    email: EmailStr

    @field_validator("phone")
    def validate_phone(cls, value):
        number_str = str(value)
        regex = r"^\d{10}$|^\d{11}$"
        if re.match(regex, number_str):
            return value
        raise HTTPException(status_code=422, detail="Неправильно набран номер телефона")

    @field_validator("username")
    def validate_username(cls, value):
        latyn_regex = r"^[a-zA-Z]+(\s[a-zA-Z]+){1,2}$"
        cyrilic_regex = r"^[а-яА-Я]+(\s[а-яА-Я]+){1,2}$"

        if re.match(latyn_regex, value) or re.match(cyrilic_regex, value):
            return value
        raise HTTPException(status_code=422, detail="Неправильно введено имя пользователя")

    @field_validator("password")
    def validate_password(cls, value):
        regex = r"^[a-zA-Zа-яА-Я0-9_+=-@.,/]{8,16}"
        if re.match(regex, value):
            return value
        raise HTTPException(status_code=422, detail="Пароль не соответствует требованиям безопасности")
