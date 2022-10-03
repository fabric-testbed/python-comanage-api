# comanage_api/_cogroupmember.py

"""
CoGroupMember API - https://spaces.at.internet2.edu/display/COmanage/CoGroupMember+API

Methods
-------
cogroupmember_add(group_id: int, person_id: int) -> dict
    Add a new CoGroupMember (ie: a member of a CO group).
cogroupmember_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove a CoGroupMember.
cogroupmember_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing CoGroupMember.
cogroupmember_view_all() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve all existing CoGroupMembers.
cogroupmember_view_per_group(group_id: int) -> dict
    Retrieve CoGroupMembers attached to a CoGroup.
cogroupmember_view_one() -> dict
    ### NOT IMPLEMENTED ###
    Retrieve an existing CoGroupMember.
"""

import json


def cogroupmember_add(self, group_id: int, person_id: int) -> dict:
    """
    Add a new CoGroupMember (ie: a member of a CO group).
    group_id: COmanage COGroup Id
    person_id: COmanage COPerson Id
    :request
        {
            "RequestType":"CoGroupMembers",
            "Version":"1.0",
            "CoGroupMembers":
            [
                {
                    "Version":"1.0",
                    "CoGroupId":"<CoGroupId>",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    "Member":true|false,
                    "Owner":true|false,
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>"
                }
            ]
        }:
    Response Format
        HTTP Status                  Response Body        Description
        201  Added                   NewObjectResponse    CoGroupMember added
        400  Bad Request                                  CoGroupMember Request not
                                                            provided in POST body
        400  Invalid Fields          ErrorResponse        An error in one or more
                                                            provided fields
        401  Unauthorized                                 Authentication required
        403  CoGroup Does Not Exist                       The specified CoGroup does not exist
        403  CoPerson Does Not Exist                      The specified CoPerson does not exist
        403  CoPerson Already Member                      The specified CoPerson is already a
                                                            member of the specified CoGroup
        500  Other Error                                  Unknown error
    """

    post_body = {
            "RequestType":"CoGroupMembers",
            "Version":"1.0",
            "CoGroupMembers":
            [
                {
                    "Version":"1.0",
                    "CoGroupId":"<CoGroupId>",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    "Member":True,
                    "Owner":False
                }
            ]
        }

    post_body['CoGroupMembers'][0]['CoGroupId'] = group_id
    post_body['CoGroupMembers'][0]['Person']['Id'] = person_id

    post_body = json.dumps(post_body)
    url = self._CO_API_URL + '/co_group_members.json'
    resp = self._s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def cogroupmember_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a CoGroupMember.

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


def cogroupmember_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing CoGroupMember.

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


def cogroupmember_view_all(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve all existing CoGroupMembers.

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


def cogroupmember_view_per_group(self, group_id: int) -> dict:
    """
    Retrieve CoGroupMembers attached to a CoGroup.
    group_id: COmanage COGroup Id
    :request
        {
            "RequestType":"CoGroupMembers",
            "Version":"1.0",
            "CoGroupMembers":
            [
                {
                    "Version":"1.0",
                    "CoGroupId":"<CoGroupId>",
                    "Person":
                    {
                        "Type":"CO",
                        "Id":"<ID>"
                    },
                    "Member":true|false,
                    "Owner":true|false,
                    "ValidFrom":"<ValidFrom>",
                    "ValidThrough":"<ValidThrough>"
                }
            ]
        }:
    Response Format
        HTTP Status                  Response Body          Description
        200  OK                      CoGroupMemberResponse  CoGroupMember returned
        401  Unauthorized                                   Authentication required
        403  CoGroup Unknown                                id not found
        500  Other Error                                    Unknown error
    """

    url = self._CO_API_URL + '/co_group_members.json'
    params = {'cogroupid': group_id}
    resp = self._s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def cogroupmember_view_one(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Retrieve an existing CoGroupMember.

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
