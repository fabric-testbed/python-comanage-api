# examples/coperson_roles_example.py
# CoPersonRoles API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# dynamically discover a valid CO Person ID and COU ID from the CO
print('### discover CO Person ID and COU ID')
try:
    per_co_copeople = api.copeople_view_per_co()
    CO_PERSON_ID = int(per_co_copeople['CoPeople'][0]['Id'])
    print('Using CO Person ID: ' + str(CO_PERSON_ID))
except (KeyError, IndexError, HTTPError) as err:
    print('[ERROR] Could not discover a CO Person ID')
    print('--> ', type(err).__name__, '-', err)
    CO_PERSON_ID = None

try:
    cous_per_co = api.cous_view_per_co()
    COU_ID = int(cous_per_co['Cous'][0]['Id'])
    print('Using COU ID: ' + str(COU_ID))
except (KeyError, IndexError, HTTPError) as err:
    print('[ERROR] Could not discover a COU ID')
    print('--> ', type(err).__name__, '-', err)
    COU_ID = None

# # coperson_roles_add(coperson_id: int, cou_id: int, status: str = None, affiliation: str = None) -> dict
print('### coperson_roles_add')
try:
    coperson_id = CO_PERSON_ID
    cou_id = COU_ID
    status = 'PendingApproval'
    affiliation = 'student'
    roles_add = api.coperson_roles_add(
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(json.dumps(roles_add, indent=4))
except (ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one')
try:
    coperson_role_id = roles_add.get('Id')
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_edit(coperson_role_id: int, coperson_id: int = None, cou_id: int = None, status: str = None,
#                    affiliation: str = None) -> bool
print('### coperson_roles_edit')
try:
    status = 'Active'
    affiliation = 'member'
    roles_edit = api.coperson_roles_edit(
        coperson_role_id=coperson_role_id,
        coperson_id=coperson_id,
        cou_id=cou_id,
        status=status,
        affiliation=affiliation
    )
    print(roles_edit)
except (NameError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one')
try:
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_all() -> dict
print('### coperson_roles_view_all')
try:
    roles_all = api.coperson_roles_view_all()
    print(json.dumps(roles_all, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_per_coperson(coperson_id: int) -> dict
print('### coperson_roles_view_per_coperson')
try:
    roles_view_per_coperson = api.coperson_roles_view_per_coperson(coperson_id=coperson_id)
    print(json.dumps(roles_view_per_coperson, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_per_cou(cou_id: int) -> dict
print('### coperson_roles_view_per_cou')
try:
    roles_view_per_cou = api.coperson_roles_view_per_cou(cou_id=cou_id)
    print(json.dumps(roles_view_per_cou, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_delete(coperson_role_id: int) -> bool
print('### coperson_roles_delete')
try:
    roles_delete = api.coperson_roles_delete(coperson_role_id=coperson_role_id)
    print(roles_delete)
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coperson_roles_view_one(coperson_role_id: int) -> dict
print('### coperson_roles_view_one (previously deleted co person role)')
try:
    roles_view_one = api.coperson_roles_view_one(coperson_role_id=coperson_role_id)
    print(json.dumps(roles_view_one, indent=4))
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
