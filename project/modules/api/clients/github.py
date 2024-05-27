import requests

class Github:

    # def get_user_defunkt(self):
    #     r = requests.get('http://api.github.com/users/defunkt')
    #     body = r.json()
    #     return body
    
    # def get_non_exist_user(self):
    #     r = requests.get('http://api.github.com/users/snowwhiteship')
    #     body = r.json()
    #     return body

    def def_user(self, username):
        r = requests.get(f"http://api.github.com/users/{username}")
        body = r.json()

        return body