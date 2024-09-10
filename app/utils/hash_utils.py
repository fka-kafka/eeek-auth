import bcrypt
from fastapi import HTTPException, status


def hash_passwd(passwd: str):
    try:
        hashed_passwd_bytes = bcrypt.hashpw(
            passwd.encode('utf-8'), bcrypt.gensalt(13))
        hashed_passwd = hashed_passwd_bytes.decode('utf-8')
        return hashed_passwd
    except TypeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def verify_passwd(passwd: str, hashed_passwd: bytes):
    try:
        verified_passwd = bcrypt.checkpw(passwd.encode('utf-8'), hashed_passwd)
        return verified_passwd
    except TypeError as error:
        print(error)
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")

