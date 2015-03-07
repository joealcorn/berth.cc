from uuid import uuid4

from exam import fixture

from berth.project.models import Project
from berth.user.models import User


class Fixtures(object):

    @fixture
    def project(self):
        return self.create_project(
            name='Test Project',
            slug='test-project',
            repo_url='https://github.com/joealcorn/berth.cc.git',
            owner=self.user,
        )

    @fixture
    def user(self):
        return self.create_user()

    def create_user(self, **kwargs):
        if 'email' not in kwargs:
            kwargs['email'] = '%s@berth.cc' % uuid4().hex

        password = kwargs.pop('password', 'password')
        user = User(**kwargs)
        user.set_password(password)
        user.save(force_insert=True)
        return user

    def create_project(self, **kwargs):
        if 'owner' not in kwargs:
            kwargs.owner = self.user

        return Project.objects.create(**kwargs)
