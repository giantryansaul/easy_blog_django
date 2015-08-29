from django.db import models
from django.conf import settings

from ..core.models import TimeStampedModel


class PostManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(published__exact=True, **kwargs)


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    # Add custom model manager
    objects = PostManager()