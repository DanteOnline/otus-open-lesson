from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from otus_open_lesson.models import mock
from otus_open_lesson.cases import OtusOpenLessonTestCase


class SomeTest(TestCase):

    def test_mock(self):
        mock()
        self.assertTrue(True)


class TestHelloWorldAPI(OtusOpenLessonTestCase):

    def setUp(self):
        self.url = '/hello/'
        self.guest_client = self.client
        # self.auth_client = self.client

    def test_hello_status_code(self):
        response = self.guest_client.get(self.url)
        self.assertStatusCode(response, 200)

    def test_hello_status_content(self):
        response = self.guest_client.get(self.url)
        self.assertTrue('hello' in response.json())
        self.assertIn('hello', response.json())
        self.assertEqual(response.json(), {'hello': 'world'})
        self.assertDictEqual(response.json(), {'hello': 'world'})


class TestByWorldAPI(OtusOpenLessonTestCase):

    def setUp(self):
        self.url = '/by/'
        self.guest_client = self.client
        # self.auth_client = self.client

    def test_hello_status_code(self):
        response = self.guest_client.get(self.url)
        self.assertStatusCode(response, 200)

    def test_hello_status_content(self):
        response = self.guest_client.get(self.url)
        self.assertTrue('by' in response.json())
        self.assertIn('by', response.json())
        self.assertEqual(response.json(), {'by': 'by world'})

    def test_response(self):
        response = self.guest_client.get(self.url)
        self.assertResponse(response,
                            status_code=200,
                            )

# Параметризировать одинаковые
# Динамически передавать атрибуты запроса для проверки
