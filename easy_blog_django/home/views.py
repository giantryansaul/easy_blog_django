from django.views.generic import ListView

from ..posts.models import Post


class LastPostMixIn(object):
    """
    Returns the most recent post. Only returns a single post.
    """
    # TODO: Use for jumbotron
    def get_context_data(self, **kwargs):
        context = super(LastPostMixIn, self).get_context_data(**kwargs)
        try:
            last_post = Post.objects.published()
            last_post = last_post.latest('created')
            context['last_post'] = last_post
            return context
        except Post.DoesNotExist, does_not_exist:
            raise does_not_exist
        except Post.MultipleObjectsReturned, multiple_objects_returned:
            raise multiple_objects_returned


class HomeView(LastPostMixIn, ListView):

    template_name = "pages/home.html"

    paginate_by = 5

    posts = Post.objects.published()
    posts = posts.order_by('-created')
    queryset = posts