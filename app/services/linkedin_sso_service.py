from typing import Any
import requests
from urllib.parse import urlencode


from app.config import get_settings
from app.utils.token_utils import generate_sso_secret


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
        'https://www.linkedin.com/oauth/v2/accessToken', data=encoded_params, headers=headers)

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def create_linkedin_user_model(token_data: dict[str, Any]):
    headers = {
        'Authorization': f'Bearer {token_data['access_token']}'
    }

    response = requests.get(
        'https://api.linkedin.com/v2/userinfo', headers=headers)

    user_data = response.json()

    print(user_data)

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

