import pytest
from modules.api.clients.github import Github

@pytest.mark.api
def test_user_exists(github_api):
    #api = Github()
    #user = api.get_user_defunkt()
    user = github_api.get_user("defunkt")
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exist(github_api):
    #api = Github()
    #r = api.get_non_exist_user()
    #print(r)
    r = github_api.get_user("snowwhitesheep")
    assert r['message'] == 'Not Found'