from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve

# Create your tests here.
from .models import Sacco
from .views import home, sacco


class HomeTests(TestCase):
    # Test to make sure '/' url path returns home view
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class SaccoTestClass(TestCase):
    def setUp(self):
        Sacco.objects.create(id='1', name='test sacco',
                             description='test description', sacco_logo='test.png')

    def test_sacco_view_success_status_code(self):
        url = reverse('sacco', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_sacco_view_not_found_status_code(self):
        url = reverse('sacco', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_sacco_url_resolves_sacco_view(self):
        view = resolve('/saccos/1/')
        self.assertEquals(view.func, sacco)
