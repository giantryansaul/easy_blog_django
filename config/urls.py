# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .settings.common import INSTALLED_APPS

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("easy_blog_django.users.urls", namespace="users")),


    # Blog apps
    url(r'^posts/', include('easy_blog_django.posts.urls', namespace="posts")),
    url(r'^tags/', include('easy_blog_django.tags.urls', namespace="tags")),
    url(r'^$', include('easy_blog_django.home.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'allauth' in INSTALLED_APPS:
    urlpatterns.append(url(r'^accounts/', include('allauth.urls')))

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
