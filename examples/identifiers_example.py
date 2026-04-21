# examples/identifiers_example.py
# Identifier API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 163

# identifiers_add() -> dict
print('### identifiers_add')
try:
    new_identifier = api.identifiers_add(
        identity_type='eppn',
        identifier='test@domain.com',
        login_flag=False,
        person_type='CO',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(new_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_assign() -> bool
print('### identifiers_assign')
try:
    assign_identifier = api.identifiers_assign()
    print(json.dumps(assign_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_delete() -> bool
print('### identifiers_delete')
try:
    delete_identifier = api.identifiers_delete()
    print(json.dumps(delete_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_edit() -> bool
print('### identifiers_edit')
try:
    edit_identifier = api.identifiers_edit()
    print(json.dumps(edit_identifier, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_all() -> dict
print('### identifiers_view_all')
try:
    all_identifiers = api.identifiers_view_all()
    print(json.dumps(all_identifiers, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_per_entity(entity_type: str, entity_id: int) -> dict:
print('### identifiers_view_per_entity')
try:
    entity_identifiers = api.identifiers_view_per_entity(
        entity_type='copersonid',
        entity_id=CO_PERSON_ID
    )
    print(json.dumps(entity_identifiers, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_one(identifier_id: int) -> dict
print('### identifiers_view_one')
try:
    # get first Identifiers['Id'] from entity_identifiers response
    identifier_id = int(entity_identifiers['Identifiers'][0]['Id'])
    one_identifier = api.identifiers_view_one(identifier_id=identifier_id)
    print(json.dumps(one_identifier, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
