import pyotp


BASE32_SECRET = pyotp.random_base32()
totp = pyotp.TOTP(BASE32_SECRET, interval=900)

def generate_otp() -> str:
    """Generate a new OTP."""
    try:
        return totp.now()   
    except Exception as e:
        raise RuntimeError(f"Failed to generate OTP: {str(e)}") from e

def verify_otp(otp: str) -> bool:
    """Verify the provided OTP."""
    try:
        return totp.verify(otp)
    except Exception as e:
        raise RuntimeError(f"Failed to verify OTP: {str(e)}") from e
