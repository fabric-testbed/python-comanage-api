# comanage_api/_names.py

"""
Name API - https://spaces.at.internet2.edu/display/COmanage/Name+API
"""


class NamesMixin:
    """Mixin providing Name API methods."""

    def names_add(self) -> dict:
        """### NOT IMPLEMENTED ### Add a new Name."""
        raise NotImplementedError("names_add() is not implemented")

    def names_delete(self) -> bool:
        """### NOT IMPLEMENTED ### Remove a Name."""
        raise NotImplementedError("names_delete() is not implemented")

    def names_edit(self) -> bool:
        """### NOT IMPLEMENTED ### Edit an existing Name."""
        raise NotImplementedError("names_edit() is not implemented")

    def names_view_all(self) -> dict:
        """
        Retrieve all existing Names.

        Response Format
            HTTP Status         Response Body           Description
            200 OK              Name Response           Name returned
            401 Unauthorized                            Authentication required
            500 Other Error                             Unknown error
        """
        return self._get('names.json')

    def names_view_per_person(self, person_type: str, person_id: int) -> dict:
        """
        Retrieve Names attached to a CO Person or Org Identity.

        :param person_type:
        :param person_id:

        Response Format
            HTTP Status                 Response Body           Description
            200 OK                      Name Response           Name returned
            401 Unauthorized                                    Authentication required
            500 Other Error                                     Unknown error
        """
        return self._get_by_entity('names.json', person_type, person_id,
                                   self.PERSON_OPTIONS, 'person_type')

    def names_view_one(self, name_id: int) -> dict:
        """
        Retrieve an existing Name.

        :param name_id:

        Response Format
            HTTP Status                 Response Body           Description
            200 OK                      Name Response           Name returned
            401 Unauthorized                                    Authentication required
            404 Name Unknown                                    id not found
            500 Other Error                                     Unknown error
        """
        return self._get(f'names/{name_id}.json')
