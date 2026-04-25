# comanage_api/_emailaddresses.py

"""
EmailAddress API - https://spaces.at.internet2.edu/display/COmanage/EmailAddress+API
"""


class EmailAddressesMixin:
    """Mixin providing EmailAddress API methods."""

    def email_addresses_add(self) -> dict:
        """### NOT IMPLEMENTED ### Add a new EmailAddress."""
        raise NotImplementedError("email_addresses_add() is not implemented")

    def email_addresses_delete(self) -> bool:
        """### NOT IMPLEMENTED ### Remove an EmailAddress."""
        raise NotImplementedError("email_addresses_delete() is not implemented")

    def email_addresses_edit(self) -> bool:
        """### NOT IMPLEMENTED ### Edit an existing EmailAddress."""
        raise NotImplementedError("email_addresses_edit() is not implemented")

    def email_addresses_view_all(self) -> dict:
        """
        Retrieve all existing EmailAddresses.

        Response Format
            HTTP Status         Response Body           Description
            200 OK              EmailAddress Response   EmailAddresses returned
            401 Unauthorized                            Authentication required
            500 Other Error                             Unknown error
        """
        return self._get('email_addresses.json')

    def email_addresses_view_per_person(self, person_type: str, person_id: int) -> dict:
        """
        Retrieve EmailAddresses attached to a CO Department, CO Person, or Org Identity.

        :param person_type:
        :param person_id:

        Response Format
            HTTP Status                 Response Body           Description
            200 OK                      EmailAddress Response   EmailAddress returned
            401 Unauthorized                                    Authentication required
            500 Other Error                                     Unknown error
        """
        return self._get_by_entity('email_addresses.json', person_type, person_id,
                                   self.EMAILADDRESS_OPTIONS, 'person_type')

    def email_addresses_view_one(self, email_address_id: int) -> dict:
        """
        Retrieve an existing EmailAddress.

        :param email_address_id:

        Response Format
            HTTP Status                 Response Body               Description
            200 OK                      EmailAddress Response       EmailAddress returned
            401 Unauthorized                                        Authentication required
            404 EmailAddress Unknown                                id not found
            500 Other Error                                         Unknown error
        """
        return self._get(f'email_addresses/{email_address_id}.json')
