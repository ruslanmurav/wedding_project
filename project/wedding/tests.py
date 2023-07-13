from django.test import TestCase
from django.urls import reverse


class MainViewTestCase(TestCase):

    def test_view(self):
        path = reverse('main')
        response = self.client.get(path)

