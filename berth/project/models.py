from django.db import models

from berth.models import Model


class Project(Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    repo_url = models.CharField(max_length=256)
    owner = models.ForeignKey('user.User')
