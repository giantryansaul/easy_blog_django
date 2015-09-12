from django.views.generic import ListView, DetailView, CreateView

from .models import Tag
from ..posts.models import Post


class PostsByTagNameMixIn(object):
    """
    Returns posts related to the tag name.
    """
    def get_context_data(self, **kwargs):
        context = super(PostsByTagNameMixIn, self).get_context_data(**kwargs)
        try:
            posts = Post.objects.published()
            posts = posts.filter(tags=self.get_object())
            context['posts'] = posts
            return context
        except Post.DoesNotExist:
            pass


class TagListView(ListView):

    model = Tag


class TagDetailView(PostsByTagNameMixIn, DetailView):

    model = Tag