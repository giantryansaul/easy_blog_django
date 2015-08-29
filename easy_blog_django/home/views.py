from django.views.generic import TemplateView

from ..posts.models import Post


class LastPostMixIn(object):
    """
    Returns the most recent post. Only returns a single post.
    """
    #TODO: Use for jumbotron
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


class MostRecentPostsMixIn(object):
    """
    Returns the most recent posts up to the specified amount.
    easy_blog_django default is set to 10.
    """
    def get_context_data(self, **kwargs):
        context = super(MostRecentPostsMixIn, self).get_context_data(**kwargs)
        try:
            most_recent_posts = Post.objects.published()
            most_recent_posts = most_recent_posts.order_by('-created')[:10]
            context['most_recent_posts'] = most_recent_posts
            return context
        except Post.DoesNotExist, does_not_exist:
            raise does_not_exist


class HomeView(LastPostMixIn, MostRecentPostsMixIn, TemplateView):
    template_name = "pages/home.html"

