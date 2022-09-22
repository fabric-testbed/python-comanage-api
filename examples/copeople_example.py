# examples/copeople_example.py
# CoPerson API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# copeople_add() -> dict
print('### copeople_add')
try:
    new_copeople = api.copeople_add()
    print(json.dumps(new_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_delete() -> bool
print('### copeople_delete')
try:
    per_co_copeople = api.copeople_view_per_co()
    if per_co_copeople['CoPeople']:
        coperson_id = int(per_co_copeople['CoPeople'][0]['Id'])
        delete_copeople = api.copeople_delete(coperson_id=coperson_id)
    print(delete_copeople)
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_edit() -> bool
print('### copeople_edit')
try:
    edit_copeople = api.copeople_edit()
    print(json.dumps(edit_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# copeople_find() -> dict
print('### copeople_find')
try:
    find_copeople = api.copeople_find()
    print(json.dumps(find_copeople, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

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
    identifier = 'ImPACT1000002'
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
