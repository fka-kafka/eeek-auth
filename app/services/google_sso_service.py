from google.oauth2 import id_token
from google.auth.transport import requests
from typing import Any


from config import get_settings
from utils.token_utils import generate_sso_secret


settings = get_settings()


def get_user_info(token: str):
    user_info = id_token.verify_oauth2_token(
        token, requests.Request(), settings.google_cid)
    return user_info


def create_gsi_user_model(user_info: dict[str, Any]):
    hashed_password = generate_sso_secret()
    new_user = {
        "firstname": user_info["given_name"],
        "lastname": user_info["family_name"],
        "username": f"{user_info["family_name"].lower()}_{user_info["given_name"].lower()}",
        "email": user_info["email"],
        "password": hashed_password,
        "sso_user": True
    }
    return new_user
