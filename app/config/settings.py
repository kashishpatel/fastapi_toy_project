from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    DATABASE_URL: str
    ALGORITHM: str
    DEBUG: bool
    API_PREFIX: str

    class Config:
        env_file = ".env"  # Load environment variables from a .env file

# Create an instance of the settings
settings = Settings()
