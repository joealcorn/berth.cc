from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from berth.models import Model


class User(AbstractBaseUser, Model):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    objects = BaseUserManager()
