#!/usr/bin/env python

import os
import subprocess


FILE_WITH_TEST_FILES = '.jenkins/test_files.txt'
TEST_PATH = os.environ['TEST_PATH']
URL = u'https://archive.gemini.edu/file/'


def download_test_data():

    create_test_folder_if_does_not_exist()
    download_non_existing_test_files()


def create_test_folder_if_does_not_exist():

    if os.path.exists(TEST_PATH):
        print('Skip creation of existing folder: {}'.format(TEST_PATH))
    else:
        print('Create non-existing test folder: {}'.format(TEST_PATH))
        os.makedirs(TEST_PATH)


def download_non_existing_test_files():

    with open(FILE_WITH_TEST_FILES, 'r') as list_of_files:

        for _filename in list_of_files.readlines():

            current_file = os.path.join(TEST_PATH, _filename).strip()

            if os.path.exists(current_file):
                print('Skip existing file: {:s}'.format(current_file))

            else:
                print('Download missing file: {:s}'.format(current_file))
                _path, _file = os.path.split(current_file)
                if not os.path.exists(_path):
                    os.makedirs(_path)
                subprocess.run(['curl', '--silent', URL + _file, '--output',
                                current_file])


if __name__ == "__main__":
    download_test_data()
