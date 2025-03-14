from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


import schemas, models
from utils.hash_utils import hash_passwd


def create_user(user: schemas.UserSignup, db: Session):
    try:
        user.password = hash_passwd(user.password)
        new_user = models.User(**user.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as error:
        if 'username' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"A user with the username '{user.username}' already exists. Please choose a different username.")
        elif 'email' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"The email '{user.email}' is already registered.")
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Please contact support. Details: IntegrityError ")
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def create_sso_user(user_info_dict: dict, db: Session):
    try:
        user_info = schemas.UserSignup(**user_info_dict)
        new_sso_user = models.User(**user_info.dict())

        db.add(new_sso_user)
        db.commit()
        db.refresh(new_sso_user)
        return new_sso_user
    except IntegrityError as error:
        if 'username' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"A user with the username '{user_info.username}' already exists. Please choose a different username.")
        elif 'email' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"The email '{user_info.email}' is already registered.")
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Please contact support. Details: IntegrityError ")
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support. Details: {error}.")
