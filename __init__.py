import requests

endpoint = 'https://api.github.com/repos/ktm5j/gh-issues-connector/issues'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer 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',
    'X-GitHub-Api-Version': '2022-11-28'
}

class GHConnector():
    def GetIssues():
        global endpoint, headers
        r = requests.get(endpoint, headers=headers)
        return r
    
