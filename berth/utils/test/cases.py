from django.test import TestCase
from exam import Exam, before
from rest_framework.test import APITestCase

from .fixtures import Fixtures


class BaseTestCase(Fixtures):
    pass


class TestCase(Exam, TestCase, BaseTestCase):
    pass


class APITestCase(Exam, APITestCase, BaseTestCase):
    pass
