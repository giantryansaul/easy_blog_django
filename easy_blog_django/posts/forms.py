from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description', 'tags', 'published', 'author']

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(PostForm, self).__init__(*args, **kwargs)
