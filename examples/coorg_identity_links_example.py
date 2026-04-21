# examples/coorg_identity_links_example.py
# CoOrgIdentityLinks API examples

import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from examples import *

# coorg_identity_links_add() -> dict
print('### coorg_identity_links_add')
try:
    new_coorg_identity_link = api.coorg_identity_links_add()
    print(json.dumps(new_coorg_identity_link, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# coorg_identity_links_delete() -> bool
print('### coorg_identity_links_delete')
try:
    delete_coorg_identity_link = api.coorg_identity_links_delete()
    print(json.dumps(delete_coorg_identity_link, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# coorg_identity_links_edit() -> bool
print('### coorg_identity_links_edit')
try:
    edit_coorg_identity_link = api.coorg_identity_links_edit()
    print(json.dumps(edit_coorg_identity_link, indent=4))
except NotImplementedError as err:
    print('[NOT IMPLEMENTED] ', type(err).__name__, '-', err)

# dynamically discover a valid CO Person ID for view_by_identity
print('### discover CO Person ID')
try:
    per_co_copeople = api.copeople_view_per_co()
    CO_PERSON_ID = int(per_co_copeople['CoPeople'][0]['Id'])
    print('Using CO Person ID: ' + str(CO_PERSON_ID))
except (KeyError, IndexError, HTTPError) as err:
    print('[ERROR] Could not discover a CO Person ID')
    print('--> ', type(err).__name__, '-', err)
    CO_PERSON_ID = None

# coorg_identity_links_view_by_identity(self, identity_type: str, identity_id: int) -> dict
print('### coorg_identity_links_view_by_identity')
try:
    IDENTITY_ID = CO_PERSON_ID
    IDENTITY_TYPE = 'copersonid'
    per_identity_coorg_identity_links = api.coorg_identity_links_view_by_identity(
        identity_type=IDENTITY_TYPE,
        identity_id=IDENTITY_ID
    )
    print(json.dumps(per_identity_coorg_identity_links, indent=4))
except (NameError, KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# coorg_identity_links_view_one(self, coorg_identity_link_id: int) -> dict
print('### coorg_identity_links_view_one')
try:
    # get first CoOrgIdentityLinks['Id'] from per_identity_coorg_identity_links response
    coorg_identity_link_id = int(per_identity_coorg_identity_links['CoOrgIdentityLinks'][0]['Id'])
    one_coorg_identity_link = api.coorg_identity_links_view_one(coorg_identity_link_id=coorg_identity_link_id)
    print(json.dumps(one_coorg_identity_link, indent=4))
except (NameError, KeyError, IndexError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
