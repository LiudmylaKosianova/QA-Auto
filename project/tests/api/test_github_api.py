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

@pytest.mark.api_plus
def test_emoji_is_there(github_api):
    emoji = github_api.get_emoji()
    assert emoji["-1"] != ""

@pytest.mark.api_plus
def test_repo_commits(github_api):
    commits = github_api.get_commit("LiudmylaKosianova", "learning-QA-Auto")

    assert commits[0]["commit"]["author"]["name"] == "Liudmyla Kosianova"
    assert commits[0]["commit"]["author"]["email"] == "Liudmyla.Kosianova@gmail.com"
    assert commits[0]["commit"]["verification"]["verified"] == False
    

@pytest.mark.api_plus
def test_repo_contributors(github_api):
    contributors = github_api.get_contributors("LiudmylaKosianova", "learning-QA-Auto")
    
    assert len(contributors) == 1
    assert contributors[0]["login"] == "LiudmylaKosianova"
    assert contributors[0]["type"] == "User"
    assert contributors[0]["contributions"] != 0

@pytest.mark.api_plus
def test_repo_languages(github_api):
    languages = github_api.get_languages("LiudmylaKosianova", "learning-QA-Auto")
    assert "Python" in languages
    


 


    
