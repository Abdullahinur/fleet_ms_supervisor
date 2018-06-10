from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

# Create your tests here.
from .models import Sacco
from .views import home


class HomeTests(TestCase):
    # Test to make sure '/' url path returns home view
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


# class SaccoTestClass(TestCase):
#
#     # Set up method
#     def setUp(self):
#         self.sacco = Sacco(name='test sacco', description='test descriptions')
#
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.sacco, Sacco))
#
#     def tearDown(self):
#         self.sacco.delete()
