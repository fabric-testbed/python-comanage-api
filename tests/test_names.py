import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'


SAMPLE_NAMES = {
    'ResponseType': 'Names',
    'Version': '1.0',
    'Names': [{
        'Version': '1.0',
        'Id': 500,
        'Given': 'John',
        'Family': 'Doe',
        'Type': 'official',
        'Person': {'Type': 'CO', 'Id': 100},
        'PrimaryName': True,
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
    }],
}


class TestNamesNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.names_add()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.names_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.names_edit()


class TestNamesView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names.json', json=SAMPLE_NAMES)
        result = api.names_view_all()
        assert result['Names'][0]['Given'] == 'John'

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names/500.json', json=SAMPLE_NAMES)
        result = api.names_view_one(name_id=500)
        assert result['Names'][0]['Family'] == 'Doe'

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.names_view_one(name_id=999)


class TestNamesViewPerPerson:
    def test_valid_copersonid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names.json', json=SAMPLE_NAMES)
        api.names_view_per_person(person_type='copersonid', person_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_valid_orgidentityid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names.json', json=SAMPLE_NAMES)
        api.names_view_per_person(person_type='orgidentityid', person_id=50)
        assert 'orgidentityid' in mock_adapter.last_request.qs

    def test_invalid_person_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="person_type"):
            api.names_view_per_person(person_type='badtype', person_id=100)

    def test_default_person_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/names.json', json=SAMPLE_NAMES)
        api.names_view_per_person(person_type=None, person_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs
