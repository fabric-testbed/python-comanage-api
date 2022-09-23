# comanage_api/_orgidentities.py

"""
OrgIdentity API - https://spaces.at.internet2.edu/display/COmanage/OrgIdentity+API

Methods
-------
org_identities_add() -> dict
    Add a new Organizational Identity. A person must have an OrgIdentity before they can be added to a CO.
org_identities_delete(org_identity_id: int) -> bool
    Remove an Organizational Identity.
    The person must be removed from any COs (CoPerson) before the OrgIdentity record can be removed.
    This method will also delete related data, such as Addresses, EmailAddresses, and TelephoneNumbers.
org_identities_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing Organizational Identity.
org_identities_view_all() -> dict
    Retrieve all existing Organizational Identities.
org_identities_view_per_co(person_type: str, person_id: int) -> dict
    Retrieve all existing Organizational Identities for the specified CO.
org_identities_view_per_identifier(identifier: str) -> dict
    Retrieve all existing Organizational Identities attached to the specified identifier.
    Note the specified identifier must be attached to an Org Identity, not a CO Person.
org_identities_view_one(org_identity_id: int) -> dict
    Retrieve an existing Organizational Identity.
"""

import json


def org_identities_add(self) -> dict:
    """
    Add a new Organizational Identity. A person must have an OrgIdentity before they can be added to a CO.

    :request
    {
        "RequestType":"OrgIdentities",
        "Version":"1.0",
        "OrgIdentities":
        [
            {
                "Version":"1.0",
                "Affiliation":"<Affiliation>",
                "Title":"<Title>",
                "O":"<O>",
                "Ou":"<Ou>",
                "CoId":"<CoId>",
                "ValidFrom":"<ValidFrom>",
                "ValidThrough":"<ValidThrough>",
                "DateOfBirth":"<DateOfBirth>"
            }
        ]
    }:

    Response Format
        HTTP Status                  Response Body        Description
        201  Added                   NewObjectResponse    OrgIdentity added
        400  Bad Request                                  OrgIdentity Request not
                                                            provided in POST body
        400  Invalid Fields          ErrorResponse        An error in one or more
                                                            provided fields
        401  Unauthorized                                 Authentication required
        403  CO Does Not Exist                            The specified CO does not exist
        500  Other Error                                  Unknown error
    """
    post_body = {
        "RequestType":"OrgIdentities",
        "Version":"1.0",
        "OrgIdentities":
        [
            {
                "Version":"1.0",
                "Affiliation":"member",
                "CoId":"<CoId>"
            }
        ]
    }

    post_body['OrgIdentities'][0]['CoId'] = self._CO_API_ORG_ID

    post_body = json.dumps(post_body)
    url = self._CO_API_URL + '/org_identities.json'
    resp = self._s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def org_identities_delete(self, org_identity_id: int) -> bool:
    """
    Remove an Organizational Identity. The person must be removed from any COs (CoPerson)
    before the OrgIdentity record can be removed. This method will also delete related data,
    such as Addresses, EmailAddresses, and TelephoneNumbers.

    :request
        {
            "RequestType":"OrgIdentities",
            "Version":"1.0",
            "OrgIdentities":
            [
                {
                "Version":"1.0",
                "Affiliation":"<Affiliation>",
                "Title":"<Title>",
                "O":"<O>",
                "Ou":"<Ou>",
                "CoId":"<CoId>",
                "ValidFrom":"<ValidFrom>",
                "ValidThrough":"<ValidThrough>",
                "DateOfBirth":"<DateOfBirth>"
                }
            ]
        }

    Response Format
        HTTP Status                  Response Body        Description
        200  Deleted                                      OrgIdentity deleted
        400  Invalid Fields                               id not provided
        401  Unauthorized                                 Authentication required
        403  CoPerson Exists         ErrorResponse        id must not be attached to any
                                                            CoPerson. (Delete the CoPerson first.)
        404  OrgIdentity Unknown                          id not found
        500  Other Error                                  Unknown error
    """

    url = self._CO_API_URL + '/org_identities/' + str(org_identity_id) + '.json'
    resp = self._s.delete(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def org_identities_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing Organizational Identity.

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


def org_identities_view_all(self) -> dict:
    """
    Retrieve all existing EmailAddresses.

    :param self:
    :return
        {
            "ResponseType":"OrgIdentities",
            "Version":"1.0",
            "OrgIdentities":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "Affiliation":"<Affiliation>",
                    "Title":"<Title>",
                    "O":"<O>",
                    "Ou":"<Ou>",
                    "CoId":"<CoId>",
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body           Description
        200 OK              OrgIdentity Response    OrgIdentity returned
        401 Unauthorized                            Authentication required
        500 Other Error                             Unknown error
    """
    url = self._CO_API_URL + '/org_identities.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def org_identities_view_per_co(self) -> dict:
    """
    Retrieve all existing Organizational Identities for the specified CO.

    :param self:
    :return
        {
            "ResponseType":"OrgIdentities",
            "Version":"1.0",
            "OrgIdentities":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "Affiliation":"<Affiliation>",
                    "Title":"<Title>",
                    "O":"<O>",
                    "Ou":"<Ou>",
                    "CoId":"<CoId>",
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body           Description
        200 OK              OrgIdentity Response    OrgIdentity returned
        401 Unauthorized                            Authentication required
        404 CO Unknown                              id not found
        500 Other Error                             Unknown error
    """
    url = self._CO_API_URL + '/org_identities.json'
    params = {'coid': self._CO_API_ORG_ID}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def org_identities_view_per_identifier(self, identifier: str) -> dict:
    """
    Retrieve all existing Organizational Identities attached to the specified identifier.
    Note the specified identifier must be attached to an Org Identity, not a CO Person.

    :param self:
    :param identifier_id:
    :return
       {
            "ResponseType":"OrgIdentities",
            "Version":"1.0",
            "OrgIdentities":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "Affiliation":"<Affiliation>",
                    "Title":"<Title>",
                    "O":"<O>",
                    "Ou":"<Ou>",
                    "CoId":"<CoId>",
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body           Description
        200 OK              OrgIdentity Response    OrgIdentity returned
        401 Unauthorized                            Authentication required
        404 CO Unknown                              id not found
        500 Other Error                             Unknown error
    """
    url = self._CO_API_URL + '/org_identities.json'
    params = {'coid': self._CO_API_ORG_ID, 'search.identifier': identifier}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def org_identities_view_one(self, org_identity_id: int) -> dict:
    """
    Retrieve an existing Organizational Identity.

    :param self:
    :param org_identity_id:
    :return
        {
            "ResponseType":"OrgIdentities",
            "Version":"1.0",
            "OrgIdentities":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "Affiliation":"<Affiliation>",
                    "Title":"<Title>",
                    "O":"<O>",
                    "Ou":"<Ou>",
                    "CoId":"<CoId>",
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                }
            ]
        }:

    Response Format
        HTTP Status                 Response Body               Description
        200 OK                      OrgIdentity Response        OrgIdentity returned
        401 Unauthorized                                        Authentication required
        404 OrgIdentity Unknown                                 id not found
        500 Other Error                                         Unknown error
    """
    url = self._CO_API_URL + '/org_identities/' + str(org_identity_id) + '.json'
    params = {'coid': self._CO_API_ORG_ID}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()
