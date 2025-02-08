from pydantic_settings import BaseSettings
from pydantic.networks import PostgresDsn


class Settings(BaseSettings):
    ENV_NAME: str = "local"
    
    # PostgreSQL settings for hotel_management database
    DB_HOST: str = "localhost"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_PORT: int = 5432
    DB_NAME: str = "hotel_management"

    @property
    def DB_URL(self) -> str:
        # Return string representation for asyncpg
        return str(PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=f"{self.DB_NAME}"
        ))

    @property
    def DB_URL_SYNC(self) -> str:
        # Return string representation for sync connection
        return str(PostgresDsn.build(
            scheme="postgresql",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=f"{self.DB_NAME}"
        ))

settings = Settings()


