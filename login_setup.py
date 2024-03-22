import requests
from dotenv import dotenv_values

class LoginSetup:
    def __init__(self):
        self.config = dotenv_values("config.env")

    def get_access_token(self):
        params = {
            "clientId": self.config["client_id"],
            "token": self.config["token"]
        }
        response = requests.get(url=self.config["authorization_url"], params=params).json()
        access_token = response['data']['accessToken']
        return access_token
