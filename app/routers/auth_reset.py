from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from httpx import get
from app import models, schemas
from app.database import get_db
from app.utils.connection_utils import get_connections
from sqlalchemy.orm import Session

from app.services.email_service import send_coded_email
from app.utils.hash_utils import hash_passwd
from app.utils.otp_utils import verify_otp, generate_otp
from app.utils.redis_utils import get_reset_token, store_reset_token
from app.utils.token_utils import generate_token_data, validate_reset_token

router = APIRouter(
    prefix="/forgot-password",
    tags=['Reset Password']
)


@router.post('/request-reset', status_code=status.HTTP_202_ACCEPTED)
def send_otp(payload: schemas.PayloadSchema, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter_by(
        email=payload.content).first()

    if found_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The email account provided is not associated with any user account.")

    try:
        otp = generate_otp()

        print(found_user.id, otp)
        store_reset_token(otp, str(found_user.id))

        send_coded_email(otp, 'otp.html', found_user.email, f"{found_user.firstname} {
            found_user.lastname}")

        return {'otp_sent': True}
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error in sending OTP email: {str(e)}") from e


@router.post('/verify-reset', status_code=status.HTTP_200_OK)
def verify_reset(payload: schemas.PayloadSchema, connections: tuple = Depends(get_connections)):
    # if isinstance(payload.content, int) is False:
    #     raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,
    #                         detail=f"Invalid payload data")

    if not verify_otp(str(payload.content)):
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Invalid OTP.")

    token, token_data = generate_token_data()

    db, redis_db = connections

    user_id = redis_db.hget(str(payload.content), 'sub')
    print(user_id)

    user_to_reset = db.query(models.User).filter(models.User.id == user_id).first()
    print(user_to_reset)

    store_reset_token(str(payload.content), str(user_to_reset.id), token_data)

    send_coded_email(token, 'reset.html', user_to_reset.email, str(payload.content)[::-1], f"{user_to_reset.firstname} {
        user_to_reset.lastname}")

    return redis_db.hgetall(str(payload.content))


@router.get('/reset/{reset_pin}', status_code=status.HTTP_200_OK)
def approve_reset_password(token: str, reset_pin: str):
    stored_token_data = get_reset_token(reset_pin[::-1])

    if stored_token_data == None:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Invalid reset link.")

    if not validate_reset_token(token, stored_token_data):
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"Invalid reset link.")

    return {'allowed': True}


@router.post('/reset/{reset_pin}', status_code=status.HTTP_201_CREATED)
def reset_password(token: str, reset_pin: str, payload: schemas.PayloadSchema, connections: tuple = Depends(get_connections)):
    db, redis_db = connections
    stored_token_data = get_reset_token(reset_pin[::-1])

    if payload is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"An error occured while trying to reset your password.")

    if stored_token_data == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid reset link.")

    if not validate_reset_token(token, stored_token_data):
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid reset link.")

    user_id = redis_db.hget(reset_pin[::-1], 'sub')

    if not user_id:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"An error occured while trying to reset your password.")

    new_password = hash_passwd(payload.content)

    query = db.query(models.User).filter_by(id=user_id)
    user = query.first()
    if user == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"An error occured while trying to reset your password.")

    query.update({models.User.password: new_password},
                 synchronize_session=False)
    db.commit()

    return {"Password reset successful."}
