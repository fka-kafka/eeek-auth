import string
import secrets
from secrets import token_urlsafe
from datetime import UTC, datetime, timedelta, timezone
from utils.hash_utils import generate_token_hash, hash_passwd, validate_token_hash
from config import get_settings

settings = get_settings()


def generate_token_data():
    expiry = datetime.now(
        UTC) + timedelta(seconds=int(settings.reset_token_expiry_seconds))

    token = token_urlsafe(64)

    token_hash = generate_token_hash(token)

    token_data = {
        'hash': token_hash,
        'exp': str(expiry)
    }
    try:
        return token, token_data
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error while generating reset token.") from e


def validate_reset_token(token: str, token_data: dict[str, str]):
    if not validate_token_hash(token, token_data['hash']):
        return False

    # Parse the expiration time from token_data
    expiry = datetime.fromisoformat(token_data['exp'])

    # Compare with current UTC time
    if datetime.now(timezone.utc) > expiry:
        return False

    return True


def generate_sso_secret():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(12))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1):
            break
    
    sso_secret = hash_passwd(password)
    return sso_secret
