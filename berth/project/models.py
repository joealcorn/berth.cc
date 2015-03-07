from os import path

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from berth.models import Model


class Project(Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    repo_url = models.CharField(max_length=256)
    owner = models.ForeignKey('user.User', editable=False)

    def get_checkout_directory(self):
        directory = '%s-%s-%s' % (self.owner_id, self.id, self.name)
        return path.join(settings.REPO_CLONE_DIR, directory)

    def get_absolute_url(self):
        return reverse('update-project', args=[self.pk])
