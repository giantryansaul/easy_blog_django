from django.db import models

from ..core.models import TimeStampedModel


class PostManager(models.Manager):

    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(published__exact=True, **kwargs)


class Post(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    # TODO: Add author field
    #author = models.ForeignKey(User, blank=True, null=True)

    # Add custom model manager
    objects = PostManager()