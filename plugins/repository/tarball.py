import logging
import tarfile
import tempfile
import os, fnmatch
import config

from plugins.repository import helper


class TarbalHelper(helper.RepositoryHelper):

    def __init__(self, file_location=None):
        self.file_location = file_location
        self.temp_location = None

    def can_process(self, url):
        """
        :param url: check if URL is actually a tarfile. if it is, extract it to a temporary location
        :return:
        """
        self.file_location = url
        logging.error(self.file_location) #debug logging tarfile location
        if tarfile.is_tarfile(self.file_location): #confirm tar file
            self.temp_location = tempfile.mkdtemp() #create temporary extraction folder
            print(self.temp_location) #debug print extraction folder location
            tarball = tarfile.open(self.file_location, "r")
            tarball.extractall(self.temp_location) #extract tar.gz to file extraction location
            return True
        else:
            return False

    def login(self):
        """
        Login using the appropriate credentials
        :return:
        """
        #raise NotImplementedError("This method must be overridden")

    def get_files_from_root(self, candidate_filenames):
        """
        Given a list of candidate file names, examine the repository root, returning the file names and contents
        :param candidate_filenames: A list of the files of interest e.g. ['COPYING','LICENSE']
        :return: A Dictionary of the form {'filename':file_contents,...}
        """

        def find(candidate_filenames, path):
            found_files = {}
            for root, dirs, files in os.walk(path):
                for name in files:
                    for poss_name in candidate_filenames:
                        if fnmatch.fnmatch(name, poss_name):
                            found_files[name] = os.path.join(root, name)
            return found_files

        return find(candidate_filenames, self.temp_location)




    def get_commits(self, sha=None, path=None, author=None, number=-1, etag=None, since=None, until=None):
        """
        Return a list of all commits in a repository
        :params:
        Parameters:
        sha (str) – (optional), sha or branch to start listing commits from
        path (str) – (optional), commits containing this path will be listed
        author (str) – (optional), GitHub login, real name, or email to filter commits by (using commit author)
        number (int) – (optional), number of commits to return. Default: -1 returns all commits
        etag (str) – (optional), ETag from a previous request to the same endpoint
        since (datetime or string) – (optional), Only commits after this date will be returned. This can be a datetime or an ISO8601 formatted date string.
        until (datetime or string) – (optional), Only commits before this date will be returned. This can be a datetime or an ISO8601 formatted date string.
        :return: a list of Commit
        """
        #raise NotImplementedError("This method must be overridden")
        return []
