from typing import Annotated
import jwt
from fastapi import Depends, HTTPException, status
from datetime import UTC, datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from app import models, schemas
from app.config import get_settings
from app.database import get_db

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


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials.",
        headers={'WWW-Authenticate': "Bearer"}
    )

    try:
        payload = verify_jwt(token)
        user_id = payload.get('sub')

        if user_id is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    user = db.query(models.User).get(user_id)  # filter(models.User.id == user_id).first() 
    if user is None:
        raise credentials_exception
    
    return user
