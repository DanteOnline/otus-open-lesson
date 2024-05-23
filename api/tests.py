from django.test import TestCase
from otus_open_lesson.models import mock


class SomeTest(TestCase):

    def test_mock(self):
        mock()
        self.assertTrue(True)
