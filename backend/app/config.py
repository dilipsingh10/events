from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    app_name: str = "Event Management API"
    database_url: str = "sqlite+pysqlite:///./dev.db"
    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    cors_allowed_origins: List[AnyHttpUrl] | List[str] = ["http://localhost:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"


settings = Settings()

