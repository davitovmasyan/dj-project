from typing import List, Tuple, Union

from django.template import loader

from .tasks import send_async_email

__all__ = (
    "send_email",
)


Recipient_s = Union[List[str], Tuple[str], str]


def render_body(template_name: str, context: dict = None) -> str:
    """
    Load template by given name, pass it context
    and render as a string.
    """
    template = loader.get_template(template_name)
    return template.render(context)


def send_email(
    subject: str,
    template_name: str,
    context: dict,
    to: Recipient_s,
    bcc: Recipient_s = None,
    cc: Recipient_s = None,
    reply_to: Recipient_s = None,
):

    if not to:
        return

    body = render_body(template_name, context)

    send_async_email.delay(
        subject=subject,
        body=body,
        to=[to],
        bcc=[bcc] if bcc else None,
        cc=[cc] if cc else None,
        reply_to=[reply_to] if reply_to else None,
    )
