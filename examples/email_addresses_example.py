# examples/email_addresses_example.py
# EmailAddress API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# dynamically discover a valid CO Person ID from the CO
print('### discover CO Person ID')
try:
    per_co_copeople = api.copeople_view_per_co()
    CO_PERSON_ID = int(per_co_copeople['CoPeople'][0]['Id'])
    print('Using CO Person ID: ' + str(CO_PERSON_ID))
except (KeyError, IndexError, HTTPError) as err:
    print('[ERROR] Could not discover a CO Person ID')
    print('--> ', type(err).__name__, '-', err)
    CO_PERSON_ID = None

# email_addresses_add() -> dict
print('### email_addresses_add')
try:
    new_email_address = api.email_addresses_add()
    print(json.dumps(new_email_address, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# email_addresses_delete() -> bool
print('### email_addresses_delete')
try:
    delete_email_address = api.email_addresses_delete()
    print(json.dumps(delete_email_address, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# email_addresses_edit() -> bool
print('### email_addresses_edit')
try:
    edit_email_address = api.email_addresses_edit()
    print(json.dumps(edit_email_address, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# email_addresses_view_per_person(person_type: str, person_id: int) -> dict:
print('### email_addresses_view_per_person')
try:
    per_person_email_addresses = api.email_addresses_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(per_person_email_addresses, indent=4))
except (ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_one(email_address_id: int) -> dict
print('### email_addresses_view_one')
try:
    # get first EmailAddresses['Id'] from per_person_email_addresses response
    email_address_id = int(per_person_email_addresses['EmailAddresses'][0]['Id'])
    one_email_address = api.email_addresses_view_one(email_address_id=email_address_id)
    print(json.dumps(one_email_address, indent=4))
except (NameError, KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
