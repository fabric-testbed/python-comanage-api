import pytest
from requests.exceptions import HTTPError

API_URL = 'https://registry.example.org/registry'
CO_ID = 123


SAMPLE_COPEOPLE = {
    'ResponseType': 'CoPeople',
    'Version': '1.0',
    'CoPeople': [
        {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
        {'Version': '1.0', 'Id': 101, 'CoId': CO_ID, 'Status': 'Active'},
    ],
}


class TestCopeopleNotImplemented:
    def test_add(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.copeople_add()

    def test_delete(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.copeople_delete()

    def test_edit(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.copeople_edit()

    def test_find(self, api, mock_adapter):
        with pytest.raises(NotImplementedError):
            api.copeople_find()


class TestCopeopleMatch:
    def test_match_by_given(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people.json', json=SAMPLE_COPEOPLE)
        result = api.copeople_match(given='John')
        assert 'given' in mock_adapter.last_request.qs
        assert len(result['CoPeople']) == 2

    def test_match_distinct_by_id(self, api, mock_adapter):
        dupes = {
            'ResponseType': 'CoPeople',
            'Version': '1.0',
            'CoPeople': [
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
            ],
        }
        mock_adapter.get(f'{API_URL}/co_people.json', json=dupes)
        result = api.copeople_match(given='John', distinct_by_id=True)
        assert len(result['CoPeople']) == 1

    def test_match_no_distinct(self, api, mock_adapter):
        dupes = {
            'ResponseType': 'CoPeople',
            'Version': '1.0',
            'CoPeople': [
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
            ],
        }
        mock_adapter.get(f'{API_URL}/co_people.json', json=dupes)
        result = api.copeople_match(given='John', distinct_by_id=False)
        assert len(result['CoPeople']) == 2

    def test_match_multiple_params(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people.json', json=SAMPLE_COPEOPLE)
        api.copeople_match(given='John', family='Doe', mail='j@example.com')
        qs = mock_adapter.last_request.qs
        assert 'given' in qs
        assert 'family' in qs
        assert 'mail' in qs


class TestCopeopleView:
    def test_view_all(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people.json', json=SAMPLE_COPEOPLE)
        result = api.copeople_view_all()
        assert len(result['CoPeople']) == 2

    def test_view_per_co(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people.json', json=SAMPLE_COPEOPLE)
        result = api.copeople_view_per_co()
        assert 'coid' in mock_adapter.last_request.qs

    def test_view_per_identifier(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people.json', json=SAMPLE_COPEOPLE)
        result = api.copeople_view_per_identifier(identifier='user@example.com')
        qs = mock_adapter.last_request.qs
        assert 'search.identifier' in qs

    def test_view_per_identifier_distinct(self, api, mock_adapter):
        dupes = {
            'ResponseType': 'CoPeople',
            'Version': '1.0',
            'CoPeople': [
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
                {'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'},
            ],
        }
        mock_adapter.get(f'{API_URL}/co_people.json', json=dupes)
        result = api.copeople_view_per_identifier(identifier='x', distinct_by_id=True)
        assert len(result['CoPeople']) == 1

    def test_view_one(self, api, mock_adapter):
        single = {
            'ResponseType': 'CoPeople',
            'Version': '1.0',
            'CoPeople': [{'Version': '1.0', 'Id': 100, 'CoId': CO_ID, 'Status': 'Active'}],
        }
        mock_adapter.get(f'{API_URL}/co_people/100.json', json=single)
        result = api.copeople_view_one(coperson_id=100)
        assert result['CoPeople'][0]['Id'] == 100

    def test_view_one_not_found(self, api, mock_adapter):
        mock_adapter.get(f'{API_URL}/co_people/999.json', status_code=404)
        with pytest.raises(HTTPError):
            api.copeople_view_one(coperson_id=999)
