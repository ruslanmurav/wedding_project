from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse


class MainViewTestCase(TestCase):

    def test_view(self):
        path = reverse('main')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Главная страница')
        self.assertTemplateUsed(response, 'wedding/main.html')
