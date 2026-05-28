import pytest
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError

from comanage_api import __VERSION__, ComanageApi

API_URL = 'https://registry.example.org/registry'


class TestConstructor:
    def test_defaults(self, api, mock_adapter):
        assert api._CO_API_ORG_ID == 123
        assert api._CO_API_ORG_NAME == 'TestCO'
        assert api._timeout == 5
        assert api._CO_SSH_KEY_AUTHENTICATOR_ID == 7

    def test_trailing_slash_stripped(self, mock_adapter):
        api = ComanageApi(
            co_api_url='https://example.com/registry/',
            co_api_user='u', co_api_pass='p',
            co_api_org_id=1, co_api_org_name='T',
        )
        assert api._CO_API_URL == 'https://example.com/registry'

    def test_default_timeout(self, mock_adapter):
        api = ComanageApi(
            co_api_url='https://example.com',
            co_api_user='u', co_api_pass='p',
            co_api_org_id=1, co_api_org_name='T',
        )
        assert api._timeout == 30

    def test_custom_timeout(self, mock_adapter):
        api = ComanageApi(
            co_api_url='https://example.com',
            co_api_user='u', co_api_pass='p',
            co_api_org_id=1, co_api_org_name='T',
            timeout=60,
        )
        assert api._timeout == 60

    def test_no_ssh_key_authenticator(self, mock_adapter):
        api = ComanageApi(
            co_api_url='https://example.com',
            co_api_user='u', co_api_pass='p',
            co_api_org_id=1, co_api_org_name='T',
        )
        assert api._CO_SSH_KEY_AUTHENTICATOR_ID == 0

    def test_retry_adapter_mounted(self, api, mock_adapter):
        adapter = api._s.get_adapter('https://example.com')
        assert isinstance(adapter, HTTPAdapter)

    def test_version(self):
        assert __VERSION__ == '0.2.2'


class TestOptionSets:
    def test_status_options(self, api, mock_adapter):
        assert 'Active' in api.STATUS_OPTIONS
        assert 'Suspended' in api.STATUS_OPTIONS
        assert len(api.STATUS_OPTIONS) == 14

    def test_affiliation_options(self, api, mock_adapter):
        assert 'member' in api.AFFILIATION_OPTIONS
        assert 'faculty' in api.AFFILIATION_OPTIONS

    def test_entity_options(self, api, mock_adapter):
        assert 'copersonid' in api.ENTITY_OPTIONS
        assert 'cogroupid' in api.ENTITY_OPTIONS

    def test_person_options(self, api, mock_adapter):
        assert 'copersonid' in api.PERSON_OPTIONS
        assert 'orgidentityid' in api.PERSON_OPTIONS
        assert len(api.PERSON_OPTIONS) == 2

    def test_ssh_key_options(self, api, mock_adapter):
        assert 'ssh-rsa' in api.SSH_KEY_OPTIONS
        assert 'ssh-ed25519' in api.SSH_KEY_OPTIONS


class TestHttpHelpers:
    def test_get(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', json={'ok': True})
        result = api._get('test.json')
        assert result == {'ok': True}

    def test_get_with_params(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', json={'ok': True})
        api._get('test.json', params={'key': 'val'})
        assert 'key' in mock_adapter.last_request.qs

    def test_get_error(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', status_code=500)
        with pytest.raises(HTTPError):
            api._get('test.json')

    def test_post(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/test.json', json={'Id': '1'}, status_code=201)
        result = api._post('test.json', {'data': 'value'})
        assert result['Id'] == '1'

    def test_put(self, api, mock_adapter):
        mock_adapter.put(f'{API_URL}/test.json', status_code=200)
        assert api._put('test.json', {'data': 'value'}) is True

    def test_delete(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/test.json', status_code=200)
        assert api._delete('test.json') is True

    def test_delete_with_params(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/test.json', status_code=200)
        api._delete('test.json', params={'coid': 123})
        assert 'coid' in mock_adapter.last_request.qs


class TestGetByEntity:
    def test_valid_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', json={'ok': True})
        api._get_by_entity('test.json', 'copersonid', 100, api.PERSON_OPTIONS, 'test_field')
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_invalid_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="test_field"):
            api._get_by_entity('test.json', 'badtype', 100, api.PERSON_OPTIONS, 'test_field')

    def test_none_defaults_to_copersonid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', json={'ok': True})
        api._get_by_entity('test.json', None, 100, api.PERSON_OPTIONS, 'test_field')
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_case_insensitive(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/test.json', json={'ok': True})
        api._get_by_entity('test.json', 'OrgIdentityId', 50, api.PERSON_OPTIONS, 'test_field')
        assert 'orgidentityid' in mock_adapter.last_request.qs
