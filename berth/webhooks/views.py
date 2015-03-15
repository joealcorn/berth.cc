from django.conf import settings
from rest_framework import response, views, generics

from berth.job.models import Job
from berth.job import constants as job_constants
from berth.project import constants as project_constants
from berth.project.models import Project
from berth.webhooks.serializers import GithubWebhookSerializer


class GithubWebhook(generics.GenericAPIView):
    serializer_class = GithubWebhookSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(status=400)

        try:
            project = Project.objects.get(
                repo_identifier=serializer.data['repository']['id'],
                repo_source=project_constants.GITHUB,
            )
        except Project.DoesNotExist:
            return response.Response(status=404)

        job = Job.objects.create(
            project=project,
            state=job_constants.BUILD_STATUS_QUEUED,
        )
        job.build()

        return response.Response()
