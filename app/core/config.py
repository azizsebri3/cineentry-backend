import os

class Settings:
    PROJECT_NAME: str = "Movie Reservation System"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    BACKEND_CORS_ORIGINS: list = []

settings = Settings()