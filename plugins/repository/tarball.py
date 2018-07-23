"""
check file is a tar file
if it is a tar file, invoke method to extract

method of extraction
create temp folder directory
extract tar file to temp directory
loop through the files in temp for documentation files

"""
import tarfile
import tempfile
import config

from plugins.repository.helper import *


class TarbalHelper(RepositoryHelper):

    def __init__(self, file_location=None):
        self.file_location = file_location
        self.temp_location = None

    def can_process(self, url):
        self.file_location = url
        logging.error(self.file_location)
        if tarfile.is_tarfile(self.file_location):
            self.temp_location = tempfile.mkdtemp()
            print(self.temp_location)
            tarball = tarfile.open(self.file_location, "r")
            tarball.extractall(self.temp_location)
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
        found_files = {}
        # Get all files in the root of the extracted tar file, temp_location
        root_files = self.temp_location.contents('/')
        root_files_iter = root_files.items()
        for name, contents in root_files_iter:
            for poss_name in candidate_filenames:
                if poss_name in name.upper():
                    logging.info("Found a candidate file: " + name)
                    found_files[name] = self.temp_location.contents(name).decoded.decode('UTF-8')

        return found_files

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
