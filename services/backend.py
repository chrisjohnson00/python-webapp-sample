import requests


class Backend:
    def __init__(self, api_hostname):
        self.api_hostname = api_hostname

    def get_users(self):
        url = f'http://{self.api_hostname}/api/v1/users'
        response = requests.get(url)
        data = response.json()
        return data
