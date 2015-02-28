from django.core.urlresolvers import reverse_lazy

from berth.utils.test import APITestCase
from berth.user.serializers import CreateUserSerializer


class TestCreateUserView(APITestCase):

    endpoint = reverse_lazy('create-user')

    def test_success(self):
        data = {
            'email': 'joe@example.org',
            'password': 'password',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 201

    def test_short_password(self):
        data = {
            'email': 'joe@example.org',
            'password': 'short',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 400
        assert 'password' in resp.data

    def test_user_exists(self):
        user = self.create_user()
        data = {
            'email': user.email,
            'password': 'password',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 400
        assert 'email' in resp.data


class TestSignInView(APITestCase):

    endpoint = reverse_lazy('sign-in')

    def test_correct_password(self):
        user = self.create_user()
        data = {
            'email': user.email,
            'password': 'password',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 200

    def test_wrong_password(self):
        user = self.create_user(password='test')
        data = {
            'email': user.email,
            'password': 'incorrect',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 400
        assert 'password' in resp.data

    def test_nonexistant_email(self):
        data = {
            'email': 'blahblah@berth.cc',
            'password': 'password',
        }

        resp = self.client.post(self.endpoint, data)
        assert resp.status_code == 400
        assert 'email' in resp.data
