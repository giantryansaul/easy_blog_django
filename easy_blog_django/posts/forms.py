from django import forms

from .models import Post

from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'tags',
            'published',
            'author',
            'header_image',
        ]