import pytest
from utilities import get_request
from Data.Test_data import Data
from login_setup import get_access_token
from utilities import post_request

@pytest.fixture(scope="module")
def access_token():
    token = get_access_token()
    yield token

def test_get_designations_positive(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = get_request("designations", headers=headers)
    assert response.status_code == 200
def test_get_designations_negetive(access_token):
    headers = {"Authorization": f"Bearer"}
    response = get_request("designations", headers=headers)
    assert response.status_code == 401

def test_post_designations_positive(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    payload={
        'name': Data.name_generator(access_token),
        'description': Data.description_generator(access_token),
        'status': 'True'
    }
    response = post_request("designations",headers,payload)
    assert response.status_code == 201
    data_set= response.json()
    assert payload['name'] == data_set['data']['name']
    data_id= data_set['data']['id']
    data_name= data_set['data']['name']
    fetch_data= [data_id,data_name]
    print (fetch_data[1])
    return fetch_data

def test_post_designations_negetive (access_token):
    data= test_post_designations_positive(access_token)
    headers= {"Authorization":f"Bearer Token"}
    payload_1 = {
        'name': data[1],
        'description': Data.description_generator(access_token),
        'status': 'True'
    }

    payload_2 ={
        'name': '',
        'description': Data.description_generator(access_token),
        'status': 'True'
    }
    response_1 = post_request("designations", headers, payload_1)
    response_2=  post_request("designations", headers, payload_1)
    assert response_1.status_code == 400




