import hashlib
import os

REPO_DIR = '_repos'


def store_dir(file_path, file_name):
    path = os.path.join(file_path, file_name)
    hash = hashlib.md5(path).hexdigest()
    dir1 = hash[0:2]
    dir2 = hash[2:4]
    file_dir = os.path.join(REPO_DIR, dir1, dir2, file_name)
    return file_dir
