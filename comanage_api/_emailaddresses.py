# comanage_api/_emailaddresses.py

"""
EmailAddress API - https://spaces.at.internet2.edu/display/COmanage/EmailAddress+API

Methods
-------
email_addresses_add() -> dict
    Add a new EmailAddress.
email_addresses_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove an EmailAddress.
email_addresses_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing EmailAddress.
email_addresses_view_all() -> dict
    Retrieve all existing EmailAddresses.
email_addresses_view_per_person(person_type: str, person_id: int) -> dict
    Retrieve EmailAddresses attached to a CO Department, CO Person, or Org Identity.
email_addresses_view_one(email_address_id: int) -> dict
    Retrieve an existing EmailAddress.
"""

import json


def email_addresses_add(self, email_address: str, person_type: str, person_id: int) -> dict:
    """
    Add a new EmailAddress

    :param self:
    :param email_address:
    :param person_type:
    :param person_id:
    :return
        {
            "RequestType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Mail":"<Mail>",
                    "Type":"<Type>",
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
                        "Id":"<ID>"
                    }
                }
            ]
        }:

    Response Format
        HTTP Status                  Response Body        Description
        201  Added                   NewObjectResponse    EmailAddress added
        400  Bad Request                                  EmailAddress Request not
                                                          provided in POST body
        400  Invalid Fields          ErrorResponse        An error in one or more provided fields
        401  Unauthorized                                 Authentication required
        403  No Person Specified                          Either a CO Person or an Org Identity
                                                          must be specified to attach the
                                                          Email Address to
        403  Person Does Not Exist                        The specified CO Department, CO Person,
                                                          or Org Identity does not exist
        500  Other Error                                  Unknown error
    """
    post_body = {
        "RequestType":"EmailAddresses",
        "Version":"1.0",
        "EmailAddresses":
        [
            {
                "Version":"1.0",
                "Mail":"<Mail>",
                "Type":"official",
                "Description":"",
                "Verified": False,
                "Person":
                {
                    "Type":"<Type>",
                    "Id":"<ID>"
                }
            }
        ]
    }

    post_body['EmailAddresses'][0]['Mail'] = email_address
    post_body['EmailAddresses'][0]['Person']['Type'] = person_type
    post_body['EmailAddresses'][0]['Person']['Id'] = person_id

    post_body = json.dumps(post_body)
    url = self._CO_API_URL + '/email_addresses.json'
    resp = self._s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)

    resp.raise_for_status()


def email_addresses_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove an EmailAddress.

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


def email_addresses_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing EmailAddress.

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


def email_addresses_view_all(self) -> dict:
    """
    Retrieve all existing EmailAddresses.

    :param self:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
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
        200 OK              EmailAddress Response   EmailAddresses returned
        401 Unauthorized                            Authentication required
        500 Other Error                             Unknown error
    """
    url = self._CO_API_URL + '/email_addresses.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def email_addresses_view_per_person(self, person_type: str, person_id: int) -> dict:
    """
    Retrieve EmailAddresses attached to a CO Department, CO Person, or Org Identity.

    :param self:
    :param person_type:
    :param person_id:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
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
        200 OK                      EmailAddress Response     EmailAddress returned
        204 CO Department                                   The requested CO Department was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 CO Person                                       The requested CO Person was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 Organization                                    The requested Organization was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 Org Identity                                    The requested Org Identity was found,
            Has No EmailAddress                                   but has no email addresses attached
        401 Unauthorized                                    Authentication required
        404 CO Department Unknown                           id not found for CO Department
        404 CO Person Unknown                               id not found for CO Person
        404 Organization Unknown                            id not found for Organization
        404 Org Identity Unknown                            id not found for Org Identity
        500 Other Error                                     Unknown error
    """
    if not person_type:
        person_type = 'copersonid'
    else:
        person_type = str(person_type).lower()
    if person_type not in self.EMAILADDRESS_OPTIONS:
        raise TypeError("Invalid Fields 'person_type'")
    url = self._CO_API_URL + '/email_addresses.json'
    params = {str(person_type): str(person_id)}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def email_addresses_view_one(self, email_address_id: int) -> dict:
    """
    Retrieve an existing EmailAddress.

    :param self:
    :param emailaddress_id:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                }
            ]
        }:

    Response Format
        HTTP Status                 Response Body               Description
        200 OK                      EmailAddress Response       EmailAddress returned
        401 Unauthorized                                        Authentication required
        404 EmailAddress Unknown                                id not found
        500 Other Error                                         Unknown error
    """
    url = self._CO_API_URL + '/email_addresses/' + str(email_address_id) + '.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()
