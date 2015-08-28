from django.views.generic import TemplateView

from ..posts.models import Post


class LastPostMixIn(object):

    def get_context_data(self, **kwargs):
        context = super(LastPostMixIn, self).get_context_data(**kwargs)
        try:
            last_post = Post.objects.latest('created')
            context['last_post'] = last_post
            return context
        except Post.DoesNotExist, does_not_exist:
            raise does_not_exist
        except Post.MultipleObjectsReturned, multiple_objects_returned:
            raise multiple_objects_returned


class HomeView(LastPostMixIn, TemplateView):
    template_name = "pages/home.html"

