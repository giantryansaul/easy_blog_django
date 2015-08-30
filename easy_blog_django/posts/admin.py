from django.contrib import admin

from .models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(Post, PostAdmin)