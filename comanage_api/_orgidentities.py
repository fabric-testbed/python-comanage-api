# comanage_api/_orgidentities.py

"""
OrgIdentity API - https://spaces.at.internet2.edu/display/COmanage/OrgIdentity+API

Methods
-------
org_identities_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new Organizational Identity. A person must have an OrgIdentity before they can be added to a CO.
org_identities_delete() -> bool
    ### NOT IMPLEMENTED ###
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
org_identities_view_per_identifier(identifier_id: int) -> dict
    Retrieve all existing Organizational Identities attached to the specified identifier.
    Note the specified identifier must be attached to an Org Identity, not a CO Person.
org_identities_view_one(org_identity_id: int) -> dict
    Retrieve an existing Organizational Identity.
"""


def org_identities_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new Organizational Identity. A person must have an OrgIdentity before they can be added to a CO.

    :param self:
    """
    raise NotImplementedError("org_identities_add() is not implemented")


def org_identities_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove an Organizational Identity.
    The person must be removed from any COs (CoPerson) before the OrgIdentity record can be removed.
    This method will also delete related data, such as Addresses, EmailAddresses, and TelephoneNumbers.

    :param self:
    """
    raise NotImplementedError("org_identities_delete() is not implemented")


def org_identities_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing Organizational Identity.

    :param self:
    """
    raise NotImplementedError("org_identities_edit() is not implemented")


def org_identities_view_all(self) -> dict:
    """
    Retrieve all existing Organizational Identities.

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
    return self._get('org_identities.json')


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
    return self._get('org_identities.json', params={'coid': self._CO_API_ORG_ID})


def org_identities_view_per_identifier(self, identifier_id: int) -> dict:
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
    return self._get('org_identities.json', params={
        'coid': self._CO_API_ORG_ID,
        'search.identifier': int(identifier_id)
    })


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
    return self._get(f'org_identities/{org_identity_id}.json', params={'coid': self._CO_API_ORG_ID})
