import pyotp


BASE32_SECRET = pyotp.random_base32()
TOTP = pyotp.TOTP(BASE32_SECRET, interval=4)

def generate_otp() -> str:
    """Generate a new OTP."""
    try:
        return TOTP.now()
    except Exception as e:
        raise RuntimeError(f"Failed to generate OTP: {str(e)}") from e

def verify_otp(otp: str) -> bool:
    """Verify the provided OTP."""
    try:
        return TOTP.verify(otp)
    except Exception as e:
        raise RuntimeError(f"Failed to verify OTP: {str(e)}") from e
