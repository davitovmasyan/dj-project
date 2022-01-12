from typing import List

import celery

from django.core.mail import EmailMessage

from project.celery import app

__all__ = (
    "send_async_email",
)


@app.task(bind=True)
def send_async_email(
    task_object: celery.Task,
    subject: str,
    body: str,
    to: List[str],
    bcc: List[str] = None,
    cc: List[str] = None,
    reply_to: List[str] = None,
):
    "Task for sending emails asynchronously"
    email = EmailMessage(
        subject=subject,
        body=body,
        to=to,
        bcc=bcc,
        cc=cc,
        reply_to=reply_to,
    )

    # Setting main content
    email.content_subtype = "html"

    email.send()
