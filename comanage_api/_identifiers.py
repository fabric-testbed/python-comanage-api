# comanage_api/_identifiers.py

"""
Identifier API - https://spaces.at.internet2.edu/display/COmanage/Identifier+API
"""


class IdentifiersMixin:
    """Mixin providing Identifier API methods."""

    def identifiers_add(self) -> dict:
        """### NOT IMPLEMENTED ### Add a new Identifier."""
        raise NotImplementedError("identifiers_add() is not implemented")

    def identifiers_assign(self) -> bool:
        """### NOT IMPLEMENTED ### Assign Identifiers for a CO Person."""
        raise NotImplementedError("identifiers_assign() is not implemented")

    def identifiers_delete(self) -> bool:
        """### NOT IMPLEMENTED ### Remove an Identifier."""
        raise NotImplementedError("identifiers_delete() is not implemented")

    def identifiers_edit(self) -> bool:
        """### NOT IMPLEMENTED ### Edit an existing Identifier."""
        raise NotImplementedError("identifiers_edit() is not implemented")

    def identifiers_view_all(self) -> dict:
        """
        Retrieve all existing Identifiers.

        Response Format
            HTTP Status         Response Body           Description
            200 OK              Identifier Response     Identifiers returned
            401 Unauthorized                            Authentication required
            500 Other Error                             Unknown error
        """
        return self._get('identifiers.json')

    def identifiers_view_per_entity(self, entity_type: str, entity_id: int) -> dict:
        """
        Retrieve Identifiers attached to a CO Department, Co Group, CO Person, or Org Identity.

        :param entity_type:
        :param entity_id:

        Response Format
            HTTP Status                 Response Body           Description
            200 OK                      Identifier Response     Identifier returned
            401 Unauthorized                                    Authentication required
            500 Other Error                                     Unknown error
        """
        return self._get_by_entity('identifiers.json', entity_type, entity_id,
                                   self.ENTITY_OPTIONS, 'entity_type')

    def identifiers_view_one(self, identifier_id: int) -> dict:
        """
        Retrieve an existing Identifier.

        :param identifier_id:

        Response Format
            HTTP Status                 Response Body           Description
            200 OK                      Identifier Response     Identifiers returned
            401 Unauthorized                                    Authentication required
            404 Identifier Unknown                              id not found
            500 Other Error                                     Unknown error
        """
        return self._get(f'identifiers/{identifier_id}.json')
