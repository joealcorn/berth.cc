from django.db import IntegrityError
from rest_framework import generics, response

from berth.user.models import User
from berth.user.serializers import CreateUserSerializer


class CreateUser(generics.CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer

    def post(self, *a, **kw):
        try:
            return self.create(*a, **kw)
        except IntegrityError:
            return response.Response({'email': ['User already exists']}, 400)

    def perform_create(self, serializer):
        password = serializer.data.pop('password')
        user = User(**serializer.data)
        user.set_password(password)
        user.save()
        return user
