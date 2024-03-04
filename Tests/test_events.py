import pytest
from utilities import get_request
from Data.Test_data import Data
from login_setup import get_access_token
from utilities import post_request
from utilities import put_request
from utilities import delete_request

@pytest.fixture(scope="module")
def access_token():
    token = get_access_token()
    yield token

def test_get_events_positive(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = get_request("events", headers=headers)
    assert response.status_code == 200

def test_get_events_negetive(access_token):
    headers = {"Authorization": f"Bearer "}
    response = get_request("events", headers=headers)
    assert response.status_code == 401

