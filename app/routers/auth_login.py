from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_db
from app.utils.auth_utils import verify_user
from app.utils.jwt_utils import generate_jwt

router = APIRouter(
    prefix='/login',
    tags=['Login']
)


@router.post('/', status_code=status.HTTP_200_OK)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        verified_user = verify_user(user_credentials, db)
        to_authorize = schemas.UserSchema.model_validate(verified_user)
        token = generate_jwt(to_authorize)

        return {
            "access_token": token,
            'token_type': "bearer"
        }
    except AttributeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.attr")
    except TypeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.type")
