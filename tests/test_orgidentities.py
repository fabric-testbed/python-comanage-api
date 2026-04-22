import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'
CO_ID = 123


SAMPLE_ORG_IDS = {
    'ResponseType': 'OrgIdentities',
    'Version': '1.0',
    'OrgIdentities': [{
        'Version': '1.0',
        'Id': 600,
        'Affiliation': 'member',
        'O': 'Example Org',
        'CoId': CO_ID,
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
    }],
}


class TestOrgIdentitiesNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.org_identities_add()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.org_identities_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.org_identities_edit()


class TestOrgIdentitiesView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities.json', json=SAMPLE_ORG_IDS)
        result = api.org_identities_view_all()
        assert result['OrgIdentities'][0]['Id'] == 600

    def test_view_per_co(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities.json', json=SAMPLE_ORG_IDS)
        api.org_identities_view_per_co()
        assert 'coid' in mock_adapter.last_request.qs

    def test_view_per_identifier(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities.json', json=SAMPLE_ORG_IDS)
        api.org_identities_view_per_identifier(identifier_id=12345)
        qs = mock_adapter.last_request.qs
        assert 'coid' in qs
        assert 'search.identifier' in qs

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities/600.json', json=SAMPLE_ORG_IDS)
        result = api.org_identities_view_one(org_identity_id=600)
        assert result['OrgIdentities'][0]['Id'] == 600
        assert 'coid' in mock_adapter.last_request.qs

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.org_identities_view_one(org_identity_id=999)

    def test_view_all_server_error(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/org_identities.json', status_code=500)
        with pytest.raises(HTTPError):
            api.org_identities_view_all()
