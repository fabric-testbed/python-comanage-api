import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'


SAMPLE_IDENTIFIERS = {
    'ResponseType': 'Identifiers',
    'Version': '1.0',
    'Identifiers': [{
        'Version': '1.0',
        'Id': 400,
        'Type': 'oidcsub',
        'Identifier': 'http://cilogon.org/serverA/users/12345',
        'Login': False,
        'Person': {'Type': 'CO', 'Id': 100},
        'Status': 'Active',
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
    }],
}


class TestIdentifiersNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.identifiers_add()

    def test_assign(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.identifiers_assign()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.identifiers_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.identifiers_edit()


class TestIdentifiersView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers.json', json=SAMPLE_IDENTIFIERS)
        result = api.identifiers_view_all()
        assert result['Identifiers'][0]['Id'] == 400

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers/400.json', json=SAMPLE_IDENTIFIERS)
        result = api.identifiers_view_one(identifier_id=400)
        assert result['Identifiers'][0]['Identifier'] == 'http://cilogon.org/serverA/users/12345'

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.identifiers_view_one(identifier_id=999)


class TestIdentifiersViewPerEntity:
    def test_valid_copersonid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers.json', json=SAMPLE_IDENTIFIERS)
        api.identifiers_view_per_entity(entity_type='copersonid', entity_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_valid_cogroupid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers.json', json=SAMPLE_IDENTIFIERS)
        api.identifiers_view_per_entity(entity_type='cogroupid', entity_id=50)
        assert 'cogroupid' in mock_adapter.last_request.qs

    def test_invalid_entity_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="entity_type"):
            api.identifiers_view_per_entity(entity_type='badtype', entity_id=100)

    def test_default_entity_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers.json', json=SAMPLE_IDENTIFIERS)
        api.identifiers_view_per_entity(entity_type=None, entity_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_case_insensitive(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/identifiers.json', json=SAMPLE_IDENTIFIERS)
        api.identifiers_view_per_entity(entity_type='CoPersonId', entity_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs
