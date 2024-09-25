from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


from app import schemas, models
from app.utils.hash_utils import hash_passwd
from app.utils.token_utils import generate_sso_secret


def create_user(user: schemas.UserSignup, db: Session):
    try:
        user.password = hash_passwd(user.password)
        new_user = models.User(**user.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as error:
        print(error)
        if 'username' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"A user with the username '{
                                user.username}' already exists. Please choose a different username.")
        elif 'email' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"The email '{
                                user.email}' is already registered.")
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Please contact support. Details: IntegrityError ")
    except Exception as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def create_sso_user(user_info: dict[str, Any], db: Session):
    try:
        new_sso_user = models.User(**user_info)

        db.add(new_sso_user)
        db.commit()
        db.refresh(new_sso_user)
        return new_sso_user
    except IntegrityError as error:
        print(error)
        if 'username' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"A user with the username '{
                                user_info.username}' already exists. Please choose a different username.")
        elif 'email' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"The email '{
                                user_info.email}' is already registered.")
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Please contact support. Details: IntegrityError ")
    except Exception as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")
