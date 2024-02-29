import pytest
from utilities import get_request
from login_setup import get_access_token

@pytest.fixture(scope="module")
def access_token():
    token = get_access_token()
    yield token

def test_get_designations(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = get_request("designations", headers=headers)
    assert response.status_code == 200

