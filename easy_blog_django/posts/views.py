from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostResultsView(PostDetailView):
    template_name = "posts/results.html"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post

    def get_success_url(self):
        return reverse("posts:detail", kwargs={"pk": self.object.pk})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'description')

    def form_valid(self, form):
        return super(PostCreateView, self).form_valid(form)