"""
@deprecated
"""


import time

from git import InvalidGitRepositoryError, NoSuchPathError, Repo

# Let's make gots not depend on github; gothub can depend on github
from github import Github, GithubException


class git_methods:
    ##This class provides a list of git methods to be used in another directory, gothub, to create a pull request
    def __init__(self, repo_url, local_dir, access_token):
        self.repo_url = repo_url  ##import repository url from config file
        self.local_dir = local_dir  ##import local directory from config file
        self.github = Github(access_token)  ##import access token from config file
        try:
            self.gh_repo = self.github.get_repo(
                "Git-of-Thoughts/Gothub"
            )  ##import repository from config file
            self.repo = Repo(self.local_dir)  ##import local directory from config file
        except InvalidGitRepositoryError:
            self.repo = Repo.init(self.local_dir)  ##initialize local directory
        except NoSuchPathError:
            self.repo = Repo.clone_from(
                self.repo_url, self.local_dir
            )  ##clone repository from config file
        except GithubException as g:
            print(
                f"An error occurred while accessing the GitHub repository: {g}"
            )  ##print error message
            raise

    # def branch_exists(self, branch_name):
    #     branches = [b.name for b in self.repo.branches]
    #     return branch_name in branches

    # def create_branch(self, branch_name):
    #     if not self.branch_exists(branch_name):
    #         self.repo.git.checkout("-b", branch_name)
    #         time.sleep(0.5)

    # def switch_branch(self, branch_name):
    #     if self.branch_exists(branch_name):
    #         self.repo.git.checkout(branch_name)

    def commit_changes(self, commit_message):
        self.repo.git.add(A=True)  # This will add all files to the staging area
        self.repo.index.commit(commit_message)  # This will commit all files

    def push_changes(self, branch_name):
        origin = self.repo.remote(
            name="origin"
        )  # This will get the remote named 'origin'
        origin.push(branch_name)  # This will push the changes to the branch

    def pull_changes(self):
        self.repo.git.pull()  # This will pull the changes from the remote

    def create_pull_request(self, branch_name):
        pr = self.gh_repo.create_pull(
            title=f"PR for step: {branch_name} created",
            body=f"This is a pull request for changes in the branch {branch_name}",
            head=branch_name,  # name of the branch you want to merge
            base="main",  # name of the branch you want to merge into
        )  # This will create a pull request
