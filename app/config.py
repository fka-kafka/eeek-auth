from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    algorithm: str
    priv_key_path: str
    pub_key_path: str

    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_settings():
    return Settings()
