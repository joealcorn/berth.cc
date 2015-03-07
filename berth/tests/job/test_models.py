from berth.job.models import Job
from berth.job import constants
from berth.utils.test import TestCase


class TestJobNumbers(TestCase):
    def test_job_number_increments(self):
        project = self.project
        job1 = Job.objects.create(
            project=self.project,
            state=constants.BUILD_STATUS_QUEUED,
        )

        job2 = Job.objects.create(
            project=self.project,
            state=constants.BUILD_STATUS_QUEUED,
        )

        job3 = Job.objects.create(
            project=self.create_project(),
            state=constants.BUILD_STATUS_QUEUED,
        )

        job4 = Job.objects.create(
            project=self.project,
            state=constants.BUILD_STATUS_QUEUED,
        )

        job1 = Job.objects.get(pk=job1.pk)
        job2 = Job.objects.get(pk=job2.pk)
        job3 = Job.objects.get(pk=job3.pk)
        job4 = Job.objects.get(pk=job4.pk)

        assert job1.number == 1
        assert job2.number == 2
        assert job3.number == 1
        assert job4.number == 3
