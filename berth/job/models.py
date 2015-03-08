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

    def build(self):
        self.state = constants.BUILD_STATUS_QUEUED
        self.save(update_fields=['state'])

        from berth.job import tasks
        chain = (tasks.checkout.s(self.pk) | tasks.commence_build.s())
        return chain.apply_async()
