# comanage_api/_copeople.py

"""
CoPerson API - https://spaces.at.internet2.edu/display/COmanage/CoPerson+API

Methods
-------
copeople_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new CO Person. A person must have an OrgIdentity before they can be added to a CO.
    Note that linking to an OrgIdentity and invitations are separate operations.
copeople_delete() -> bool
    ### NOT IMPLEMENTED ###
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


def copeople_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new CO Person. A person must have an OrgIdentity before they can be added to a CO.
    Note that linking to an OrgIdentity and invitations are separate operations.

    :param self:
    """
    raise NotImplementedError("copeople_add() is not implemented")


def copeople_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a CO Person. This method will also delete related data, such as CoPersonRoles, EmailAddresses,
    and Identifiers. A person must be removed from any COs (CoPerson records must be deleted)
    before the OrgIdentity record can be removed.

    :param self:
    """
    raise NotImplementedError("copeople_delete() is not implemented")


def copeople_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CO Person.

    :param self:
    """
    raise NotImplementedError("copeople_edit() is not implemented")


def copeople_find(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Search for existing CO Person records.
    When too many records are found, a message may be returned rather than specific records.

    :param self:
    """
    raise NotImplementedError("copeople_find() is not implemented")


def _deduplicate_copeople(resp_dict: dict) -> dict:
    distinct_copeople = list({v['Id']: v for v in resp_dict.get('CoPeople')}.values())
    resp_dict['CoPeople'] = distinct_copeople
    return resp_dict


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
    params = {'coid': self._CO_API_ORG_ID}
    if given:
        params['given'] = given
    if family:
        params['family'] = family
    if mail:
        params['mail'] = mail
    resp_dict = self._get('co_people.json', params=params)
    if distinct_by_id:
        return _deduplicate_copeople(resp_dict)
    return resp_dict


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
    return self._get('co_people.json')


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
    return self._get('co_people.json', params={'coid': self._CO_API_ORG_ID})


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
    params = {'coid': self._CO_API_ORG_ID, 'search.identifier': identifier}
    resp_dict = self._get('co_people.json', params=params)
    if distinct_by_id:
        return _deduplicate_copeople(resp_dict)
    return resp_dict


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
    return self._get(f'co_people/{coperson_id}.json', params={'coid': self._CO_API_ORG_ID})
