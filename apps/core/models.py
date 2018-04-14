from django.db import models


__all__ = (
    "AbstractDate",
)


class AbstractDate(models.Model):
    "Created and Modified datetime fields for models"
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
