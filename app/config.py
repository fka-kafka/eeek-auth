from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    reset_algorithm: str
    auth_algorithm: str
    priv_key_path: str
    pub_key_path: str
    secret_key: str
    access_token_expiry_minutes: str
    reset_token_expiry_minutes: str
    redis_password: str
    redis_host: str
    redis_port: str
    smtp_username: str
    smtp_password: str
    smtp_server: str
    smtp_port: str
    frontend_url: str
    google_cid: str
    linkedin_cid: str
    linkedin_secret: str
    linkedin_redirect_uri: str

    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_settings():
    return Settings()
