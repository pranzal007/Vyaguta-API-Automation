import pytest
from Data.Test_data import Data
from login_setup import LoginSetup
from utilities import ApiRequest

@pytest.fixture(scope="module")
def access_token():
    login = LoginSetup()
    token = login.get_access_token()
    yield token

@pytest.fixture(scope="module")
def api_request():
    return ApiRequest()

def test_get_designations_positive(access_token, api_request):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = api_request.get_request("designations", headers=headers)
    assert response.status_code == 200

def test_get_designations_negetive(access_token,api_request):
    headers = {"Authorization": "Bearer"}
    response = api_request.get_request("designations", headers=headers)
    assert response.status_code == 401

def test_post_designations_positive(access_token,api_request):
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
            'name': Data.name_generator(self=None),
            'description': Data.description_generator(self=None),
            'status': 'True'
             }
    response = api_request.post_request("designations", headers, payload)
    assert response.status_code == 201
    data_set = response.json()
    assert payload['name'] == data_set['data']['name']
    data_id = data_set['data']['id']
    data_name = data_set['data']['name']
    fetch_data = {
            'id': data_id,
            'name': data_name
                }
    return fetch_data

def test_post_designations_negetive(access_token,api_request):
    data = test_post_designations_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    payload_1 = {
            'name': data['name'],
            'description': Data.description_generator(self=None),
             'status': 'True'
                    }

    payload_2 = {
            'name': '',
            'description': Data.description_generator(access_token),
            'status': 'True'
                    }
    response_1 = api_request.post_request("designations", headers, payload_1)
    response_2 = api_request.post_request("designations", headers, payload_2)
    assert response_1.status_code == 422
    assert response_2.status_code == 422

def test_update_designations_positive(access_token,api_request):
    data = test_post_designations_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
            'name': Data.name_generator(self=None),
            'description': Data.description_generator(access_token),
            'status': 'True',
            'id': data['id']
                    }
    response = api_request.put_request(f"designations/{data['id']}", headers, payload)
    assert response.status_code == 200
    data_set = response.json()
    fetch_id = data_set['data']['id']
    return fetch_id

def test_update_designations_negetive(access_token,api_request):
    data = test_update_designations_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
            'name': '',
            'description': Data.description_generator(self=None),
            'status': 'True',
            'id': data
                }

    response = api_request.put_request(f"designations/{data}", headers, payload)
    assert response.status_code == 400

def test_delete_designation(access_token,api_request):
    data = test_post_designations_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = api_request.delete_request(f"designations/{data['id']}", headers)
    assert response.status_code == 200

