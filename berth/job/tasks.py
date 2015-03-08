from berth.job import constants
from berth.job.models import Job
from berth.builder import SphinxBackend
from berth.celery import app as celery
from berth.project.models import Project
from berth.vcs.git_vcs import Git


class BuildTaskBase(celery.Task):
    abstract = True

    def update_job_state(self, job_pk, state):
        return Job.objects.filter(pk=job_pk).update(state=state)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        job_pk = args[0]
        self.update_job_state(job_pk, constants.BUILD_STATUS_FAILED)


class Checkout(BuildTaskBase):
    def run(self, job_pk):
        job = Job.objects.select_related('project').get(pk=job_pk)
        job.state = constants.BUILD_STATUS_IN_PROGRESS
        job.save(update_fields=['state'])

        git = Git(job.project)
        git.update()
        # support for tags will come eventually
        git.checkout('master')
        return job.pk


class CommenceBuild(BuildTaskBase):
    def run(self, job_pk):
        job = Job.objects.select_related('project').get(pk=job_pk)
        backend = SphinxBackend(job.project)
        backend.build()

    def on_success(self, retval, task_id, args, kwargs):
        job_pk = args[0]
        self.update_job_state(job_pk, constants.BUILD_STATUS_COMPLETE)


checkout = Checkout()
commence_build = CommenceBuild()
