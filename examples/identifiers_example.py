# examples/identifiers_example.py
# Identifier API examples

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

# identifiers_add() -> dict
print('### identifiers_add')
try:
    new_identifier = api.identifiers_add()
    print(json.dumps(new_identifier, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# identifiers_assign() -> bool
print('### identifiers_assign')
try:
    assign_identifier = api.identifiers_assign()
    print(json.dumps(assign_identifier, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# identifiers_delete() -> bool
print('### identifiers_delete')
try:
    delete_identifier = api.identifiers_delete()
    print(json.dumps(delete_identifier, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# identifiers_edit() -> bool
print('### identifiers_edit')
try:
    edit_identifier = api.identifiers_edit()
    print(json.dumps(edit_identifier, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# identifiers_view_per_entity(entity_type: str, entity_id: int) -> dict:
print('### identifiers_view_per_entity')
try:
    entity_identifiers = api.identifiers_view_per_entity(
        entity_type='copersonid',
        entity_id=CO_PERSON_ID
    )
    print(json.dumps(entity_identifiers, indent=4))
except (ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# identifiers_view_one(identifier_id: int) -> dict
print('### identifiers_view_one')
try:
    # get first Identifiers['Id'] from entity_identifiers response
    identifier_id = int(entity_identifiers['Identifiers'][0]['Id'])
    one_identifier = api.identifiers_view_one(identifier_id=identifier_id)
    print(json.dumps(one_identifier, indent=4))
except (NameError, KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
