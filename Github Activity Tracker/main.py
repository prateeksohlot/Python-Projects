import requests
from collections import defaultdict

username = "prateeksohlot"
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url, timeout=10)
events = response.json()


for event in events:
    event_type = event.get('type')  
    repo_name = event['repo']['name']  
    actor = event['actor']['login']

    if event_type == 'PushEvent':  
        commits_count = len(event['payload']['commits'])  
        print(f"Pushed {commits_count} commits to {repo_name}")  
    if event_type == 'IssuesEvent' and event['payload']['action'] == 'opened':  
        print(f"Opened a new issue in {repo_name}")
    if event_type == 'IssuesEvent' and  event['payload']['action'] == 'closed':
        print(f"Closed an issue in {repo_name}")
    if event_type == 'WatchEvent':  
        print(f"Starred {repo_name}")
    if event_type == 'PullRequestEvent':
        print(f"Opened a new pull request in {repo_name}")
    


'''
PushEvent: Triggered when commits are pushed to a repository1
.

PullRequestEvent: Triggered when a pull request is created, closed, reopened, or synchronized1
.

IssueCommentEvent: Triggered when a comment is created on an issue1
.

CreateEvent: Triggered when a repository, branch, or tag is created1
.

DeleteEvent: Triggered when a repository, branch, or tag is deleted1
.

Issue and Pull Request Events
IssuesEvent: Triggered when an issue is opened, closed, reopened, labeled, or assigned1
.

PullRequestEvent: Triggered when a pull request is opened, closed, reopened, labeled, or assigned1
.

CommitCommentEvent: Triggered when a comment is made on a commit1
.

PullRequestReviewEvent: Triggered when a pull request review is submitted1
.

Organization Events
MemberEvent: Triggered when a user is added or removed from an organization1
.

TeamEvent: Triggered when a team is added or removed from an organization1
.

RepositoryEvent: Triggered when a repository is added or removed from an organization1
.

Other Events
WatchEvent: Triggered when a user starts or stops watching a repository1
.

ForkEvent: Triggered when a user forks a repository1
.

GollumEvent: Triggered when a wiki page is created, edited, or deleted1
.

StatusEvent: Triggered when the status of a commit is updated1
.


'''

