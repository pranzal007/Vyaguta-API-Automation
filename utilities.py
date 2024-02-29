import requests
from config import configure

def get_request(endpoint, headers=None):
    url = f"{configure.base_url}/{endpoint}"
    response = requests.get(url, headers=headers)
    return response

def post_request(endpoint,headers=None, payload)
    url= f"{configure.base_url}/{endpoint}"
    response = requests.post(url,headers=headers,json=payload)
    return response