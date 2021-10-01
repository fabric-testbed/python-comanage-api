# comanage_api/_names.py
# Name API - https://spaces.at.internet2.edu/display/COmanage/Name+API

import json


def names_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new Name.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self.MOCK_501_URL
    resp = self.mock_session.get(
        url=url
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def names_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a Name.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self.MOCK_501_URL
    resp = self.mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def names_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing Name.

    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self.MOCK_501_URL
    resp = self.mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def names_view_all(self) -> dict:
    """
    Retrieve all existing Names.

    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body           Description
        200 OK              Name Response           Name returned
        401 Unauthorized                            Authentication required
        500 Other Error                             Unknown error
    """
    url = self.CO_API_URL + '/names.json'
    resp = self.s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def names_view_per_person(self, person_type: str, person_id: int) -> dict:
    """
    Retrieve Names attached to a CO Person or Org Identity.

    :param person_type:
    :param person_id:
    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      Name Response           Name returned
        401 Unauthorized                                    Authentication required
        404 CO Person Unknown                               id not found for CO Person
        404 Org Identity Unknown                            id not found for Org Identity
        500 Other Error                                     Unknown error
    """
    if not person_type:
        person_type = 'copersonid'
    else:
        person_type = str(person_type).lower()
    if person_type not in self.PERSON_OPTIONS:
        raise TypeError("Invalid Fields 'person_type'")
    url = self.CO_API_URL + '/names.json'
    params = {str(person_type): str(person_id)}
    resp = self.s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def names_view_one(self, name_id: int) -> dict:
    """
    Retrieve Names attached to a CO Person or Org Identity.

    :param name_id:
    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      Name Response           Name returned
        401 Unauthorized                                    Authentication required
        404 Name Unknown                                    id not found
        500 Other Error                                     Unknown error
    """
    url = self.CO_API_URL + '/names/' + str(name_id) + '.json'
    resp = self.s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()