import requests


class Backend:
    def __init__(self, api_hostname):
        self.api_hostname = api_hostname

    def get_users(self):
        return self.get('/api/v1/users')

    def get_comments(self):
        return self.get('/api/v1/comments')

    def get(self, api_path):
        url = f'http://{self.api_hostname}{api_path}'
        response = requests.get(url)
        data = response.json()
        return data
