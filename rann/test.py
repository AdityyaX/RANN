from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class FooTest(TestCase):
    def test_create(self):
        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
