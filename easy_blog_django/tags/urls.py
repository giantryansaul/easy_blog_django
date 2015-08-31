from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r"^$",
        view=views.TagListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.TagDetailView.as_view(),
        name="detail"
    ),
]