from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.utils import generate_jwt, verify_user

router = APIRouter(
  prefix='/login',
  tags=['Login']
)

@router.post('/', status_code=status.HTTP_200_OK)
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # validate user
    verified_user = verify_user(user_credentials, db)
    # authorize login
    if verified_user != None:
        to_authorize = schemas.UserSchema.from_orm(verified_user)
        token = generate_jwt(to_authorize)

    return {
      "access_token": token,
      'token_type': "bearer"
    }
