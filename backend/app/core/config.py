from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    jwt_private_key: str
    jwt_public_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()