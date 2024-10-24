from typing import Any
import requests
from urllib.parse import urlencode


from config import get_settings
from utils.token_utils import generate_sso_secret


settings = get_settings()


def get_access_token(code: str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.linkedin_cid,
        'client_secret': settings.linkedin_secret,
        'redirect_uri': settings.linkedin_redirect_uri,
    }

    encoded_params = urlencode(params)

    response = requests.post(
        settings.linkedin_access_token_uri, data=encoded_params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_linkedin_user_model(token_data: dict[str, Any]):
    headers = {
        'Authorization': f"Bearer {token_data['access_token']}"
    }

    response = requests.get(
        settings.linkedin_user_info_uri, headers=headers)

    user_data = response.json()

    hashed_password = generate_sso_secret()
    new_user = {
        "firstname": user_data["given_name"],
        "lastname": user_data["family_name"],
        "username": user_data['name'].lower().replace(' ', "_"),
        "email": user_data["email"],
        "password": hashed_password,
        "sso_user": True
    }

    return new_user

