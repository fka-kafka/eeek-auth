from fastapi import APIRouter, HTTPException, Response, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


import schemas
from database import get_db
from config import get_settings
from utils.auth_utils import validate_sso_user, validate_user
from utils.jwt_utils import generate_session_token
from services.google_sso_service import get_user_info, create_gsi_user_model
from services.linkedin_sso_service import get_access_token, create_linkedin_user_model


settings = get_settings()

router = APIRouter(
    prefix='/login',
    tags=['Login']
)


@router.post('/', status_code=status.HTTP_200_OK)
def login(response: Response, user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        verified_user = validate_user(user_credentials, db)
        to_authorize = schemas.UserSchema.model_validate(verified_user)
        token = generate_session_token(to_authorize)

        response.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            secure=True,
            samesite='strict',
            domain='localhost',
            max_age=86400
        )

        return {
            "status": "login succesful",
        }
    except AttributeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.attr")
    except TypeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.type")


@router.post('-sso/{provider}', status_code=status.HTTP_200_OK)
def sso_login(response: Response, payload: schemas.PayloadSchema, provider: str, db: Session = Depends(get_db)):
    try:
        if provider == 'linkedin':
            token_data = get_access_token(payload.content)
            user_info = create_linkedin_user_model(token_data)
        elif provider == 'google':
            user_data = get_user_info(payload.content)
            user_info = create_gsi_user_model(user_data)

        verified_user = validate_sso_user(user_info, db)
        to_authorize = schemas.UserSchema.model_validate(verified_user)
        token = generate_session_token(to_authorize)

        response.set_cookie(
            key='access_token',
            value=token,
            httponly=True,
            secure=True,
            samesite='strict',
            domain='localhost',
            max_age=86400
        )

        return {
            "status": "login succesful",
        }
    except AttributeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.attr")
    except TypeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Please contact support.type")
