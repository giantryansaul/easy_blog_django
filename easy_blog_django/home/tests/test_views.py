from django.test import RequestFactory
from django.core.exceptions import ObjectDoesNotExist

from test_plus.test import TestCase

from ..views import (
    HomeView,
)


class TestHomePage(TestCase):
    """
    Test for home page elements.
    """

    def test_home_page_without_posts(self):
        view = HomeView()
        self.factory = RequestFactory()
        request = self.factory.get('/')
        view.request = request
        with self.assertRaises(ObjectDoesNotExist):
            view.get_context_data()

    #TODO: Unit tests for single post returned and multiple posts returned