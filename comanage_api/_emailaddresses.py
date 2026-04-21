# comanage_api/_emailaddresses.py

"""
EmailAddress API - https://spaces.at.internet2.edu/display/COmanage/EmailAddress+API

Methods
-------
email_addresses_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new EmailAddress.
email_addresses_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove an EmailAddress.
email_addresses_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing EmailAddress.
email_addresses_view_all() -> dict
    Retrieve all existing EmailAddresses.
email_addresses_view_per_person(person_type: str, person_id: int) -> dict
    Retrieve EmailAddresses attached to a CO Department, CO Person, or Org Identity.
email_addresses_view_one(email_address_id: int) -> dict
    Retrieve an existing EmailAddress.
"""


def email_addresses_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new EmailAddress.

    :param self:
    """
    raise NotImplementedError("email_addresses_add() is not implemented")


def email_addresses_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove an EmailAddress.

    :param self:
    """
    raise NotImplementedError("email_addresses_delete() is not implemented")


def email_addresses_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing EmailAddress.

    :param self:
    """
    raise NotImplementedError("email_addresses_edit() is not implemented")


def email_addresses_view_all(self) -> dict:
    """
    Retrieve all existing EmailAddresses.

    :param self:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

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

    :param self:
    :param person_type:
    :param person_id:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                },
                {...}
            ]
        }:

    Response Format
        HTTP Status                 Response Body           Description
        200 OK                      EmailAddress Response     EmailAddress returned
        204 CO Department                                   The requested CO Department was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 CO Person                                       The requested CO Person was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 Organization                                    The requested Organization was found,
            Has No EmailAddress                                   but has no email addresses attached
        204 Org Identity                                    The requested Org Identity was found,
            Has No EmailAddress                                   but has no email addresses attached
        401 Unauthorized                                    Authentication required
        404 CO Department Unknown                           id not found for CO Department
        404 CO Person Unknown                               id not found for CO Person
        404 Organization Unknown                            id not found for Organization
        404 Org Identity Unknown                            id not found for Org Identity
        500 Other Error                                     Unknown error
    """
    return self._get_by_entity('email_addresses.json', person_type, person_id,
                               self.EMAILADDRESS_OPTIONS, 'person_type')


def email_addresses_view_one(self, email_address_id: int) -> dict:
    """
    Retrieve an existing EmailAddress.

    :param self:
    :param emailaddress_id:
    :return
        {
            "ResponseType":"EmailAddresses",
            "Version":"1.0",
            "EmailAddresses":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Mail":"<Mail>",
                    "Type":<"Type">,
                    "Description":"<Description>",
                    "Verified":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Dept"|"Org"|"Organization"),
                        "Id":"<ID>"
                    }
                    "Created":"<CreateTime>",
                    "Modified":"<ModTime>"
                }
            ]
        }:

    Response Format
        HTTP Status                 Response Body               Description
        200 OK                      EmailAddress Response       EmailAddress returned
        401 Unauthorized                                        Authentication required
        404 EmailAddress Unknown                                id not found
        500 Other Error                                         Unknown error
    """
    return self._get(f'email_addresses/{email_address_id}.json')
