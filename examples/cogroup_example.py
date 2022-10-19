# examples/cogroup_example.py
# CoGroup API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# cogroup_add, cogroup_delete, cogroup_edit, cogroup_reconcile_all, cogroup_reconcile_one, cogroup_view_all, \
#   cogroup_view_per_co, cogroup_view_per_coperson, cogroup_view_per_identifier, cogroup_view_one

# cogroup_add() -> dict
print('### cogroup_add')
try:
    new_cogroup = api.cogroup_add()
    print(json.dumps(new_cogroup, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_delete() -> bool
print('### cogroup_delete')
try:
    delete_cogroup = api.cogroup_delete()
    print(json.dumps(delete_cogroup, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_edit() -> bool
print('### cogroup_edit')
try:
    edit_cogroup = api.cogroup_edit()
    print(json.dumps(edit_cogroup, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_reconcile_all() -> bool
print('### cogroup_reconcile_all')
try:
    reconcile_all_cogroup = api.cogroup_reconcile_all()
    print(json.dumps(reconcile_all_cogroup, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_reconcile_one() -> bool
print('### cogroup_reconcile_one')
try:
    reconcile_one_cogroup = api.cogroup_reconcile_one()
    print(json.dumps(reconcile_one_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_view_all() -> dict
print('### cogroup_view_all')
try:
    all_cogroup = api.cogroup_view_all()
    print(json.dumps(all_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_view_per_co() -> dict
print('### cogroup_view_per_co')
try:
    per_co_cogroup = api.cogroup_view_per_co()
    print(json.dumps(per_co_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_view_per_coperson() -> dict
print('### cogroup_view_per_coperson')
try:
    per_coperson_cogroup = api.cogroup_view_per_coperson()
    print(json.dumps(per_coperson_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_view_per_identifier() -> dict
print('### cogroup_view_per_identifier')
try:
    per_identfier_cogroup = api.cogroup_view_per_identifier()
    print(json.dumps(per_identfier_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# cogroup_view_one() -> dict
print('### cogroup_view_one')
try:
    one_cogroup = api.cogroup_view_one()
    print(json.dumps(one_cogroup, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
