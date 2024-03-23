from pydantic import Field, BaseSettings


class Settings(BaseSettings):
    DBNAME: str = Field(default="DBNAME", description="Имя базы данных")
    DB_USER: str = Field(default="DB_USER", description="Имя пользователя базы данных")
    PASSWORD: str = Field(default="PASSWORD", description="Пароль пользователя базы данных")
    HOST: str = Field(default="HOST", description="Хост базы данных")
    PORT: int = Field(default=5432, description="Порт подключения к базе данных")
    API_HOST: str = Field(default="127.0.0.1", description="Хост API")
    API_PORT: int = Field(default=5000, description="Порт API")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'



settings = Settings()


