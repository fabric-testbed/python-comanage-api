# comanage_api/_copeople.py

"""
CoPerson API - https://spaces.at.internet2.edu/display/COmanage/CoPerson+API

Methods
-------
copeople_add() -> dict
    Add a new CO Person. A person must have an OrgIdentity before they can be added to a CO.
    Note that linking to an OrgIdentity and invitations are separate operations.
copeople_delete(coperson_id: int) -> bool
    Remove a CO Person. This method will also delete related data, such as CoPersonRoles, EmailAddresses,
    and Identifiers. A person must be removed from any COs (CoPerson records must be deleted)
    before the OrgIdentity record can be removed.
copeople_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing CO Person.
copeople_find() -> dict
    ### NOT IMPLEMENTED ###
    Search for existing CO Person records.
    When too many records are found, a message may be returned rather than specific records.
copeople_match(given: str = None, family: str = None, mail: str = None, distinct_by_id: bool = True) -> dict
    Attempt to match existing CO Person records.
    Note that matching is not performed on search criteria of less than 3 characters,
    or for email addresses that are not syntactically valid.
copeople_view_all() -> dict
    Retrieve all existing CO People.
copeople_view_per_co() -> dict
    Retrieve all existing CO People for the specified CO.
copeople_view_per_identifier(identifier: str, distinct_by_id: bool = True) -> dict
    Retrieve all existing CO People attached to the specified identifier.
    Note the specified identifier must be attached to a CO Person, not an Org Identity.
copeople_view_one(coperson_id: int) -> dict
    Retrieve an existing CO Person.
"""

import json


