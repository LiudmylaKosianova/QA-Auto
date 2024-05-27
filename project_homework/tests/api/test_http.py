import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(f"Response: {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body["company"] == None    
    assert r.status_code == 200
    assert headers["Accept-Ranges"] == "bytes"

@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/liudmila_kosianova")
    assert r.status_code == 404