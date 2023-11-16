import requests
import json

from enum import Enum

class Status(Enum):
    SUCCESS = 1
    FAILURE = 2

class IssuesConnector():
    def __init__(self, _endpoint, _api_key):
        self.endpoint = _endpoint
        self.headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {_api_key}',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def IsWorking(self):
        return

    def GetIssues(self):
        # global endpoint, headers
        r = requests.get(self.endpoint, headers=self.headers)

        if r.status_code != 200:
            raise Exception("Request unsuccessful, check endpoint url or api key!")

        return json.loads(r.text)

    def CreateIssue(self, title, body, assignedto=None, labels=None):
        payload = {'title': title,
                   'body': body,
                   'assignee': assignedto,
                   'labels': labels
                 }

        r = requests.post(self.endpoint, headers=self.headers, data=json.dumps(payload))
        # return r
        if r.status_code != 201:
            raise Exception("Request unsuccessful, check endpoint url or api key!")

        return json.loads(r.text)

