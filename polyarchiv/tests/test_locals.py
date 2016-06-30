# coding=utf-8
from __future__ import unicode_literals

import os
import shutil

from polyarchiv.locals import FileRepository, LocalRepository, GitRepository, ArchiveRepository
from polyarchiv.remotes import RemoteRepository
from polyarchiv.sources import RSync
from polyarchiv.tests.test_base import FileTestCase


class TestLocalRepository(FileTestCase):

    def test_local_repository(self):
        local_repository = self.get_local_repository()
        assert isinstance(local_repository, LocalRepository)
        local_repository.variables.update(RemoteRepository.constant_format_values)
        source = RSync('rsync', local_repository, self.original_dir_path, destination_path='rsync')
        local_repository.add_source(source)
        local_repository.backup()
        shutil.rmtree(self.copy_dir_path)
        os.rename(self.original_dir_path, self.copy_dir_path)
        local_repository.restore()
        self.assertEqualPaths(self.copy_dir_path, self.original_dir_path)

    def get_local_repository(self):
        raise NotImplementedError


class TestFileLocalRepository(TestLocalRepository):

    def get_local_repository(self):
        return FileRepository('test_repo', local_path=self.local_repository_path, command_display=True,
                              command_keep_output=True)


class TestGitLocalRepository(TestLocalRepository):

    def get_local_repository(self):
        return GitRepository('test_repo', local_path=self.local_repository_path, command_display=True,
                             command_keep_output=True)


class TestArchiveLocalRepository(TestLocalRepository):

    def get_local_repository(self):
        return ArchiveRepository('test_repo', local_path=self.local_repository_path, command_display=True,
                                 command_keep_output=True)