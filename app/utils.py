import bcrypt
import jwt
from os import read
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

def hash_passwd(passwd: str):
    hashed_passwd_bytes = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt(13))
    hashed_passwd = hashed_passwd_bytes.decode('utf-8')
    return hashed_passwd

def verify_passwd(passwd: str, hashed_passwd: bytes):
    verified_passwd = bcrypt.checkpw(passwd.encode('utf-8'), hashed_passwd)
    return verified_passwd

def verify_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    if '@' in user_credentials.username:
        valid_user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    else:
        valid_user = db.query(models.User).filter(models.User.username == user_credentials.username).first()

    if valid_user == None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password.")

    valid_passwd = verify_passwd(user_credentials.password, valid_user.password.encode('utf8'))

    if not valid_passwd:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password.")

    return valid_user

def generate_jwt(to_authorize: schemas.UserSchema):
    with open('/home/brandon/papyrus/eeek-auth/app/.keys/pkey.pem', 'rb') as key_file:
        private_key = key_file.read()

    ALGORITHM = 'RS256'
    payload = {
        'user_id': str(to_authorize.id),
        'username': to_authorize.username,
        'created': str(to_authorize.date_created)
    }
    token = jwt.encode(payload, private_key, algorithm=ALGORITHM)
    return token

def verify_jwt(token):
    with open('/home/brandon/papyrus/eeek-auth/app/.keys/pub_key.pem', 'rb') as key_file:
        public_key = key_file.read()

    ALGORITHM = 'RS256'

    decoded = jwt.decode(token, public_key, algorithms=[ALGORITHM])
    print(decoded)
    return decoded
