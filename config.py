from pydantic import IPvAnyAddress, PostgresDsn, EmailStr, AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: IPvAnyAddress
    port: int
    secret: str  # openssl rand -hex 32
    postgres_url: PostgresDsn
    token_lifetime: int
    system_username: str
    system_pwd: str
    system_email: EmailStr
    domain: str
    static_url: str = ""

    class Config:
        env_file = '.env'


Config = Settings()
