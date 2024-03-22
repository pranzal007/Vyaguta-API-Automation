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

def test_get_events_positive(access_token,api_request):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = api_request.get_request("events", headers=headers)
    assert response.status_code == 200


def test_get_events_negetive(access_token,api_request):
    headers = {"Authorization": f"Bearer "}
    response = api_request.get_request("events", headers=headers)
    assert response.status_code == 401


def test_post_events_positive(access_token,api_request):
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        'name': Data.name_generator(self=None),
        'description': Data.description_generator(self=None),
        'link': None,
        'eventDate': Data.date_generator(self=None),
    }
    response = api_request.post_request("events", headers, payload)
    assert response.status_code == 201
    data_set = response.json()
    assert data_set['message'] == 'Event created successfully.'
    data_id = data_set['data']['id']
    fetch_data = {
        'id': data_id,
        'name': payload['name']

    }
    return fetch_data


def test_post_events_negetive(access_token,api_request):
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        'name': '',
        'description': Data.description_generator(self=None),
        'link': None,
        'eventDate': Data.date_generator(self=None),
    }
    response = api_request.post_request("events", headers, payload)
    assert response.status_code == 400


def test_update_events_positive(access_token,api_request):
    data = test_post_events_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        'name': Data.name_generator(self=None),
        'description': Data.description_generator(self=None),
        'link': None,
        'eventDate': Data.date_generator(self=None),
    }
    response = api_request.put_request(f"events/{data['id']}", headers, payload)
    assert response.status_code == 200


def test_update_events_negetive(access_token,api_request):
    data = test_post_events_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        'name': '',
        'description': Data.description_generator(self=None),
        'link': None,
        'eventDate': Data.date_generator(self=None),
    }
    response = api_request.put_request(f"events/{data['id']}", headers, payload)
    assert response.status_code == 400


def test_delete_event(access_token,api_request):
    data = test_post_events_positive(access_token,api_request)
    headers = {"Authorization": f"Bearer {access_token}"}
    response = api_request.delete_request(f"events/{data['id']}", headers)
    assert response.status_code == 200
