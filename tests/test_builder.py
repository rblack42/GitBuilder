import unittest
import os
from shutil import rmtree
from GitBuilder import GitBuilder

REPO_NAME = 'test.git'
REPO_PATH = '_repos'
TEST_FILE = 'src/main.cpp'


class TestGitBuilder(unittest.TestCase):

    def test_new_repo(self):
        repo_path = os.path.join(REPO_PATH, REPO_NAME)
        if os.path.exists(repo_path):
            rmtree(REPO_PATH)
        gb = GitBuilder(REPO_NAME)
        self.assertTrue(os.path.exists(repo_path))

    def test_file_store(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
