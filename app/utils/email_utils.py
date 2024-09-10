from typing import Dict
from jinja2 import Environment, PackageLoader, TemplateNotFound, select_autoescape
from app.utils.otp_utils import generate_otp

def generate_email_content(template_name: str = 'otp.html') -> str:
    """
    Generate email content using a Jinja2 template and OTP.

    Args:
        template_name (str): Name of the template file. Defaults to 'otp.html'.

    Returns:
        str: Rendered email content.

    Raises:
        RuntimeError: If template is not found or rendering fails.
    """
    try:
        otp = generate_otp()
        
        env = Environment(
            loader=PackageLoader('app', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        template = env.get_template(template_name)
        context: Dict[str, str] = {'OTP': otp}
        
        return template.render(context)
    
    except TemplateNotFound as e:
        raise RuntimeError(f"Template '{template_name}' not found") from e
    except Exception as e:
        raise RuntimeError(f"Failed to generate email content: {str(e)}") from e