from berth.utils.test import TestCase
from berth.user.serializers import CreateUserSerializer


class TestCreateUserSerializer(TestCase):

    def test_password_minlength(self):
        data = {
            'email': 'joe@example.org',
            'password': '1' * 5,
        }

        serializer = CreateUserSerializer(data=data)
        assert serializer.is_valid() is False
        assert 'password' in serializer.errors

        data['password'] = '1' * 6
        serializer = CreateUserSerializer(data=data)
        assert serializer.is_valid()
