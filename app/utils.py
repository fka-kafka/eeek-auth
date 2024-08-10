import bcrypt

def password_hasher(passwd: str):
    hashed_passwd_bytes = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt(13))
    hashed_passwd = hashed_passwd_bytes.decode('utf-8')
    return hashed_passwd

def password_verifier(passwd: str, hashed_passwd: bytes):
    verified_passwd = bcrypt.checkpw(passwd.encode('utf-8'), hashed_passwd)
    return verified_passwd
