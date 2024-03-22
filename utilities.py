import requests
from dotenv import dotenv_values

class ApiRequest:
    def __init__(self):
        self.config = dotenv_values("config.env")
        self.base_url = self.config['base_url']

    def get_request(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=headers)
        return response

    def post_request(self, endpoint, headers=None, payload=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=headers, json=payload)
        return response

    def put_request(self, endpoint, headers=None, payload=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=headers, json=payload)
        return response

    def delete_request(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=headers)
        return response
