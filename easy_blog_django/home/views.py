from django.views.generic import ListView

from ..posts.models import Post


class HomeView(ListView):

    template_name = "pages/home.html"

    paginate_by = 5

    posts = Post.objects.published()
    posts = posts.order_by('-created')
    queryset = posts