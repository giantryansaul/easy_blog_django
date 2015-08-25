from django.db import models

from ..core.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # TODO: Add author field
    #createdBy = models.ForeignKey(User, blank=True, null=True)