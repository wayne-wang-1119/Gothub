from git import InvalidGitRepositoryError, NoSuchPathError, Repo
import time
from github import Github, GithubException


class git_methods:
    def __init__(self, repo_url, local_dir, access_token):
        self.repo_url = repo_url
        self.local_dir = local_dir
        self.github = Github(access_token)
        try:
            self.gh_repo = self.github.get_repo("Git-of-Thoughts/Gothub")
            self.repo = Repo(self.local_dir)
        except InvalidGitRepositoryError:
            self.repo = Repo.init(self.local_dir)
        except NoSuchPathError:
            self.repo = Repo.clone_from(self.repo_url, self.local_dir)
        except GithubException as g:
            print(f"An error occurred while accessing the GitHub repository: {g}")
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
        self.repo.index.commit(commit_message)

    def push_changes(self, branch_name):
        origin = self.repo.remote(name="origin")
        origin.push(branch_name)

    def pull_changes(self):
        self.repo.git.pull()

    def create_pull_request(self, branch_name):
        pr = self.gh_repo.create_pull(
            title=f"PR for step: {branch_name} created",
            body=f"This is a pull request for changes in the branch {branch_name}",
            head=branch_name,  # name of the branch you want to merge
            base="main",  # name of the branch you want to merge into
        )
