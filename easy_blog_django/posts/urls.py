# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r"^$",
        view=views.PostListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^add/$",
        view=views.PostCreateView.as_view(),
        name="add"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.PostDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/results/$",
        view=views.PostResultsView.as_view(),
        name="results"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/update/$",
        view=views.PostUpdateView.as_view(),
        name="update"
    ),

]