from pydantic import SecretStr
from .requests import CreateProfileRequest


class CreateProfileResponse(CreateProfileRequest):
    id: int
    password: SecretStr
