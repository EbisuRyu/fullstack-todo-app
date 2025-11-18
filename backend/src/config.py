from functools import cached_property

from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings as PydanticSettings


class BaseSettings(PydanticSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_ignore_empty=True,
        extra="ignore"
    )
    

class MongoSettings(BaseSettings):
    MONGO_URI: str 
    MONGO_DATABASE: str


class Settings:
    
    @cached_property
    def database(self) -> MongoSettings:
        return MongoSettings()


def load_settings() -> Settings:
    return Settings()