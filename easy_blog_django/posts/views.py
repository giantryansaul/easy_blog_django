from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post
from .forms import PostForm


class PostFormMixIn(object):
    """
    Common form methods
    """

    model = Post
    form_class = PostForm




class PostActionMixIn(object):
    """
    Overrides form_valid method to display a message after a form has been submitted.
    Returns user to the created or updated object.
    """

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PostActionMixIn, self).form_valid(form)

    def get_success_url(self):
        return reverse("posts:detail", kwargs={"slug": self.object.slug})


class PostSearchMixIn(object):
    """
    Allows the user to send a search query through GET.
    Uses the standard "q" attribute.
    """
    def get_queryset(self):

        queryset = super(PostSearchMixIn, self).get_queryset()

        q = self.request.GET.get("q")

        if q:
            return queryset.filter(title__icontains=q)

        return queryset


class PostListView(PostSearchMixIn, ListView):

    paginate_by = 20

    posts = Post.objects.published()
    posts = posts.order_by('-created')
    queryset = posts


class PostDetailView(DetailView):

    model = Post


class PostResultsView(PostDetailView):

    template_name = "posts/results.html"


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, PostFormMixIn, PostActionMixIn, UpdateView):

    permission_required = 'posts.change_post'
    raise_exception = True

    success_msg = "Post Updated"

    def get_form_kwargs(self):
        kwargs = super(PostFormMixIn, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, PostFormMixIn, PostActionMixIn, CreateView):

    permission_required = 'posts.add_post'
    raise_exception = True

    success_msg = "Post Created"

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs



