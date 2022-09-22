# examples/names_example.py
# Name API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 163

# names_add(person_type: str, person_id: int, given: str, family: str) -> dict
print('### names_add')
try:
    new_name = api.names_add(
        person_type='copersonid',
        person_id=CO_PERSON_ID,
        given="TestGiven",
        family="TestFamily"
    ))
    print(json.dumps(new_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_delete() -> bool
print('### names_delete')
try:
    delete_name = api.names_delete()
    print(json.dumps(delete_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_edit() -> bool
print('### names_edit')
try:
    edit_name = api.names_edit()
    print(json.dumps(edit_name, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_all() -> dict
print('### names_view_all')
try:
    all_names = api.names_view_all()
    print(json.dumps(all_names, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_per_person(person_type: str, person_id: int) -> dict
print('### names_view_per_person')
try:
    person_names = api.names_view_per_person(
        person_type='copersonid',
        person_id=CO_PERSON_ID
    )
    print(json.dumps(person_names, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# names_view_one(name_id: int) -> dict
print('### names_view_one')
try:
    name_id = int(person_names['Names'][0]['Id'])
    one_name = api.names_view_one(name_id=name_id)
    print(json.dumps(one_name, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
