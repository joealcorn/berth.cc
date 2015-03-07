from django.db import models

from berth.job import constants
from berth.insert_returning import InsertReturningManager
from berth.models import Model


class Job(Model):
    project = models.ForeignKey('project.Project')
    state = models.IntegerField(choices=constants.BUILD_STATE_CHOICES)
    number = models.IntegerField()

    objects = InsertReturningManager()

    class Meta:
        unique_together = (
            ('project', 'number'),
        )
