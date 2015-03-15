
from os import path

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from berth.models import Model
from berth.project import constants


class Project(Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    repo_url = models.CharField(max_length=256)
    owner = models.ForeignKey('user.User', editable=False)
    subdomain = models.CharField(max_length=128, unique=True)
    repo_identifier = models.IntegerField()
    repo_source = models.PositiveSmallIntegerField(choices=constants.REPO_SOURCE_CHOICES)

    class Meta:
        unique_together = (
            ('repo_identifier', 'repo_source'),
        )

    def get_checkout_directory(self):
        '''
        Returns the directory code checkouts live
        '''
        directory = '%s-%s-%s' % (self.owner_id, self.id, self.name)
        return path.join(settings.REPO_CLONE_DIR, directory)

    def get_artifact_directory(self):
        '''
        Returns the directory build artifacts are placed in
        during builds
        '''
        directory = '%s-%s' % (self.owner_id, self.id)
        return path.join(settings.ARTIFACT_DIR, directory)

    def get_serve_directory(self):
        '''
        Returns the directory builds should be served from
        '''
        return path.join(settings.SERVE_DIR, self.slug)

    def get_absolute_url(self):
        return reverse('update-project', args=[self.pk])
