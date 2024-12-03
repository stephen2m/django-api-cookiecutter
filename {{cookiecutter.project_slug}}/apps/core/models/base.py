from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract base model that automatically maintains created and modified timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True