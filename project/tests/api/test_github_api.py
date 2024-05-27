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

@pytest.mark.api
def test_repo_is_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    #print(r)
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]

@pytest.mark.api
def test_repo_not_found(github_api):
    r = github_api.search_repo("liudmyla-kosianova")
    assert r["total_count"] == 0

@pytest.mark.api
def test_repo_one_char_found(github_api):
    r = github_api.search_repo("a")
    assert r["total_count"] != 0