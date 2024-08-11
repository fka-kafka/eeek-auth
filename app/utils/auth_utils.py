import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models
from app.database import get_db


def hash_passwd(passwd: str):
    try:
        hashed_passwd_bytes = bcrypt.hashpw(
            passwd.encode('utf-8'), bcrypt.gensalt(13))
        hashed_passwd = hashed_passwd_bytes.decode('utf-8')
        return hashed_passwd
    except TypeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def verify_passwd(passwd: str, hashed_passwd: bytes):
    try:
        verified_passwd = bcrypt.checkpw(passwd.encode('utf-8'), hashed_passwd)
        return verified_passwd
    except TypeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def verify_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
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

        valid_passwd = verify_passwd(
            user_credentials.password, valid_user.password.encode('utf8'))

        if not valid_passwd:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Incorrect username or password.")

        return valid_user
    except AttributeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


