from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from app import models, schemas
from app.database import get_db
from sqlalchemy.orm import Session

from app.services.email_service import send_otp_email

router = APIRouter(
    prefix="/reset-password",
    tags=['Reset Password']
)


@router.post('/')
def send_otp(payload: schemas.PayloadSchema, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter_by(
        username=payload.username).first()
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The username {payload.username} does not exist")

    username, domain = found_user.email.split('@')
    try:
        send_otp_email(found_user.email, f"{found_user.firstname} {found_user.lastname}")
        return {'status':f"OTP sent to the mailbox of {username[:4]}{"*" * len(username[4:])}@{domain} registered to the username provided."}
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error in sending OTP email: {str(e)}") from e
    
@router.get('/')
def reset_password():
    return {'reset'}
    



