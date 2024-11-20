from pydantic import BaseModel, Field, SecretStr
from .requests import NewProfile


class CreateProfileResponse(NewProfile):
    id: int
    password: SecretStr