def copeople_add(self) -> dict:
    """
    Add a new CO Person. A person must have an OrgIdentity before they can be added to a CO.
    Note that linking to an OrgIdentity and invitations are separate operations.

    :request
        {
            "RequestType":"CoPeople",
            "Version":"1.0",
            "CoPeople":
            [
                {
                    "Version":"1.0",
                    "CoId":"<CoId>",
                    "Timezone":"<Timezone>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|
                            "Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Locked"|"Pending"|
                            "PendingApproval"|"PendingConfirmation"|
                            "PendingVetting"|"Suspended")
                }
            ]
        }:

    Response Format
        HTTP Status                  Response Body        Description
        201  Added                   NewObjectResponse    CoPerson created
        400  Bad Request                                  CoPerson Request not
                                                            provided in POST body
        400  Invalid Fields          ErrorResponse        An error in one or more
                                                            provided fields
        401  Unauthorized                                 Authentication required
        403  Co Does Not Exist                            The specified Co does not exist
        500  Other Error                                  Unknown error
    """
    post_body = {
        "RequestType":"CoPeople",
        "Version":"1.0",
        "CoPeople":
        [
            {
                "Version":"1.0",
                "CoId":"<CoId>",
                "Status":"Active"
            }
        ]
    }

    post_body['CoPeople'][0]['CoId'] = self._CO_API_ORG_ID

    post_body = json.dumps(post_body)
    url = self._CO_API_URL + '/co_people.json'
    resp = self._s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_delete(self, coperson_id: int) -> bool:
    """
    Remove a CO Person. This method will also delete related data, such as CoPersonRoles, EmailAddresses,
    and Identifiers. A person must be removed from any COs (CoPerson records must be deleted)
    before the OrgIdentity record can be removed.

    :request
        {
            "RequestType":"CoPeople",
            "Version":"1.0",
            "CoPeople":
            [
                {
                    "Version":"1.0",
                    "CoId":"<CoId>",
                    "Timezone":"<Timezone>",
                    "DateOfBirth":"<DateOfBirth>",
                    "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|
                            "Duplicate"|"Expired"|"GracePeriod"|"Invited"|"Locked"|"Pending"|
                            "PendingApproval"|"PendingConfirmation"|
                            "PendingVetting"|"Suspended")
                }
            ]
        }:

    Response Format
        HTTP Status                  Response Body        Description
        200  Deleted                                      OrgPerson deleted
        400  Invalid Fields                               id not provided
        401  Unauthorized                                 Authentication required
        403  CoPersonRole Exists                          The Person has one or more Person
                                                            Role records and cannot be deleted
        403  CouPerson Exists in Unowned COU               The Person has a role in one
                                                            or more COUs that the authenitcated
                                                            user does not control
        404  OrgIdentity Unknown                          id not found
        500  Other Error                                  Unknown error
    """

    url = self._CO_API_URL + '/co_people/' + str(coperson_id) + '.json'
    resp = self._s.delete(
        url=url
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def copeople_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CO Person.

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


def copeople_find(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Search for existing CO Person records.
    When too many records are found, a message may be returned rather than specific records.

    :param self:
    :return
        501 Server Error: Not Implemented for url: mock://not_implemented_501.local:
    """
    url = self._MOCK_501_URL
    resp = self._mock_session.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_match(self, given: str = None, family: str = None, mail: str = None, distinct_by_id: bool = True) -> dict:
    """
    Attempt to match existing CO Person records.
    Note that matching is not performed on search criteria of less than 3 characters,
    or for email addresses that are not syntactically valid.

    :param self:
    :param given:
    :param family:
    :param mail:
    :param distinct_by_id:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoPerson Response       CoPerson returned (zero or more matches may be returned)
        401 Unauthorized                                Authentication required
        404 CO Unknown                                  id not found - Not currently implemented
                                                            -- unknown CO will return an empty set
        500 Other Error                                 Unknown error
    """
    url = self._CO_API_URL + '/co_people.json'
    params = {'coid': self._CO_API_ORG_ID}
    if given:
        params.update({'given': given})
    if family:
        params.update({'family': family})
    if mail:
        params.update({'mail': mail})
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        if distinct_by_id:
            resp_dict = json.loads(resp.text)
            distinct_copeople = list({v['Id']: v for v in resp_dict.get('CoPeople')}.values())
            resp_dict['CoPeople'] = distinct_copeople
            return resp_dict
        else:
            return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_view_all(self) -> dict:
    """
    Retrieve all existing CO People.

    :param self:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoPerson Response       CoPerson returned
        401 Unauthorized                                Authentication required
        500 Other Error                                 Unknown error
    """
    url = self._CO_API_URL + '/co_people.json'
    resp = self._s.get(
        url=url
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_view_per_co(self) -> dict:
    """
    Retrieve all existing CO People for the specified CO.

    :param self:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoPerson Response       CoPerson returned (zero or more matches may be returned)
        401 Unauthorized                                Authentication required
        404 CO Unknown                                  id not found - Not currently implemented
                                                            -- unknown CO will return an empty set
        500 Other Error                                 Unknown error
    """
    url = self._CO_API_URL + '/co_people.json'
    params = {'coid': self._CO_API_ORG_ID}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_view_per_identifier(self, identifier: str, distinct_by_id: bool = True) -> dict:
    """
    Retrieve all existing CO People attached to the specified identifier.
    Note the specified identifier must be attached to a CO Person, not an Org Identity.

    :param self:
    :param identifier:
    :param distinct_by_id:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      CoPerson Response       CoPerson returned
        401 Unauthorized                                    Authentication required
        404 CO Unknown                                      id not found
        500 Other Error                                     Unknown error
    """
    url = self._CO_API_URL + '/co_people.json'
    params = {'coid': self._CO_API_ORG_ID, 'search.identifier': identifier}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        if distinct_by_id:
            resp_dict = json.loads(resp.text)
            distinct_copeople = list({v['Id']: v for v in resp_dict.get('CoPeople')}.values())
            resp_dict['CoPeople'] = distinct_copeople
            return resp_dict
        else:
            return json.loads(resp.text)
    else:
        resp.raise_for_status()


def copeople_view_one(self, coperson_id: int) -> dict:
    """
    Retrieve an existing CO Person.

    :param self:
    :param coperson_id:
    :return
        {
          "RequestType":"CoPeople",
          "Version":"1.0",
          "CoPeople":
          [
            {
              "Version":"1.0",
              "CoId":"<CoId>",
              "Timezone":"<Timezone>",
              "DateOfBirth":"<DateOfBirth>",
              "Status":("Active"|"Approved"|"Confirmed"|"Declined"|"Deleted"|"Denied"|"Duplicate"|"Expired"|
                  "GracePeriod"|"Invited"|"Locked"|"Pending"|"PendingApproval"|"PendingConfirmation"|"Suspended")
            }
          ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      CoPerson Response       CoPerson returned
        401 Unauthorized                                    Authentication required
        404 copeople Unknown                                id not found
        500 Other Error                                     Unknown error
    """
    url = self._CO_API_URL + '/co_people/' + str(coperson_id) + '.json'
    params = {'coid': self._CO_API_ORG_ID}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()
