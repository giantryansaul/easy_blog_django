from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify

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
    tags = models.ManyToManyField(Tag, blank=True)
    header_image = models.ImageField(upload_to='headers', default='default_image.jpg')

    slug = models.SlugField(unique=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Post, self).save()
