# comanage_api/_orgidentities.py

"""
OrgIdentity API - https://spaces.at.internet2.edu/display/COmanage/OrgIdentity+API
"""


class OrgIdentitiesMixin:
    """Mixin providing OrgIdentity API methods."""

    def org_identities_add(self) -> dict:
        """### NOT IMPLEMENTED ### Add a new Organizational Identity."""
        raise NotImplementedError("org_identities_add() is not implemented")

    def org_identities_delete(self) -> bool:
        """### NOT IMPLEMENTED ### Remove an Organizational Identity."""
        raise NotImplementedError("org_identities_delete() is not implemented")

    def org_identities_edit(self) -> bool:
        """### NOT IMPLEMENTED ### Edit an existing Organizational Identity."""
        raise NotImplementedError("org_identities_edit() is not implemented")

    def org_identities_view_all(self) -> dict:
        """
        Retrieve all existing Organizational Identities.

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

        :param identifier_id:

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

        :param org_identity_id:

        Response Format
            HTTP Status                 Response Body               Description
            200 OK                      OrgIdentity Response        OrgIdentity returned
            401 Unauthorized                                        Authentication required
            404 OrgIdentity Unknown                                 id not found
            500 Other Error                                         Unknown error
        """
        return self._get(f'org_identities/{org_identity_id}.json', params={'coid': self._CO_API_ORG_ID})
