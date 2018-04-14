import os
import uuid

from django.db import models
from django.contrib.auth.models import User


__all__ = (
    "Account",
)


def avatar_upload_path(profile, filename: str) -> str:
    extension = os.path.splitext(filename)[1]
    return os.path.join(
        "upload/accounts/avatars",
        "{0}{1}".format(uuid.uuid4().hex, extension)
    )


class Account(models.Model):
    "Account for registered users of website."
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        blank=True, null=True,
        upload_to=avatar_upload_path,
    )
    birthday = models.DateField(null=True, blank=True)
