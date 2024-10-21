from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MONGO_URI: str
    ELASTICSEARCH_HOST: str
    LOG_LEVEL: str = Field(default="info")

    class Config:
        env_file = ".env.dev"


settings = Settings()
