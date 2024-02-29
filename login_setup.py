import requests
from config import configure

def get_access_token():
    params = {
        "clientId": configure.client_id,
        "token": configure.token
    }
    response = requests.get(url=configure.authorization_url,params=params).json()
    access_token= response['data']['accessToken']
    return access_token