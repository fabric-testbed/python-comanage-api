import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'


SAMPLE_LINKS = {
    'ResponseType': 'CoOrgIdentityLinks',
    'Version': '1.0',
    'CoOrgIdentityLinks': [{
        'Version': '1.0',
        'Id': 800,
        'CoPersonId': 100,
        'OrgIdentityId': 600,
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
    }],
}


class TestCoorgIdentityLinksNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.coorg_identity_links_add()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.coorg_identity_links_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.coorg_identity_links_edit()


class TestCoorgIdentityLinksView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links.json', json=SAMPLE_LINKS)
        result = api.coorg_identity_links_view_all()
        assert result['CoOrgIdentityLinks'][0]['Id'] == 800

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links/800.json', json=SAMPLE_LINKS)
        result = api.coorg_identity_links_view_one(coorg_identity_link_id=800)
        assert result['CoOrgIdentityLinks'][0]['CoPersonId'] == 100

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.coorg_identity_links_view_one(coorg_identity_link_id=999)


class TestCoorgIdentityLinksViewByIdentity:
    def test_valid_copersonid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links.json', json=SAMPLE_LINKS)
        api.coorg_identity_links_view_by_identity(identity_type='copersonid', identity_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_valid_orgidentityid(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links.json', json=SAMPLE_LINKS)
        api.coorg_identity_links_view_by_identity(identity_type='orgidentityid', identity_id=600)
        assert 'orgidentityid' in mock_adapter.last_request.qs

    def test_invalid_identity_type(self, api, mock_adapter):
        with pytest.raises(ValueError, match="identity_type"):
            api.coorg_identity_links_view_by_identity(identity_type='badtype', identity_id=100)

    def test_default_identity_type(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links.json', json=SAMPLE_LINKS)
        api.coorg_identity_links_view_by_identity(identity_type=None, identity_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_case_insensitive(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_org_identity_links.json', json=SAMPLE_LINKS)
        api.coorg_identity_links_view_by_identity(identity_type='OrgIdentityId', identity_id=600)
        assert 'orgidentityid' in mock_adapter.last_request.qs
