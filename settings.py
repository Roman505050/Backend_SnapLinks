from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str
    PORT: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

