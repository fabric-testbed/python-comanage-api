# comanage_api/_names.py

"""
Name API - https://spaces.at.internet2.edu/display/COmanage/Name+API

Methods
-------
names_add() -> dict
    ### NOT IMPLEMENTED ###
    Add a new Name.
names_delete() -> bool
    ### NOT IMPLEMENTED ###
    Remove a Name.
names_edit() -> bool
    ### NOT IMPLEMENTED ###
    Edit an existing Name.
names_view_all() -> dict
    Retrieve all existing Names.
names_view_per_person(person_type: str, person_id: int) -> dict
    Retrieve Names attached to a CO Person or Org Identity.
names_view_one(name_id: int) -> dict
    Retrieve Names attached to a CO Person or Org Identity.
"""


def names_add(self) -> dict:
    """
    ### NOT IMPLEMENTED ###
    Add a new Name.

    :param self:
    """
    raise NotImplementedError("names_add() is not implemented")


def names_delete(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Remove a Name.

    :param self:
    """
    raise NotImplementedError("names_delete() is not implemented")


def names_edit(self) -> bool:
    """
    ### NOT IMPLEMENTED ###
    Edit an existing Name.

    :param self:
    """
    raise NotImplementedError("names_edit() is not implemented")


def names_view_all(self) -> dict:
    """
    Retrieve all existing Names.

    :param self:
    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
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
        200 OK              Name Response           Name returned
        401 Unauthorized                            Authentication required
        500 Other Error                             Unknown error
    """
    return self._get('names.json')


def names_view_per_person(self, person_type: str, person_id: int) -> dict:
    """
    Retrieve Names attached to a CO Person or Org Identity.

    :param self:
    :param person_type:
    :param person_id:
    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
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
        200 OK                      Name Response           Name returned
        401 Unauthorized                                    Authentication required
        404 CO Person Unknown                               id not found for CO Person
        404 Org Identity Unknown                            id not found for Org Identity
        500 Other Error                                     Unknown error
    """
    return self._get_by_entity('names.json', person_type, person_id,
                               self.PERSON_OPTIONS, 'person_type')


def names_view_one(self, name_id: int) -> dict:
    """
    Retrieve Names attached to a CO Person or Org Identity.

    :param self:
    :param name_id:
    :return
        {
            "ResponseType":"Names",
            "Version":"1.0",
            "Names":
            [
                {
                    "Version":"1.0",
                    "Id":"<ID>",
                    "Honorific":"<Honorific>",
                    "Given":"<Given>",
                    "Middle":"<Middle>",
                    "Family":"<Family>",
                    "Suffix":"<Suffix>",
                    "Type":"<Type>",
                    "Language":"<Language>",
                    "PrimaryName":true|false,
                    "Person":
                    {
                        "Type":("CO"|"Org"),
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
        200 OK                      Name Response           Name returned
        401 Unauthorized                                    Authentication required
        404 Name Unknown                                    id not found
        500 Other Error                                     Unknown error
    """
    return self._get(f'names/{name_id}.json')
