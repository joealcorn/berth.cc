import os
import platform
import subprocess

from django.conf import settings
from docker.client import Client
from docker.utils import kwargs_from_env


osx = any(platform.mac_ver())


class NonexistantCheckout(Exception):
    pass


class Backend(object):
    '''
    This is the base backend builder class
    which all builders inherit from.
    Contains utility functions and defines
    the public API.
    '''

    # building = ''
    # base_image = ''

    def __init__(self, project):
        self.project = project
        self.checkout_directory = project.get_checkout_directory()
        self.artifact_directory = project.get_artifact_directory()
        self.image_name = self.get_image_name()
        self.container_name = self.get_container_name()

        kwargs = kwargs_from_env()
        if settings.DEBUG and osx:
            # development helper for boot2docker users
            kwargs['tls'].assert_hostname = False
        self.docker = Client(**kwargs)

        if not os.path.exists(self.checkout_directory):
            raise NonexistantCheckout(
                'No such checkout: %s' % self.checkout_directory
            )

        if not os.path.exists(self.artifact_directory):
            os.makedirs(self.artifact_directory)

    def build_command(self):
        raise NotImplementedError

    def setup_commands(self):
        raise NotImplementedError

    def build(self):
        try:
            self.setup_container()
            command = self.build_command()
            proc = self.docker_run(command)
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                raise Exception('Build failure: %s' % stderr)

            print stdout
        finally:
            self.remove_container()

    def get_image_name(self):
        '''
        The image name is used for the persistant
        image shared between builds
        '''
        return 'berth/%s-project-%d' % (self.building, self.project.id)

    def get_container_name(self):
        '''
        The container name is used for the temporary
        state between commited images
        '''
        return 'temp-%d' % self.project.id

    def commit_container(self):
        proc = subprocess.Popen(
            ['docker', 'commit', self.container_name, self.image_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise Exception('Could not commit container: %s' % stderr)

    def remove_container(self):
        proc = subprocess.Popen(
            ['docker', 'rm', self.container_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            raise Exception('Could not remove container: %s' % stderr)

    def setup_container(self):
        if self.image_exists():
            image_name = self.image_name
        else:
            image_name = self.base_image

        for command in self.setup_commands():
            proc = self.docker_run(command, image_name)
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                raise Exception('summin went wrong: %s\n%s' % (stdout, stderr))

            print stdout
            self.commit_container()
            self.remove_container()
            image_name = self.image_name

    def image_exists(self):
        return len(self.docker.images(name=self.image_name)) > 0

    def docker_run(self, command, image_name=None):
        if image_name is None:
            image_name = self.image_name

        cmd = [
            'docker', 'run',
            '-v', '%s:/root/build/docs' % self.checkout_directory,
            '-v', '%s:/root/build/artifacts' % self.artifact_directory,
            '-w', '/root/build/docs',
            '--name', self.container_name,
            image_name,
        ]
        cmd.extend(command)

        return subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.checkout_directory,
        )
