# examples/copeople_example.py
# CoPerson API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# dynamically discover a valid CO Person ID and identifier from the CO
print('### discover CO Person ID')
try:
    per_co_copeople = api.copeople_view_per_co()
    co_person_id = int(per_co_copeople['CoPeople'][0]['Id'])
    print('Using CO Person ID: ' + str(co_person_id))
except (KeyError, IndexError, HTTPError) as err:
    print('[ERROR] Could not discover a CO Person ID')
    print('--> ', type(err).__name__, '-', err)
    co_person_id = None

# get identifier for the discovered CO Person
print('### discover identifier for CO Person')
try:
    person_identifiers = api.identifiers_view_per_entity(
        entity_type='copersonid',
        entity_id=co_person_id
    )
    identifier = person_identifiers['Identifiers'][0]['Identifier']
    print('Using identifier: ' + str(identifier))
except (NameError, KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Could not discover an identifier')
    print('--> ', type(err).__name__, '-', err)
    identifier = None

# copeople_view_per_identifier(identifier: str, distinct_by_id: bool = True) -> dict
print('### copeople_view_per_identifier')
try:
    identifier_copeople = api.copeople_view_per_identifier(
        identifier=identifier,
        distinct_by_id=True
    )
    print(json.dumps(identifier_copeople, indent=4))
except (HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_per_person(person_type: str, person_id: int) -> dict:
print('### email_addresses_view_per_person')
try:
    per_person_email_addresses = api.email_addresses_view_per_person(
        person_type='copersonid',
        person_id=co_person_id
    )
    print(json.dumps(per_person_email_addresses, indent=4))
    email_address = per_person_email_addresses.get('EmailAddresses')[0].get('Mail')
    print(email_address)
except (KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
    email_address = None

# -----

exit(0)

# copeople_add() -> dict
print('### copeople_add')
try:
    new_copeople = api.copeople_add()
    print(json.dumps(new_copeople, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# copeople_delete() -> bool
print('### copeople_delete')
try:
    delete_copeople = api.copeople_delete()
    print(json.dumps(delete_copeople, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# copeople_edit() -> bool
print('### copeople_edit')
try:
    edit_copeople = api.copeople_edit()
    print(json.dumps(edit_copeople, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# copeople_find() -> dict
print('### copeople_find')
try:
    find_copeople = api.copeople_find()
    print(json.dumps(find_copeople, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# copeople_match(given: str = None, family: str = None, mail: str = None, distinct_by_id: bool = True) -> dict
print('### copeople_match')
try:
    given = 'michael'
    family = None
    mail = None
    distinct_by_id = True
    match_copeople = api.copeople_match(
        given=given,
        family=family,
        mail=mail,
        distinct_by_id=distinct_by_id
    )
    print(json.dumps(match_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_all() -> dict
print('### copeople_view_all')
try:
    all_copeople = api.copeople_view_all()
    print(json.dumps(all_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_per_co() -> dict
print('### copeople_view_per_co')
try:
    per_co_copeople = api.copeople_view_per_co()
    print(json.dumps(per_co_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_per_identifier(identifier: str, distinct_by_id: bool = True) -> dict
print('### copeople_view_per_identifier')
try:
    identifier = 'http://cilogon.org/serverA/users/242181'
    distinct_by_id = True
    identifier_copeople = api.copeople_view_per_identifier(
        identifier=identifier,
        distinct_by_id=True
    )
    print(json.dumps(identifier_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_view_one(coperson_id: int) -> dict
print('### copeople_view_one')
try:
    # get first CoPeople['Id'] from all_copeople response
    if per_co_copeople['CoPeople']:
        coperson_id = int(per_co_copeople['CoPeople'][0]['Id'])
        one_copeople = api.copeople_view_one(coperson_id=coperson_id)
        print(json.dumps(one_copeople, indent=4))
    else:
        print('No CoPeople Found...')
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
