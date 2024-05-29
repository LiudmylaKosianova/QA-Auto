import pytest
import requests

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"

@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("butenkosergii")
    assert user["message"] == "Not Found"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo("become-qa-auto")
    assert repo["total_count"] == 57

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert repo["total_count"] == 0

@pytest.mark.api
def test_repo_with_single_char_found(github_api):
    repo = github_api.search_repo("l")
    assert repo["total_count"] != 0

@pytest.mark.api
def test_emoji_is_there(github_api):
    m = github_api.get_emoji()
    assert m["-1"] != ""

@pytest.mark.api
def test_repo_commits(github_api):
    c = github_api.get_commit("LiudmylaKosianova", "QA-Auto")
    assert c[0]["commit"]["author"]["name"] == "Liudmyla Kosianova"
    assert c[0]["commit"]["author"]["email"] == "Liudmyla.Kosianova@gmail.com"
    assert c[0]["commit"]["verification"]["verified"] == True


    
