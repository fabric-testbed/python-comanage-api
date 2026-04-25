import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'
CO_ID = 123


SAMPLE_COU = {
    'ResponseType': 'Cous',
    'Version': '1.0',
    'Cous': [{
        'Version': '1.0',
        'Id': 42,
        'CoId': CO_ID,
        'Name': 'test-cou',
        'Description': 'A test COU',
        'Lft': 1,
        'Rght': 2,
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
        'Revision': 0,
        'Deleted': False,
        'ActorIdentifier': 'admin',
    }],
}

NEW_COU = {
    'ResponseType': 'NewObject',
    'Version': '1.0',
    'ObjectType': 'Cou',
    'Id': '42',
}


class TestCousAdd:
    def test_success(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/cous.json', json=NEW_COU, status_code=201)
        result = api.cous_add(name='test-cou', description='A test COU')
        assert result['Id'] == '42'

    def test_with_parent_id(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/cous.json', json=NEW_COU, status_code=201)
        api.cous_add(name='child', description='child cou', parent_id=10)
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['ParentId'] == '10'

    def test_without_parent_id(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/cous.json', json=NEW_COU, status_code=201)
        api.cous_add(name='root', description='root cou')
        body = mock_adapter.last_request.json()
        assert 'ParentId' not in body['Cous'][0]

    def test_http_error(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/cous.json', status_code=400)
        with pytest.raises(HTTPError):
            api.cous_add(name='bad', description='bad')


class TestCousDelete:
    def test_success(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/cous/42.json', status_code=200)
        assert api.cous_delete(cou_id=42) is True

    def test_not_found(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/cous/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.cous_delete(cou_id=999)


class TestCousEdit:
    def test_edit_name(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous/42.json', json=SAMPLE_COU)
        mock_adapter.put(f'{API_URL}/cous/42.json', status_code=200)
        assert api.cous_edit(cou_id=42, name='new-name') is True
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['Name'] == 'new-name'
        assert body['Cous'][0]['Description'] == 'A test COU'

    def test_edit_keeps_existing_when_none(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous/42.json', json=SAMPLE_COU)
        mock_adapter.put(f'{API_URL}/cous/42.json', status_code=200)
        api.cous_edit(cou_id=42)
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['Name'] == 'test-cou'
        assert body['Cous'][0]['Description'] == 'A test COU'

    def test_parent_id_set(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous/42.json', json=SAMPLE_COU)
        mock_adapter.put(f'{API_URL}/cous/42.json', status_code=200)
        api.cous_edit(cou_id=42, parent_id=10)
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['ParentId'] == '10'

    def test_parent_id_clear(self, api, mock_adapter):
        cou_with_parent = {
            'ResponseType': 'Cous',
            'Version': '1.0',
            'Cous': [{**SAMPLE_COU['Cous'][0], 'ParentId': '5'}],
        }
        mock_adapter.get(f'{API_URL}/cous/42.json', json=cou_with_parent)
        mock_adapter.put(f'{API_URL}/cous/42.json', status_code=200)
        api.cous_edit(cou_id=42, parent_id=0)
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['ParentId'] == ''

    def test_parent_id_keep_existing(self, api, mock_adapter):
        cou_with_parent = {
            'ResponseType': 'Cous',
            'Version': '1.0',
            'Cous': [{**SAMPLE_COU['Cous'][0], 'ParentId': '5'}],
        }
        mock_adapter.get(f'{API_URL}/cous/42.json', json=cou_with_parent)
        mock_adapter.put(f'{API_URL}/cous/42.json', status_code=200)
        api.cous_edit(cou_id=42, name='updated')
        body = mock_adapter.last_request.json()
        assert body['Cous'][0]['ParentId'] == '5'


class TestCousView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous.json', json=SAMPLE_COU)
        result = api.cous_view_all()
        assert result['Cous'][0]['Name'] == 'test-cou'

    def test_view_per_co(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous.json', json=SAMPLE_COU)
        result = api.cous_view_per_co()
        assert 'coid' in mock_adapter.last_request.qs
        assert result['Cous'][0]['Id'] == 42

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous/42.json', json=SAMPLE_COU)
        result = api.cous_view_one(cou_id=42)
        assert result['Cous'][0]['Id'] == 42

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.cous_view_one(cou_id=999)

    def test_view_all_server_error(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/cous.json', status_code=500)
        with pytest.raises(HTTPError):
            api.cous_view_all()
