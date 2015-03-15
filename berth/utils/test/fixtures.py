import os
from random import random
from uuid import uuid4

from django.conf import settings
from django.db import IntegrityError
from exam import fixture

from berth.project.models import Project
from berth.user.models import User


class Fixtures(object):

    def load_data(self, fname):
        path = os.path.join(settings.BASE_DIR, 'berth/tests/data/', fname)
        with open(path, 'r') as f:
            return f.read()

    @fixture
    def project(self):
        return self.create_project(
            name='Test Project',
            slug='test-project',
            repo_url='https://github.com/joealcorn/berth.cc.git',
            owner=self.user,
            repo_identifier=0,
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
            kwargs['owner'] = self.user

        if 'subdomain' not in kwargs:
            kwargs['subdomain'] = uuid4().hex

        kwargs.setdefault('repo_source', 0)
        kwargs.setdefault('repo_identifier', 1)
        return Project.objects.create(**kwargs)
