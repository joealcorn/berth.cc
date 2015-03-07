from berth.celery import app as celery
from berth.project.models import Project
from berth.builder import SphinxBackend
from berth.vcs.git_vcs import Git


@celery.task
def checkout(project_pk):
    project = Project.objects.get(pk=project_pk)
    git = Git(project)
    git.update()
    # support for tags will come eventually
    git.checkout('master')
    return project_pk


@celery.task
def commence_build(project_pk):
    project = Project.objects.get(pk=project_pk)
    backend = SphinxBackend(project)
    backend.build()
