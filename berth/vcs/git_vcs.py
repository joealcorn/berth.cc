from os import path
import os

import git
from berth.vcs.base import VCS, InvalidRevision


class Git(VCS):

    repo = None

    def __init__(self, *a, **kw):
        super(Git, self).__init__(*a, **kw)
        if path.isdir(self.checkout_dir):
            self.repo = git.Repo(self.checkout_dir)
        else:
            self.repo = self.clone()

    def clone(self):
        return git.Repo.clone_from(
            self.project.repo_url,
            self.checkout_dir,
            depth=1,
            recursive=True,
        )

    def update(self):
        self.repo.remote('origin').pull()

    def checkout(self, ref):
        if ref in self.repo.tags:
            for tag in self.repo.tags:
                if tag.name != ref:
                    continue

                self.repo.head.reference = tag
                self.repo.head.reset(index=True, working_tree=True)
                tag.checkout()
                return

        if ref in self.repo.branches:
            for branch in self.repo.branches:
                if branch.name != ref:
                    continue

                branch.checkout()
                return

        raise InvalidRevision('Did not find %s in branches or tags' % ref)
