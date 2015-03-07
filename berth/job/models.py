from django.db import models

from berth.job import constants, insert_returning
from berth.models import Model


class Job(Model):
    objects = insert_returning.JobManager()

    project = models.ForeignKey('project.Project')
    state = models.IntegerField(choices=constants.BUILD_STATE_CHOICES)
    number = models.IntegerField()

    def _do_insert(self, manager, *a, **kw):
        '''
        This is required as part of the `insert...returning` hack.
        All it does is replaces the base manager in the call
        with the JobManager, which does the rest of the work.
        '''
        return super(Job, self)._do_insert(self.__class__.objects, *a, **kw)

    class Meta:
        unique_together = (
            ('project', 'number'),
        )
