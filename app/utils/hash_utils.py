import bcrypt
from hashlib import sha256
from fastapi import HTTPException, status


def hash_passwd(passwd: str):
    try:
        hashed_passwd_bytes = bcrypt.hashpw(
            passwd.encode('utf-8'), bcrypt.gensalt(13))
        hashed_passwd = hashed_passwd_bytes.decode('utf-8')
        return hashed_passwd
    except TypeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def validate_passwd(passwd: str, hashed_passwd: bytes):
    try:
        verified_passwd = bcrypt.checkpw(passwd.encode('utf-8'), hashed_passwd)
        return verified_passwd
    except TypeError as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Please contact support. Details: Server Error.")


def generate_token_hash(token: str):
    the_hash = sha256(token.encode())
    return the_hash.hexdigest()


def validate_token_hash(token: str, token_hash: str):
    if sha256(token.encode()).hexdigest() != token_hash:
        return False
    return True
