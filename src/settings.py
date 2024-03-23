from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_NAME: str = Field(description="Имя базы данных")
    DB_USER: str = Field(description="Имя пользователя базы данных")
    DB_PASSWORD: str = Field(description="Пароль пользователя базы данных")
    DB_HOST: str = Field(description="Хост базы данных")
    DB_PORT: int = Field(description="Порт подключения к базе данных")
    API_HOST: str = Field(description="Хост API")
    API_PORT: int = Field(description="Порт API")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
