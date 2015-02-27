from django.test import TestCase
from exam import Exam, before
from rest_framework.test import APITestCase

from .fixtures import Fixtures


class BaseTestCase(Fixtures, Exam):
    pass


class TestCase(TestCase, BaseTestCase):
    pass


class APITestCase(APITestCase, BaseTestCase):
    pass
