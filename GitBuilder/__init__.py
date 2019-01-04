# -*- coding: utf_8 -*-
# GitBuilder
# ~~~~~~~~~~
#
# Manufacture Git Repositories for tutorials

from GitBuilder import repo


class GitBuilder(object):

    def __init__(self, repo_name):
        self.repo = repo.init(repo_name)
