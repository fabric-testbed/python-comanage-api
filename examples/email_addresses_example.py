# examples/email_addresses_example.py
# EmailAddress API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 163

# email_addresses_add(email_address: str, person_type: str, person_id: int) -> dict
print('### email_addresses_add')
try:
    new_email_address = api.email_addresses_add(
        email_address='test@domain.com',
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(new_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_delete() -> bool
print('### email_addresses_delete')
try:
    delete_email_address = api.email_addresses_delete()
    print(json.dumps(delete_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_edit() -> bool
print('### email_addresses_edit')
try:
    edit_email_address = api.email_addresses_edit()
    print(json.dumps(edit_email_address, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_all() -> dict
print('### email_addresses_view_all')
try:
    all_email_addresses = api.email_addresses_view_all()
    print(json.dumps(all_email_addresses, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_per_person(person_type: str, person_id: int) -> dict:
print('### email_addresses_view_per_person')
try:
    per_person_email_addresses = api.email_addresses_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(per_person_email_addresses, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# email_addresses_view_one(email_address_id: int) -> dict
print('### email_addresses_view_one')
try:
    # get first EmailAddresses['Id'] from per_person_email_addresses response
    email_address_id = int(per_person_email_addresses['EmailAddresses'][0]['Id'])
    one_email_address = api.email_addresses_view_one(email_address_id=email_address_id)
    print(json.dumps(one_email_address, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
