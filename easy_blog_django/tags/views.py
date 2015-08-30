from django.views.generic import ListView

from ..tags.models import Tag


class TagListView(ListView):
    model = Tag