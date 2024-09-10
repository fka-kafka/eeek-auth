from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated
import jwt


from app import models
from app.database import get_db
from app.utils.hash_utils import verify_passwd
from app.utils.jwt_utils import verify_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


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
