from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_NAME: str = Field(default="", description="Имя базы данных")
    DB_USER: str = Field(default="", description="Имя пользователя базы данных")
    DB_PASSWORD: str = Field(default="", description="Пароль пользователя базы данных")
    DB_HOST: str = Field(default="", description="Хост базы данных")
    DB_PORT: int = Field(default=5432, description="Порт подключения к базе данных")
    API_HOST: str = Field(default="", description="Хост API")
    API_PORT: int = Field(default=8000, description="Порт API")

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
