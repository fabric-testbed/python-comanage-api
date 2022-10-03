# examples/cogroupmember_example.py
# CoGroupMember API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# cogroupmember_add, cogroupmember_delete, cogroupmember_edit, cogroupmember_view_all, cogroupmember_view_per_group, cogroupmember_view_one

# must be set ahead of time and be valid within the CO
CO_PERSON_ID = 163
CO_GROUP_ID = 2

# cogroupmember_add(group_id: int, person_id: int) -> dict
print('### cogroupmember_add')
try:
    new_cogroupmember = api.cogroupmember_add(
        group_id=CO_GROUP_ID,
        person_id=CO_PERSON_ID
    )
    print(json.dumps(new_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroupmember_delete() -> bool
print('### cogroupmember_delete')
try:
    delete_cogroupmember = api.cogroupmember_delete()
    print(json.dumps(delete_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroupmember_edit() -> bool
print('### cogroupmember_edit')
try:
    edit_cogroupmember = api.cogroupmember_edit()
    print(json.dumps(edit_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroupmember_view_all() -> dict
print('### cogroupmember_view_all')
try:
    view_all_cogroupmember = api.cogroupmember_view_all()
    print(json.dumps(view_all_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroupmember_view_per_group(group_id: int) -> dict
print('### cogroupmember_view_per_group')
try:
    view_per_group_cogroupmember = api.cogroupmember_view_per_group(
        group_id=CO_GROUP_ID
    )
    print(json.dumps(view_per_group_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroupmember_view_one() -> dict
print('### cogroupmember_view_one')
try:
    view_one_cogroupmember = api.cogroupmember_view_one()
    print(json.dumps(view_one_cogroupmember, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
