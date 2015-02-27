from uuid import uuid4

from exam import fixture

from berth.user.models import User


class Fixtures(object):

    def create_user(self, **kwargs):
        if 'email' not in kwargs:
            kwargs['email'] = '%s@berth.cc' % uuid4().hex

        password = kwargs.pop('password', 'password')
        user = User(**kwargs)
        user.set_password(password)
        user.save(force_insert=True)
        return user
