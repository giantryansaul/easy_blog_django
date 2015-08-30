from django.db import models
from django.conf import settings

from ..core.models import TimeStampedModel
from ..tags.models import Tag


class PostManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(published__exact=True, **kwargs)


class Post(TimeStampedModel):
    """
    Model for Posts.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tag)

    objects = PostManager()

    def __str__(self):
        return self.title


