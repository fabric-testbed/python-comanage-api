# comanage_api/_cous.py

"""
COU API - https://spaces.at.internet2.edu/display/COmanage/COU+API
"""


class COUsMixin:
    """Mixin providing COU API methods."""

    def cous_add(self, name: str, description: str, parent_id: int = None) -> dict:
        """
        Add a new Cou.

        :param name:
        :param description:
        :param parent_id:

        Response Format
            HTTP Status             Response Body                       Description
            201 Added               NewObjectResponse with ObjectType   Cou added
            400 Bad Request                                             Cou Request not provided in POST body
            401 Unauthorized                                            Authentication required
            403 CO Does Not Exist                                       The specified CO does not exist
            403 Name In Use                                             A COU already exists with the specified name
            500 Other Error                                             Unknown error
        """
        cou = {
            'Version': '1.0',
            'CoId': self._CO_API_ORG_ID,
            'Name': str(name),
            'Description': str(description)
        }
        if parent_id:
            cou['ParentId'] = str(parent_id)
        return self._post('cous.json', {
            'RequestType': 'Cous',
            'Version': '1.0',
            'Cous': [cou]
        })

    def cous_delete(self, cou_id: int) -> bool:
        """
        Remove a Cou.

        :param cou_id:

        Response Format
            HTTP Status                 Response Body       Description
            200 Deleted                                     Cou deleted
            400 Invalid Fields                              id not provided
            401 Unauthorized                                Authentication required
            404 Identifier Unknown                          id not found
            500 Other Error                                 Unknown error
        """
        return self._delete(f'cous/{cou_id}.json', params={'coid': self._CO_API_ORG_ID})

    def cous_edit(self, cou_id: int, name: str = None, description: str = None,
                  parent_id: int = None) -> bool:
        """
        Edit an existing Cou.

        :param cou_id:
        :param name:
        :param description:
        :param parent_id:

        Response Format
            HTTP Status             Response Body                       Description
            200 OK                                                      Cou updated
            400 Bad Request                                             Cou Request not provided in POST body
            401 Unauthorized                                            Authentication required
            403 CO Does Not Exist                                       The specified CO does not exist
            403 Name In Use                                             A COU already exists with the specified name
            404 Identifier Unknown                                      id not found
            500 Other Error                                             Unknown error
        """
        existing = self.cous_view_one(cou_id)
        existing_cou = existing.get('Cous')[0]
        cou = {
            'Version': '1.0',
            'CoId': self._CO_API_ORG_ID,
            'Name': str(name) if name else existing_cou.get('Name'),
            'Description': str(description) if description else existing_cou.get('Description')
        }
        if parent_id is not None and parent_id != 0:
            cou['ParentId'] = str(parent_id)
        elif parent_id == 0:
            cou['ParentId'] = ''
        else:
            if existing_cou.get('ParentId'):
                cou['ParentId'] = str(existing_cou.get('ParentId'))
        return self._put(f'cous/{cou_id}.json', {
            'RequestType': 'Cous',
            'Version': '1.0',
            'Cous': [cou]
        })

    def cous_view_all(self) -> dict:
        """
        Retrieve all existing Cous.

        Response Format
            HTTP Status         Response Body       Description
            200 OK              Cou Response        Cou returned
            401 Unauthorized                        Authentication required
            500 Other Error                         Unknown error
        """
        return self._get('cous.json')

    def cous_view_per_co(self) -> dict:
        """
        Retrieve Cou attached to a CO.

        Response Format
            HTTP Status         Response Body       Description
            200 OK              Cou Response        Cou returned
            401 Unauthorized                        Authentication required
            404 CO Unknown                          id not found
            500 Other Error                         Unknown error
        """
        return self._get('cous.json', params={'coid': self._CO_API_ORG_ID})

    def cous_view_one(self, cou_id: int) -> dict:
        """
        Retrieve an existing Cou.

        :param cou_id:

        Response Format
            HTTP Status         Response Body       Description
            200 OK              Cou Response        Cou returned
            401 Unauthorized                        Authentication required
            404 COU Unknown                         id not found
            500 Other Error                         Unknown error
        """
        return self._get(f'cous/{cou_id}.json', params={'coid': self._CO_API_ORG_ID})
