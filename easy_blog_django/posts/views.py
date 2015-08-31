from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import Post


class PostActionMixIn(object):

    fields = ['title', 'description', 'tags', 'published', 'slug', ]

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PostActionMixIn, self).form_valid(form)


class PostListView(ListView):

    model = Post


class PostDetailView(DetailView):

    model = Post


class PostResultsView(PostDetailView):

    template_name = "posts/results.html"


class PostUpdateView(LoginRequiredMixin, PostActionMixIn, UpdateView):
    #TODO: Add security layer so only admins can edit.

    model = Post

    success_msg = "Post Updated"
    def get_success_url(self):
        return reverse("posts:detail", kwargs={"slug": self.object.slug})


class PostCreateView(LoginRequiredMixin, PostActionMixIn, CreateView):

    model = Post

    success_msg = "Post Created"
    #
    # def form_valid(self, form):
    #     return super(PostCreateView, self).form_valid(form)


