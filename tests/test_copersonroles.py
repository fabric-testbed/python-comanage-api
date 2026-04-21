import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'


SAMPLE_ROLE = {
    'ResponseType': 'CoPersonRoles',
    'Version': '1.0',
    'CoPersonRoles': [{
        'Version': '1.0',
        'Id': 200,
        'Person': {'Type': 'CO', 'Id': 100},
        'CouId': 42,
        'Affiliation': 'member',
        'O': 'TestCO',
        'Status': 'Active',
        'Created': '2024-01-01 00:00:00',
        'Modified': '2024-01-01 00:00:00',
        'Revision': 0,
        'Deleted': False,
        'ActorIdentifier': 'admin',
    }],
}

NEW_ROLE = {
    'ResponseType': 'NewObject',
    'Version': '1.0',
    'ObjectType': 'CoPersonRole',
    'Id': '200',
}


class TestCopersonRolesAdd:
    def test_success_defaults(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/co_person_roles.json', json=NEW_ROLE, status_code=201)
        result = api.coperson_roles_add(coperson_id=100, cou_id=42)
        assert result['Id'] == '200'
        body = mock_adapter.last_request.json()
        assert body['CoPersonRoles'][0]['Status'] == 'Active'
        assert body['CoPersonRoles'][0]['Affiliation'] == 'member'

    def test_custom_status_and_affiliation(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/co_person_roles.json', json=NEW_ROLE, status_code=201)
        api.coperson_roles_add(coperson_id=100, cou_id=42, status='Pending', affiliation='faculty')
        body = mock_adapter.last_request.json()
        assert body['CoPersonRoles'][0]['Status'] == 'Pending'
        assert body['CoPersonRoles'][0]['Affiliation'] == 'faculty'

    def test_invalid_status(self, api, mock_adapter):
        with pytest.raises(ValueError, match="status"):
            api.coperson_roles_add(coperson_id=100, cou_id=42, status='BadStatus')

    def test_invalid_affiliation(self, api, mock_adapter):
        with pytest.raises(ValueError, match="affiliation"):
            api.coperson_roles_add(coperson_id=100, cou_id=42, affiliation='CEO')

    def test_affiliation_case_insensitive(self, api, mock_adapter):
        mock_adapter.post(f'{API_URL}/co_person_roles.json', json=NEW_ROLE, status_code=201)
        api.coperson_roles_add(coperson_id=100, cou_id=42, affiliation='Faculty')
        body = mock_adapter.last_request.json()
        assert body['CoPersonRoles'][0]['Affiliation'] == 'faculty'


class TestCopersonRolesDelete:
    def test_success(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/co_person_roles/200.json', status_code=200)
        assert api.coperson_roles_delete(coperson_role_id=200) is True

    def test_not_found(self, api, mock_adapter):
        mock_adapter.delete(f'{API_URL}/co_person_roles/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.coperson_roles_delete(coperson_role_id=999)


class TestCopersonRolesEdit:
    def test_edit_status(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles/200.json', json=SAMPLE_ROLE)
        mock_adapter.put(f'{API_URL}/co_person_roles/200.json', status_code=200)
        assert api.coperson_roles_edit(coperson_role_id=200, status='Suspended') is True
        body = mock_adapter.last_request.json()
        assert body['CoPersonRoles'][0]['Status'] == 'Suspended'
        assert body['CoPersonRoles'][0]['Person']['Id'] == '100'

    def test_edit_keeps_existing(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles/200.json', json=SAMPLE_ROLE)
        mock_adapter.put(f'{API_URL}/co_person_roles/200.json', status_code=200)
        api.coperson_roles_edit(coperson_role_id=200)
        body = mock_adapter.last_request.json()
        assert body['CoPersonRoles'][0]['Status'] == 'Active'
        assert body['CoPersonRoles'][0]['Affiliation'] == 'member'
        assert body['CoPersonRoles'][0]['CouId'] == '42'

    def test_edit_invalid_status(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles/200.json', json=SAMPLE_ROLE)
        with pytest.raises(ValueError, match="status"):
            api.coperson_roles_edit(coperson_role_id=200, status='Nope')

    def test_edit_invalid_affiliation(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles/200.json', json=SAMPLE_ROLE)
        with pytest.raises(ValueError, match="affiliation"):
            api.coperson_roles_edit(coperson_role_id=200, affiliation='king')


class TestCopersonRolesView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles.json', json=SAMPLE_ROLE)
        result = api.coperson_roles_view_all()
        assert result['CoPersonRoles'][0]['Id'] == 200

    def test_view_per_coperson(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles.json', json=SAMPLE_ROLE)
        api.coperson_roles_view_per_coperson(coperson_id=100)
        assert 'copersonid' in mock_adapter.last_request.qs

    def test_view_per_cou(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles.json', json=SAMPLE_ROLE)
        api.coperson_roles_view_per_cou(cou_id=42)
        assert 'couid' in mock_adapter.last_request.qs

    def test_view_one(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_person_roles/200.json', json=SAMPLE_ROLE)
        result = api.coperson_roles_view_one(coperson_role_id=200)
        assert result['CoPersonRoles'][0]['Id'] == 200
