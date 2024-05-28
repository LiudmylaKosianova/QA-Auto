import pytest
import requests


@pytest.mark.myhttp
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Responce: {r.text}")

@pytest.mark.myhttp
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers
    assert r.status_code == 200
    assert body["name"] == "Chris Wanstrath"
    assert headers["Server"] == "GitHub.com"

@pytest.mark.myhttp
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")
    assert r.status_code == 404