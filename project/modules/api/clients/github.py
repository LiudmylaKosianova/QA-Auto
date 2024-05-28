import requests

class GitHub:

    def get_user(self, username):
        address = f"https://api.github.com/users/{username}"
        r = requests.get(address)
        return r.json()
    
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params={"q":name})
        return r.json()