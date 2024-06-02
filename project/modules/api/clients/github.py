import requests

class GitHub:

    def get_user(self, username):
        address = f"https://api.github.com/users/{username}"
        r = requests.get(address)
        return r.json()
    
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params={"q":name})
        return r.json()
    
    def get_emoji(self):
        r = requests.get("https://api.github.com/emojis")
        return r.json()
    
    def get_commit(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        return r.json()
    
    def get_contributors(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/contributors")
        return r.json()
    
    def get_languages(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/languages")
        return r.json()
    
    # def list_emails(self, user):
    #     r = requests.get(f"https://api.github.com/{user}/public_emails")
    #     return r.json()


    
    

