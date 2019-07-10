import json
import requests

api_url_base = 'https://api.github.com/vikash212000yadav'
headers = {'Content-Type': 'application/json',
        'User-Agent': 'Python Student',
        'Accept': 'application/vnd.github.v3+json'}

def get_repos(username):
    api_url = '{}orgs/{}/repos'.format(api_url_base, username)
    response = requests.get(api_url, headers = headers)
    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

repo_list = get_repos('octokit')

if repo_list is not None:
    print(repo_list)
else:
    print('No Repo List Found')
