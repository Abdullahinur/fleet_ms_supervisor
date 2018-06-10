from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from .models import Sacco


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class SaccoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.sacco = Sacco(name='test sacco', description='test descriptions')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sacco, Sacco))

    def tearDown(self):
        self.sacco.pop()
