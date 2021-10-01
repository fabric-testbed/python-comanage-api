# comanage_api/_cous.py
# COU API - https://spaces.at.internet2.edu/display/COmanage/COU+API

import json


def cous_add(self, name: str, description: str, parent_id: int = None) -> dict:
    """
    Add a new Cou.

    :param name:
    :param description:
    :param parent_id:
    :return
        {
            "ResponseType":"NewObject",
            "Version":"1.0",
            "ObjectType":"Cou",
            "Id":"<INTEGER>"
        }:

    Request Format
        {
          "RequestType":"Cous",
          "Version":"1.0",
          "Cous":
          [
            {
              "Version":"1.0",
              "CoId":"<CO_API_ORG_ID>",
              "ParentId":"<parent_id>",
              "Name":"<name>",
              "Description":"<description>",
            }
          ]
        }

    Response Format
        HTTP Status             Response Body                       Description
        201 Added               NewObjectResponse with ObjectType   Cou added
        400 Bad Request                                             Cou Request not provided in POST body
        400 Invalid Fields      ErrorRespons with details in        An error in one or more provided fields
                                InvalidFields element
        401 Unauthorized                                            Authentication required
        403 CO Does Not Exist                                       The specified CO does not exist
        403 Name In Use                                             A COU already exists with the specified name in
                                                                    the specified CO
        403 Parent Would                                            Parent COU can not be a descendant of the child
        Create Cycle
        403 Wrong CO                                                Parent/Child COU not member of same CO
        500 Other Error                                             Unknown error
    """
    post_body = {
        'RequestType': 'Cous',
        'Version': '1.0',
        'Cous':
            [
                {
                    'Version': '1.0',
                    'CoId': self.CO_API_ORG_ID,
                    'Name': str(name),
                    'Description': str(description)
                }
            ]
    }
    if parent_id:
        post_body['Cous'][0]['ParentId'] = str(parent_id)
    post_body = json.dumps(post_body)
    url = self.CO_API_URL + '/cous.json'
    resp = self.s.post(
        url=url,
        data=post_body
    )
    if resp.status_code == 201:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def cous_delete(self, cou_id: int) -> bool:
    """
    Remove a Cou.

    :param cou_id:
    :return:

    Response Format
        HTTP Status                 Response Body       Description
        200 Deleted                                     Cou deleted
        400 Invalid Fields                              id not provided
        401 Unauthorized                                Authentication required
        403 CoPersonRole Exists                         One or more CO Person Roles are members of this COU,
                                                        and so the COU cannot be removed
        404 Identifier Unknown                          id not found
        500 Other Error                                 Unknown error
    """
    url = self.CO_API_URL + '/cous/' + str(cou_id) + '.json'
    params = {'coid': self.CO_API_ORG_ID}
    resp = self.s.delete(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def cous_edit(self, cou_id: int, name: str = None, description: str = None, parent_id: int = None) -> bool:
    """
    Edit an existing Cou.

    :param cou_id:
    :param name:
    :param description:
    :param parent_id:
    :return
        {
            "status_code": 200,
            "reason": "OK"
        }:

    Request Format
        {
          "RequestType":"Cous",
          "Version":"1.0",
          "Cous":
          [
            {
              "Version":"1.0",
              "CoId":"<CO_API_ORG_ID>",
              "ParentId":"<parent_id>",
              "Name":"<name>",
              "Description":"<description>",
            }
          ]
        }

    Response Format
        HTTP Status             Response Body                       Description
        200 OK                                                      Cou updated
        400 Bad Request                                             Cou Request not provided in POST body
        400 Invalid Fields      ErrorRespons with details in        An error in one or more provided fields
                                InvalidFields element
        401 Unauthorized                                            Authentication required
        403 CO Does Not Exist                                       The specified CO does not exist
        403 Name In Use                                             A COU already exists with the specified name in
                                                                    the specified CO
        403 Parent Would                                            Parent COU can not be a descendant of the child
        Create Cycle
        403 Wrong CO                                                Parent/Child COU not member of same CO
        404 Identifier Unknown                                      id not found
        500 Other Error                                             Unknown error
    """
    cou = cous_view_one(self, cou_id)
    post_body = {
        'RequestType': 'Cous',
        'Version': '1.0',
        'Cous':
            [
                {
                    'Version': '1.0',
                    'CoId': self.CO_API_ORG_ID
                }
            ]
    }
    if name:
        post_body['Cous'][0]['Name'] = str(name)
    else:
        post_body['Cous'][0]['Name'] = cou.get('Cous')[0].get('Name')
    if description:
        post_body['Cous'][0]['Description'] = str(description)
    else:
        post_body['Cous'][0]['Description'] = cou.get('Cous')[0].get('Description')
    if parent_id:
        post_body['Cous'][0]['ParentId'] = str(parent_id)
    else:
        if cou.get('Cous')[0].get('ParentId'):
            post_body['Cous'][0]['ParentId'] = str(cou.get('Cous')[0].get('ParentId'))
        if str(parent_id) == '0':
            post_body['Cous'][0]['ParentId'] = ''
    post_body = json.dumps(post_body)
    url = self.CO_API_URL + '/cous/' + str(cou_id) + '.json'
    resp = self.s.put(
        url=url,
        data=post_body
    )
    if resp.status_code == 200:
        return True
    else:
        resp.raise_for_status()


def cous_view_all(self) -> dict:
    """
    Retrieve Cou attached to a CO.

    :return
    {
        "ResponseType":"Cous",
        "Version":"1.0",
        "Cous":[
            {
                "Version":"1.0",
                "Id":"<INTEGER>",
                "CoId":"<CO_API_ORG_ID>",
                "Name":"<name>",
                "Description":"<description>",
                "Lft":"64",
                "Rght":"65",
                "Created":"2021-09-14 14:53:02",
                "Modified":"2021-09-14 14:53:02",
                "Revision":"0",
                "Deleted":false,
                "ActorIdentifier":"<COmanage_ID>"
            },
            {
                ...
            }
        ]
    }:

    Response Format
        HTTP Status         Response Body       Description
        200 OK              Cou Response        Cou returned
        401 Unauthorized                        Authentication required
        404 CO Unknown                          id not found
        500 Other Error                         Unknown error
    """
    url = self.CO_API_URL + '/cous.json'
    params = {'coid': self.CO_API_ORG_ID}
    resp = self.s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()


def cous_view_one(self, cou_id: int) -> dict:
    """
    Retrieve an existing Cou.

    :param cou_id:
    :return
    {
        "ResponseType":"Cous",
        "Version":"1.0",
        "Cous":[
            {
                "Version":"1.0",
                "Id":"<INTEGER>",
                "CoId":"<CO_API_ORG_ID>",
                "Name":"<name>",
                "Description":"<description>",
                "Lft":"64",
                "Rght":"65",
                "Created":"2021-09-14 14:53:02",
                "Modified":"2021-09-14 14:53:02",
                "Revision":"0",
                "Deleted":false,
                "ActorIdentifier":"<COmanage_ID>"
            }
        ]
    }:

    Response Format
        HTTP Status         Response Body       Description
        200 OK              Cou Response        Cou returned
        401 Unauthorized                        Authentication required
        404 COU Unknown                         id not found
        500 Other Error                         Unknown error
    """
    url = self.CO_API_URL + '/cous/' + str(cou_id) + '.json'
    params = {'coid': self.CO_API_ORG_ID}
    resp = self.s.get(
        url=url,
        params=params
    )
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        resp.raise_for_status()