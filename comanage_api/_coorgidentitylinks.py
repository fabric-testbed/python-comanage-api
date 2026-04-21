# comanage_api/_coorgidentitylinks.py

"""
CoOrgIdentityLink API - https://spaces.at.internet2.edu/display/COmanage/CoOrgIdentityLink+API

Methods
-------
coorg_identity_links_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new CO Org Identity Link.
    A person must have an Org Identity and a CO Person record before they can be linked.
    Note that invitations are a separate operation.
coorg_identity_links_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove a CO Org Identity Link.
coorg_identity_links_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing CO Identity Link.
coorg_identity_links_view_all() -> dict
    Retrieve all existing CO Identity Links.
coorg_identity_links_view_by_identity(identifier_id: int) -> dict
    Retrieve all existing CO Identity Links for a CO Person or an Org Identity.
coorg_identity_links_view_one(org_identity_id: int) -> dict
    Retrieve an existing CO Identity Link.
"""


def coorg_identity_links_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new CO Org Identity Link.
    A person must have an Org Identity and a CO Person record before they can be linked.
    Note that invitations are a separate operation.

    :param self:
    """
    raise NotImplementedError("coorg_identity_links_add() is not implemented")


def coorg_identity_links_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a CO Org Identity Link.

    :param self:
    """
    raise NotImplementedError("coorg_identity_links_delete() is not implemented")


def coorg_identity_links_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CO Identity Link.

    :param self:
    """
    raise NotImplementedError("coorg_identity_links_edit() is not implemented")


def coorg_identity_links_view_all(self) -> dict:
    """
    Retrieve all existing CO Identity Links.

    :param self:
    :return
        {
            "ResponseType":"CoOrgIdentityLinks",
            "Version":"1.0",
            "CoOrgIdentityLinks":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "CoPersonId":"<CoPersonId>",
                    "OrgIdentityId":"<OrgIdentityId>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status         Response Body                   Description
        200 OK              CoOrgIdentityLink Response      CoOrgIdentityLinks returned
        401 Unauthorized                                    Authentication required
        500 Other Error                                     Unknown error
    """
    return self._get('co_org_identity_links.json')


def coorg_identity_links_view_by_identity(self, identity_type: str, identity_id: int) -> dict:
    """
    Retrieve all existing CO Identity Links for a CO Person or an Org Identity.

    :param self:
    :param identity_type:
    :param identity_id:
    :return
       {
            "ResponseType":"CoOrgIdentityLinks",
            "Version":"1.0",
            "CoOrgIdentityLinks":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "CoPersonId":"<CoPersonId>",
                    "OrgIdentityId":"<OrgIdentityId>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status                 Response Body                   Description
        200 OK                      CoOrgIdentityLink Response      CoOrgIdentityLinks returned
        401 Unauthorized                                            Authentication required
        404 CO Person Unknown                                       copersonid not found
        404 Org Identity Unknown                                    orgidentityid not found
        500 Other Error                                             Unknown error
    """
    return self._get_by_entity('co_org_identity_links.json', identity_type, identity_id,
                               self.PERSON_OPTIONS, 'identity_type')


def coorg_identity_links_view_one(self, coorg_identity_link_id: int) -> dict:
    """
    Retrieve an existing CO Identity Link.

    :param self:
    :param coorg_identity_link_id:
    :return
        {
            "ResponseType":"CoOrgIdentityLinks",
            "Version":"1.0",
            "CoOrgIdentityLinks":
            [
                {
                    "Version":"1.0",
                    "Id":"<Id>",
                    "CoPersonId":"<CoPersonId>",
                    "OrgIdentityId":"<OrgIdentityId>",
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                }
            ]
        }:

    Response Format
        HTTP Status                     Response Body                   Description
        200 OK                          CoOrgIdentityLink Response      CoOrgIdentityLinks returned
        401 Unauthorized                                                Authentication required
        404 CoOrgIdentityLink Unknown                                   id not found
        500 Other Error                                                 Unknown error
    """
    return self._get(f'co_org_identity_links/{coorg_identity_link_id}.json')
