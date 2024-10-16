from typing import Dict, Optional
from jinja2 import Environment, PackageLoader, TemplateNotFound, select_autoescape


def generate_email_content(data: str, template: str, pin: Optional[str]) -> str:
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

        env = Environment(
            loader=PackageLoader('app', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        
        template = env.get_template(template)
        context: Dict[str, str] = {'data': data, 'pin': pin}
        
        return template.render(context)
    
    except TemplateNotFound as e:
        raise RuntimeError(f"Template '{template}' not found") from e
    except Exception as e:
        raise RuntimeError(f"Failed to generate email content: {str(e)}") from e