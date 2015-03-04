from django.conf import settings


class InvalidRevision(Exception):
    pass


class VCS(object):
    '''
    Defines the public API for all subclasses
    '''

    repo_clone_dir = settings.REPO_CLONE_DIR

    def __init__(self, project):
        self.project = project
        self.checkout_dir = project.get_checkout_directory()

    def clone(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def checkout(self, ref):
        raise NotImplementedError
