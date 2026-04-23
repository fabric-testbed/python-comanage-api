# examples/coorg_identity_links_example.py
# CoOrgIdentityLinks API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# must be set ahead of time and be valid within the CO
IDENTITY_TYPE = 'orgidentityid'
IDENTITY_ID = 190
CO_PERSON_ID = 163

# coorg_identity_links_add, coorg_identity_links_delete, coorg_identity_links_edit, \
#     coorg_identity_links_view_all, coorg_identity_links_view_by_identity, coorg_identity_links_view_one

# coorg_identity_links_add(coperson_id: int, org_identity_id: int) -> dict
print('### coorg_identity_links_add')
try:
    new_coorg_identity_link = api.coorg_identity_links_add(
        coperson_id=CO_PERSON_ID,
        org_identity_id=IDENTITY_ID
    )
    print(json.dumps(new_coorg_identity_link, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_delete() -> bool
print('### coorg_identity_links_delete')
try:
    delete_coorg_identity_link = api.coorg_identity_links_delete()
    print(json.dumps(delete_coorg_identity_link, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_edit() -> bool
print('### coorg_identity_links_edit')
try:
    edit_coorg_identity_link = api.coorg_identity_links_edit()
    print(json.dumps(edit_coorg_identity_link, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_view_all() -> dict
print('### coorg_identity_links_view_all')
try:
    all_coorg_identity_links = api.coorg_identity_links_view_all()
    print(json.dumps(all_coorg_identity_links, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_view_by_identity(self, identity_type: str, identity_id: int) -> dict
print('### coorg_identity_links_view_by_identity')
try:
    per_identity_coorg_identity_links = api.coorg_identity_links_view_by_identity(
        identity_type=IDENTITY_TYPE,
        identity_id=IDENTITY_ID
    )
    print(json.dumps(per_identity_coorg_identity_links, indent=4))
except (TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_view_one(self, coorg_identity_link_id: int) -> dict
print('### coorg_identity_links_view_one')
try:
    # get first CoOrgIdentityLinks['Id'] from per_identity_coorg_identity_links response
    coorg_identity_link_id = int(per_identity_coorg_identity_links['CoOrgIdentityLinks'][0]['Id'])
    one_email_address = api.coorg_identity_links_view_one(coorg_identity_link_id=coorg_identity_link_id)
    print(json.dumps(one_email_address, indent=4))
except (NameError, KeyError, IndexError, TypeError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
