from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils import password_hasher

router = APIRouter(
    prefix='/signup',
    tags=['Signup']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreated)
def signup(user: schemas.UserSignup, db: Session = Depends(get_db)):
    try:
        user.password = password_hasher(user.password)
        new_user = models.User(**user.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        created_user = schemas.UserCreated(id=new_user.user_id, username=new_user.username, date_created=new_user.date_created)

        return created_user
    except IntegrityError as error:
        if 'username' in error.args[0]:
            raise HTTPException(status.HTTP_409_CONFLICT, detail=f"A user with the username '{user.username}' already exists. Please choose a different username.")

        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Please contact support.")

    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Please contact support.")

    # TODO: generate token
