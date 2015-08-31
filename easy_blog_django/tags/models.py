from django.db import models

from ..core.models import TimeStampedModel


class TagManager(models.Manager):

    use_for_related_fields = True

    def partial_name(self, name, **kwargs):
        return self.filter(name__iexact=name, **kwargs)

    def exact_name(self, name, **kwargs):
        return self.filter(name__exact=name, **kwargs)


class Tag(TimeStampedModel):
    """
    Tags for posts.
    """
    name = models.CharField(max_length=255)
    author = models.BooleanField(default=False)

    objects = TagManager()

    def __str__(self):
        return self.name