# comanage_api/_copersonroles.py

"""
CoPersonRole API - https://spaces.at.internet2.edu/display/COmanage/CoPersonRole+API
"""


class CoPersonRolesMixin:
    """Mixin providing CoPersonRole API methods."""

    def coperson_roles_add(self, coperson_id: int, cou_id: int, status: str = None,
                           affiliation: str = None) -> dict:
        """
        Add a new CO Person Role.

        :param coperson_id:
        :param cou_id:
        :param status:
        :param affiliation:

        Response Format
            HTTP Status             Response Body                       Description
            201 Added               NewObjectResponse with ObjectType   CoPersonRole created
            400 Bad Request                                             CoPersonRole Request not provided in POST body
            401 Unauthorized                                            Authentication required
            403 COU Does Not Exist                                      The specified COU does not exist
            500 Other Error                                             Unknown error
        """
        role = {
            'Version': '1.0',
            'Person': {
                'Type': 'CO',
                'Id': str(coperson_id)
            },
            'CouId': str(cou_id),
            'O': str(self._CO_API_ORG_NAME)
        }
        if status:
            if status not in self.STATUS_OPTIONS:
                raise ValueError("Invalid Fields 'status'")
            role['Status'] = str(status)
        else:
            role['Status'] = 'Active'
        if affiliation:
            affiliation = str(affiliation).lower()
            if affiliation not in self.AFFILIATION_OPTIONS:
                raise ValueError("Invalid Fields 'affiliation'")
            role['Affiliation'] = str(affiliation)
        else:
            role['Affiliation'] = 'member'
        return self._post('co_person_roles.json', {
            'RequestType': 'CoPersonRoles',
            'Version': '1.0',
            'CoPersonRoles': [role]
        })

    def coperson_roles_delete(self, coperson_role_id: int) -> bool:
        """
        Remove a CO Person Role.

        :param coperson_role_id:

        Response Format
            HTTP Status                 Response Body       Description
            200 Deleted                                     CoPersonRole deleted
            400 Invalid Fields                              id not provided
            401 Unauthorized                                Authentication required
            404 CoPersonRole Unknown                        id not found
            500 Other Error                                 Unknown error
        """
        return self._delete(f'co_person_roles/{coperson_role_id}.json')

    def coperson_roles_edit(self, coperson_role_id: int, coperson_id: int = None, cou_id: int = None,
                            status: str = None, affiliation: str = None) -> bool:
        """
        Edit an existing CO Person Role.

        :param coperson_role_id:
        :param coperson_id:
        :param cou_id:
        :param status:
        :param affiliation:

        Response Format
            HTTP Status                 Response Body                       Description
            200 OK                                                          CoPersonRole updated
            400 Bad Request                                                 CoPersonRole Request not provided in body
            401 Unauthorized                                                Authentication required
            403 COU Does Not Exist                                          The specified COU does not exist
            404 CoPersonRole Unknown                                        id not found
            500 Other Error                                                 Unknown error
        """
        existing = self.coperson_roles_view_one(coperson_role_id)
        existing_role = existing.get('CoPersonRoles')[0]
        role = {
            'Version': '1.0',
            'Person': {
                'Type': 'CO',
                'Id': str(coperson_id) if coperson_id else str(existing_role.get('Person').get('Id'))
            },
            'CouId': str(cou_id) if cou_id else str(existing_role.get('CouId')),
            'O': str(self._CO_API_ORG_NAME)
        }
        if status:
            if status not in self.STATUS_OPTIONS:
                raise ValueError("Invalid Fields 'status'")
            role['Status'] = str(status)
        else:
            role['Status'] = existing_role.get('Status')
        if affiliation:
            affiliation = str(affiliation).lower()
            if affiliation not in self.AFFILIATION_OPTIONS:
                raise ValueError("Invalid Fields 'affiliation'")
            role['Affiliation'] = str(affiliation)
        else:
            role['Affiliation'] = existing_role.get('Affiliation')
        return self._put(f'co_person_roles/{coperson_role_id}.json', {
            'RequestType': 'CoPersonRoles',
            'Version': '1.0',
            'CoPersonRoles': [role]
        })

    def coperson_roles_view_all(self) -> dict:
        """
        Retrieve all existing CO Person Roles.

        Response Format
            HTTP Status             Response Body                       Description
            200 OK                  CoPersonRole Response               CoPersonRoles returned
            401 Unauthorized                                            Authentication required
            500 Other Error                                             Unknown error
        """
        return self._get('co_person_roles.json')

    def coperson_roles_view_per_coperson(self, coperson_id: int) -> dict:
        """
        Retrieve all existing CO Person Roles for the specified CO Person. Available since Registry v2.0.0.

        :param coperson_id:

        Response Format
            HTTP Status             Response Body                       Description
            200 OK                  CoPersonRole Response               CoPersonRoles returned
            401 Unauthorized                                            Authentication required
            404 CO Person Unknown                                       id not found
            500 Other Error                                             Unknown error
        """
        return self._get('co_person_roles.json', params={'copersonid': int(coperson_id)})

    def coperson_roles_view_per_cou(self, cou_id: int) -> dict:
        """
        Retrieve all existing CO Person Roles for the specified COU.

        :param cou_id:

        Response Format
            HTTP Status             Response Body                       Description
            200 OK                  CoPersonRole Response               CoPersonRoles returned
            401 Unauthorized                                            Authentication required
            404 COU Unknown                                             id not found
            500 Other Error                                             Unknown error
        """
        return self._get('co_person_roles.json', params={'couid': int(cou_id)})

    def coperson_roles_view_one(self, coperson_role_id: int) -> dict:
        """
        Retrieve an existing CO Person Role.

        :param coperson_role_id:

        Response Format
            HTTP Status                 Response Body                       Description
            200 OK                      CoPersonRole Response               CoPersonRoles returned
            401 Unauthorized                                                Authentication required
            404 CoPersonRole Unknown                                        id not found
            500 Other Error                                                 Unknown error
        """
        return self._get(f'co_person_roles/{coperson_role_id}.json')
