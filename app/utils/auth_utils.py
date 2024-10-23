from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated, Any, Callable
import jwt


import models
from database import get_db
from utils.hash_utils import validate_passwd


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def validate_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        if '@' in user_credentials.username:
            valid_user = db.query(models.User).filter(
                models.User.email == user_credentials.username).first()
        else:
            valid_user = db.query(models.User).filter(
                models.User.username == user_credentials.username).first()

        if valid_user == None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Incorrect username or password.")

        valid_passwd = validate_passwd(
            user_credentials.password, valid_user.password.encode('utf8'))

        if not valid_passwd:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Incorrect username or password.")

        return valid_user
    except AttributeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def validate_sso_user(user_credentials: dict[str, Any], db: Session = Depends(get_db)):

    try:
        valid_user = db.query(models.User).filter(
            models.User.email == user_credentials["email"]).first()

        if valid_user == None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Incorrect username or password. Do you have an account? If not, create one here!")
        return valid_user
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)] | str, validator: Callable[[str], Any], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Credentials.",
        headers={'WWW-Authenticate': "Bearer"}
    )

    try:
        payload = validator(token)
        user_id = payload.get('sub')

        if user_id is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception

    # filter(models.User.id == user_id).first()
    user = db.query(models.User).get(user_id)
    if user is None:
        raise credentials_exception

    return user
