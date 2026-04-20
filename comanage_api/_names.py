# comanage_api/_names.py

"""
Name API - https://spaces.at.internet2.edu/display/COmanage/Name+API

Methods
-------
names_add(person_type: str, person_id: int, given: str, family: str) -> dict
    Add a new Name.
names_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove a Name.
names_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing Name.
names_view_all() -> dict
    Retrieve all existing Names.
names_view_per_person(person_type: str, person_id: int) -> dict
    Retrieve Names attached to a CO Person or Org Identity.
names_view_one(name_id: int) -> dict
    Retrieve Names attached to a CO Person or Org Identity.
"""

import json


def names_add(self, person_type: str, person_id: int, given: str, family: str) -> dict:
    """
        Add a new Name.

        person_type: Type of person (i.e. "CO"|"Org")
        person_id: COmanage ID for the person_type
        given: First name for the person
        family: Last name for the person
        :request
            {
                "RequestType":"Names",
                "Version":"1.0",
                "Names":
                [
                    {
                        "Version":"1.0",
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
                    }
                ]
            }:

        Response Format
            HTTP Status                  Response Body        Description
            201  Added                   NewObjectResponse    Name added
            400  Bad Request                                  Name Request not
                                                              provided in POST body
            400  Invalid Fields          ErrorResponse        An error in one or more
                                                              provided fields
            401  Unauthorized                                 Authentication required
            403  No Person Specified                          Either a CO Person or an Org Identity
                                                              must be specified to attach the
                                                              Name to
            403  Person Does Not Exist                        The specified CO Person or
                                                              Org Identity does not exist
            500  Other Error                                  Unknown error
    """
    post_body = {
        "RequestType":"Names",
        "Version":"1.0",
        "Names":
        [
            {
                "Version":"1.0",
                "Honorific":"",
                "Given":"<Given>",
                "Middle":"",
                "Family":"<Family>",
                "Suffix":"",
                "Type":"official",
                "Language":"",
                "PrimaryName": True,
                "Person":
                {
                    "Type":"<Type>",
                    "Id":"<ID>"
                }
            }
        ]
    }

    post_body['Names'][0]['Given'] = given
    post_body['Names'][0]['Family'] = family
    post_body['Names'][0]['Person']['Type'] = person_type
    post_body['Names'][0]['Person']['Id'] = person_id

    post_body = json.dumps(post_body)
    url = self._CO_API_URL + '/names.json'
    resp = self._s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def names_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a Name.

    :param self:
    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self._MOCK_501_URL
    resp = self._mock_session.get(
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

    :param self:
    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self._MOCK_501_URL
    resp = self._mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def names_view_all(self) -> dict:
    """
    Retrieve all existing Names.

    :param self:
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
    url = self._CO_API_URL + '/names.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def names_view_per_person(self, person_type: str, person_id: int) -> dict:
    """
    Retrieve Names attached to a CO Person or Org Identity.

    :param self:
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
    url = self._CO_API_URL + '/names.json'
    params = {str(person_type): str(person_id)}
    resp = self._s.get(
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

    :param self:
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
    url = self._CO_API_URL + '/names/' + str(name_id) + '.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()
