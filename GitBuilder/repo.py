import os
import pygit2
from shutil import rmtree
import logging

REPO_PATH = '_repos'

logging.basicConfig(
        filename='_logs/gitbuilder.info.log',
        level=logging.WARN
)


def init(repo_name):
    '''create a new repo, delete old one if necessary'''
    repo_path = os.path.join(REPO_PATH, repo_name)
    if os.path.isdir(repo_path):
        logging.info("deleting old repo: " + repo_path)
        rmtree(repo_path)
    repo = pygit2.init_repository(repo_path)
    logging.info("creating new repo: " + repo_path)
    return repo
