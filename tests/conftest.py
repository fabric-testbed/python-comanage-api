import pytest
import requests_mock as rm

from comanage_api import ComanageApi

API_URL = 'https://registry.example.org/registry'
API_USER = 'co_123.test-user'
API_PASS = 'test-pass'
CO_ID = 123
CO_NAME = 'TestCO'
SSH_KEY_AUTH_ID = 7


@pytest.fixture
def mock_adapter():
    with rm.Mocker() as m:
        yield m


@pytest.fixture
def api(mock_adapter):
    return ComanageApi(
        co_api_url=API_URL,
        co_api_user=API_USER,
        co_api_pass=API_PASS,
        co_api_org_id=CO_ID,
        co_api_org_name=CO_NAME,
        co_ssh_key_authenticator_id=SSH_KEY_AUTH_ID,
        timeout=5,
    )


@pytest.fixture
def url():
    return API_URL
