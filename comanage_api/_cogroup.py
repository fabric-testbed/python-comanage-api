# comanage_api/_cogroup.py

"""
CoGroup API - https://spaces.at.internet2.edu/display/COmanage/CoGroup+API

Methods
-------
cogroup_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new CoGroup.
cogroup_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove a CoGroup.
cogroup_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing CoGroup.
cogroup_reconcile_all() -> bool
    ### NOT IMPLEMENTED ###
    Reconcile all membership groups.
cogroup_reconcile_one() -> bool
    ### NOT IMPLEMENTED ###
    Reconcile memberships for a CoGroup.
cogroup_view_all() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve all existing CoGroups.
cogroup_view_per_co() -> dict
    Retrieve CoGroups attached to a CO.
cogroup_view_per_coperson() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve Groups attached to a CO Person.
cogroup_view_per_identifier() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve all existing CO Groups attached to the specified identifier.
cogroup_view_one() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve an existing CoGroup.
"""

import json

def cogroup_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new CoGroup.

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

def cogroup_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a CoGroup.

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

def cogroup_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CoGroup.

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

def cogroup_reconcile_all(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Reconcile all membership groups.

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

def cogroup_reconcile_one(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Reconcile memberships for a CoGroup.

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

def cogroup_view_all(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve all existing CoGroups.

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

def cogroup_view_per_co(self) -> dict:
    """
    Retrieve CoGroups attached to a CO.

    :param self:
    :request
        {
            "RequestType":"CoGroups",
            "Version":"1.0",
            "CoGroups":
            [
                {
                "Version":"1.0",
                "CoId":"<CoID>",
                "Name":"<Name>",
                "Description":"<Description>",
                "Open":true|false,
                "Status":("Active"|"Suspended"),
                "CouId":"<CouID>"
                }
            ]
        }:

    Response Format
        HTTP Status             Response Body           Description
        200 OK                  CoGroup Response        CoGroup returned
        401 Unauthorized                                Authentication required
        404 CO Unknown                                  id not found
        500 Other Error                                 Unknown error
    """

    url = self._CO_API_URL + '/co_groups.json'
    params = {'coid': self._CO_API_ORG_ID}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)

    resp.raise_for_status()

def cogroup_view_per_coperson(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve Groups attached to a CO Person.

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

def cogroup_view_per_identifier(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve all existing CO Groups attached to the specified identifier.

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

def cogroup_view_one(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve an existing CoGroup.

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
