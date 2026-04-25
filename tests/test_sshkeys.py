import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'
SSH_KEY_AUTH_ID = 7


SSH_PATH = 'ssh_key_authenticator/ssh_keys'

SAMPLE_SSHKEY = {
    'ResponseType': 'SshKeys',
    'Version': '1.0',
    'SshKeys': [{
        'Version': '1.0',
        'Id': 700,
        'Person': {'Type': 'CO', 'Id': 100},
        'Comment': 'test key',
        'Type': 'ssh-rsa',
        'Skey': 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC...',
        'SshKeyAuthenticatorId': SSH_KEY_AUTH_ID,
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
        'Revision': 0,
        'Deleted': False,
        'ActorIdentifier': 'admin',
    }],
}

NEW_SSHKEY = {
    'ResponseType': 'NewObject',
    'Version': '1.0',
    'ObjectType': 'SshKey',
    'Id': '700',
}


class TestSshKeysAdd:
    def test_success(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/{SSH_PATH}.json', json=NEW_SSHKEY, status_code=201)
        result = api.ssh_keys_add(coperson_id=100, ssh_key='AAAA...', key_type='ssh-rsa', comment='my key')
        assert result['Id'] == '700'
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Comment'] == 'my key'
        assert body['SshKeys'][0]['SshKeyAuthenticatorId'] == str(SSH_KEY_AUTH_ID)

    def test_no_comment(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/{SSH_PATH}.json', json=NEW_SSHKEY, status_code=201)
        api.ssh_keys_add(coperson_id=100, ssh_key='AAAA...', key_type='ssh-rsa')
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Comment'] == ''

    def test_custom_authenticator_id(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/{SSH_PATH}.json', json=NEW_SSHKEY, status_code=201)
        api.ssh_keys_add(coperson_id=100, ssh_key='AAAA...', key_type='ssh-rsa',
                         ssh_key_authenticator_id=99)
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['SshKeyAuthenticatorId'] == '99'

    def test_invalid_key_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="key_type"):
            api.ssh_keys_add(coperson_id=100, ssh_key='AAAA...', key_type='bad-type')

    def test_key_type_case_insensitive(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/{SSH_PATH}.json', json=NEW_SSHKEY, status_code=201)
        api.ssh_keys_add(coperson_id=100, ssh_key='AAAA...', key_type='SSH-RSA')
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Type'] == 'ssh-rsa'


class TestSshKeysDelete:
    def test_success(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/{SSH_PATH}/700.json', status_code=200)
        assert api.ssh_keys_delete(ssh_key_id=700) is True

    def test_not_found(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/{SSH_PATH}/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.ssh_keys_delete(ssh_key_id=999)


class TestSshKeysEdit:
    def test_edit_comment(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/700.json', json=SAMPLE_SSHKEY)
        mock_adapter.put(f'{API_URL}/{SSH_PATH}/700.json', status_code=200)
        assert api.ssh_keys_edit(ssh_key_id=700, comment='new comment') is True
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Comment'] == 'new comment'
        assert body['SshKeys'][0]['Person']['Id'] == '100'

    def test_edit_keeps_existing(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/700.json', json=SAMPLE_SSHKEY)
        mock_adapter.put(f'{API_URL}/{SSH_PATH}/700.json', status_code=200)
        api.ssh_keys_edit(ssh_key_id=700)
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Type'] == 'ssh-rsa'
        assert body['SshKeys'][0]['Skey'] == 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC...'
        assert body['SshKeys'][0]['Comment'] == 'test key'

    def test_edit_key_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/700.json', json=SAMPLE_SSHKEY)
        mock_adapter.put(f'{API_URL}/{SSH_PATH}/700.json', status_code=200)
        api.ssh_keys_edit(ssh_key_id=700, key_type='ssh-ed25519')
        body = mock_adapter.last_request.json()
        assert body['SshKeys'][0]['Type'] == 'ssh-ed25519'

    def test_edit_invalid_key_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/700.json', json=SAMPLE_SSHKEY)
        with pytest.raises(ValueError, match="key_type"):
            api.ssh_keys_edit(ssh_key_id=700, key_type='bad-type')


class TestSshKeysView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}.json', json=SAMPLE_SSHKEY)
        result = api.ssh_keys_view_all()
        assert result['SshKeys'][0]['Id'] == 700

    def test_view_per_coperson(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}.json', json=SAMPLE_SSHKEY)
        result = api.ssh_keys_view_per_coperson(coperson_id=100)
        assert result['SshKeys'][0]['Id'] == 700
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_view_per_coperson_204_empty(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}.json', status_code=204)
        result = api.ssh_keys_view_per_coperson(coperson_id=100)
        assert result['SshKeys'] == []

    def test_view_per_coperson_error(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}.json', status_code=401)
        with pytest.raises(HTTPError):
            api.ssh_keys_view_per_coperson(coperson_id=100)

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/700.json', json=SAMPLE_SSHKEY)
        result = api.ssh_keys_view_one(ssh_key_id=700)
        assert result['SshKeys'][0]['Id'] == 700

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/{SSH_PATH}/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.ssh_keys_view_one(ssh_key_id=999)
