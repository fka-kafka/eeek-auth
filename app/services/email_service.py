from email.message import EmailMessage
from email.headerregistry import Address
from smtplib import SMTP, SMTPException
from typing import Optional

from app.utils.email_utils import generate_email_content
from app.config import get_settings

settings = get_settings()


def send_coded_email(code: str, template: str, to_email: str, pin: Optional[str] = '', to_name: Optional[str] = None) -> None:
    """
    Send an OTP email to the specified recipient.

    Args:
        to_email (str): The recipient's email address.
        to_name (Optional[str]): The recipient's name. Defaults to None.

    Raises:
        RuntimeError: If there's an error in sending the email.
    """
    try:
        content = generate_email_content(code, template, pin)

        otp_email = EmailMessage()
        otp_email['Subject'] = "Your eeek! password reset verification code"
        otp_email['From'] = Address('eeek!-auth', settings.smtp_username.split(
            '@')[0], settings.smtp_username.split('@')[1])
        otp_email['To'] = Address(
            to_name or to_email, to_email.split('@')[0], to_email.split('@')[1])

        otp_email.set_content(content, subtype='html')

        with SMTP(settings.smtp_server, settings.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(settings.smtp_username, settings.smtp_password)
            smtp.send_message(otp_email)

    except SMTPException as e:
        raise RuntimeError(f"Failed to send OTP email: {str(e)}") from e
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error in sending OTP email: {str(e)}") from e
