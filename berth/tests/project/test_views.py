from urlparse import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from berth.project.models import Project
from berth.utils.test import TestCase


class TestProjectUpdate(TestCase):

    @property
    def endpoint(self):
        return reverse_lazy('update-project', kwargs={'pk': self.project.pk})

    def test_update_when_signed_out(self):
        resp = self.client.post(self.endpoint, data={
            'name': 'New project name',
        })
        assert resp.status_code == 302
        url = urlparse(resp['Location'])
        assert reverse_lazy(settings.LOGIN_URL) == url.path

    def test_update_as_incorrect_user(self):
        user = self.create_user()
        self.client.login(email=user.email, password='password')
        resp = self.client.post(self.endpoint, data={
            'name': 'New project name',
        })
        assert resp.status_code == 403

    def test_update(self):
        self.client.login(email=self.user.email, password='password')
        resp = self.client.post(self.endpoint, data={
            'name': 'New project name',
            'slug': 'new-project-name',
            'repo_url': self.project.repo_url,
        })
        assert resp.status_code == 302
        assert urlparse(resp['Location']).path == self.endpoint
        project = Project.objects.get(pk=self.project.pk)
        assert project.name == 'New project name'
        assert project.slug == 'new-project-name'
