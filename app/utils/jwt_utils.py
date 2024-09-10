import jwt
from fastapi import HTTPException, status
from datetime import UTC, datetime, timedelta
from fastapi.security import OAuth2PasswordBearer


from app import schemas
from app.config import get_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

settings = get_settings()


def generate_jwt(to_authorize: schemas.UserSchema):
    if not to_authorize:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Please contact support.")

    try:
        with open(f'{settings.priv_key_path}', 'rb') as key_file:
            private_key = key_file.read()

        expiry = datetime.now(
            UTC) + timedelta(minutes=int(settings.access_token_expiry_minutes))

        payload = {
            'sub': str(to_authorize.id),
            'name': to_authorize.username,
            'exp': expiry,
            'created': str(to_authorize.date_created)
        }

        token = jwt.encode(payload, private_key, algorithm=settings.algorithm)

        return token
    except FileNotFoundError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support.")
    except Exception as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support.")


def verify_jwt(token: str):
    if not token:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Please contact support.")

    try:
        with open(f'{settings.pub_key_path}', 'rb') as key_file:
            public_key = key_file.read()

        decoded = jwt.decode(token, public_key, algorithms=[
                             settings.algorithm])
        print(decoded)
        return decoded
    except FileNotFoundError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support.")
    except Exception as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support.")   


