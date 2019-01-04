# -*- coding: utf_8 -*-
# GitBuilder
# ~~~~~~~~~~
#
# Manufacture Git Repositories for tutorials

from GitBuilder import repo
import pygit2


class GitBuilder(object):

    def __init__(self, repo_name):
        self.repo = repo.init(repo_name)

    def commit(self, message):
        author = pygit2.Signature('Roie Black', 'rblack@austincc.edu')
        tree = self.repo.TreeBuilder().write()
        self.repo.create_commit(
            author,
            author,
            message,
            tree,
            []
        )

    def checkout(self, branch_name):
        branch = self.repo.lookup_branch(branch_name)
        ref = self.repo.lookup_reference(branch.name)
        self.repo.checkout(ref)

    def create_branch(self, branch_name):
        pass
