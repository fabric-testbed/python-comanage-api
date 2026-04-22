import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'


SAMPLE_EMAILS = {
    'ResponseType': 'EmailAddresses',
    'Version': '1.0',
    'EmailAddresses': [{
        'Version': '1.0',
        'Id': 300,
        'Mail': 'user@example.com',
        'Type': 'official',
        'Verified': True,
        'Person': {'Type': 'CO', 'Id': 100},
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
    }],
}


class TestEmailAddressesNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.email_addresses_add()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.email_addresses_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.email_addresses_edit()


class TestEmailAddressesView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses.json', json=SAMPLE_EMAILS)
        result = api.email_addresses_view_all()
        assert result['EmailAddresses'][0]['Mail'] == 'user@example.com'

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses/300.json', json=SAMPLE_EMAILS)
        result = api.email_addresses_view_one(email_address_id=300)
        assert result['EmailAddresses'][0]['Id'] == 300

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.email_addresses_view_one(email_address_id=999)


class TestEmailAddressesViewPerPerson:
    def test_valid_copersonid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses.json', json=SAMPLE_EMAILS)
        api.email_addresses_view_per_person(person_type='copersonid', person_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_valid_orgidentityid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses.json', json=SAMPLE_EMAILS)
        api.email_addresses_view_per_person(person_type='orgidentityid', person_id=50)
        assert 'orgidentityid' in mock_adapter.last_request.qs

    def test_case_insensitive(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses.json', json=SAMPLE_EMAILS)
        api.email_addresses_view_per_person(person_type='CopersonId', person_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_invalid_person_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="person_type"):
            api.email_addresses_view_per_person(person_type='badtype', person_id=100)

    def test_default_person_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/email_addresses.json', json=SAMPLE_EMAILS)
        api.email_addresses_view_per_person(person_type=None, person_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs
