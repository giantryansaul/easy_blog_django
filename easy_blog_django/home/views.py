from django.views.generic import TemplateView

from ..posts.models import Post


class LastPostMixIn(object):

    def get_context_data(self, **kwargs):
        context = super(LastPostMixIn, self).get_context_data(**kwargs)
        last_post = Post.objects.earliest('created')
        context['last_post'] = last_post


class HomeView(LastPostMixIn, TemplateView):
    template_name = "pages/home.html"

