from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests


from app import schemas
from app.database import get_db
from app.config import get_settings
from app.utils.auth_utils import validate_sso_user, validate_user
from app.utils.jwt_utils import generate_session_token
from app.services.google_sso_service import get_user_info, create_gsi_user_model
from app.services.linkedin_sso_service import get_access_token, create_linkedin_user_model


settings = get_settings()

router = APIRouter(
    prefix='/login',
    tags=['Login']
)


@router.post('/', status_code=status.HTTP_200_OK)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        verified_user = validate_user(user_credentials, db)
        to_authorize = schemas.UserSchema.model_validate(verified_user)
        token = generate_session_token(to_authorize)

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


@router.post('-sso/{provider}', status_code=status.HTTP_200_OK)
def sso_login(payload: schemas.PayloadSchema, provider: str, db: Session = Depends(get_db)):
    user_credentials = id_token.verify_oauth2_token(
        payload.content, requests.Request(), settings.client_id)
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
