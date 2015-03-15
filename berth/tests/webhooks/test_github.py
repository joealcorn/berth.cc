import json

from django.core.urlresolvers import reverse_lazy
from exam import before, after, Exam

from berth.celery import app as celery
from berth.job import tasks
from berth.project import constants
from berth.utils.test import APITestCase

noop = lambda *a, **kw: None


class TestGithubWebhook(APITestCase):

    endpoint = reverse_lazy('gh-webhook')

    @before
    def patch_tasks(self):
        self.checkout = tasks.checkout
        self.commence_build = tasks.commence_build

        tasks.checkout = celery.task(noop)
        tasks.commence_build = celery.task(noop)

    @after
    def unpatch_tasks(self):
        tasks.checkout = self.checkout
        tasks.commence_build = self.commence_build

    def test_success(self):
        data = json.loads(self.load_data('github/webhook.json'))

        project = self.create_project(
            name=data['repository']['name'],
            repo_identifier=data['repository']['id'],
            repo_source=constants.GITHUB,
        )

        resp = self.client.post(self.endpoint, data, format='json')
        assert resp.status_code == 200

    def test_project_nonexistant(self):
        data = json.loads(self.load_data('github/webhook.json'))
        resp = self.client.post(self.endpoint, data, format='json')
        assert resp.status_code == 404
