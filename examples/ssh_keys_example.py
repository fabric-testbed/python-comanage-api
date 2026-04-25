# examples/ssh_keys_example.py
# SshKey API examples

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

EX_SSH_KEY = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6' \
             'IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJd' \
             'NUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYo' \
             'LNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4F' \
             'O3M4oqg0G+UgFQccXXi1afkJxu7z'
EX_KEY_TYPE = 'ssh-rsa'
EX_COMMENT = 'SshKey API test'

# ssh_keys_add(coperson_id: int, ssh_key: str, key_type: str, comment: str,
#              ssh_key_authenticator_id: int = None) -> dict
print('### ssh_keys_add')
try:
    coperson_id = CO_PERSON_ID
    ssh_key = EX_SSH_KEY
    key_type = EX_KEY_TYPE
    comment = EX_COMMENT
    new_key = api.ssh_keys_add(
        coperson_id=coperson_id,
        ssh_key=ssh_key,
        key_type=key_type,
        comment=comment
    )
    print(json.dumps(new_key, indent=4))
except (ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_all() -> dict
print('### ssh_keys_view_all')
try:
    all_keys = api.ssh_keys_view_all()
    print(json.dumps(all_keys, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_per_coperson(coperson_id: int) -> dict
print('### ssh_keys_view_per_coperson')
try:
    person_keys = api.ssh_keys_view_per_coperson(
        coperson_id=CO_PERSON_ID
    )
    print(json.dumps(person_keys, indent=4))
except HTTPError as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> dict
print('### ssh_keys_view_one')
try:
    # get first SshKeys['Id'] from person_keys response if it exists
    if person_keys.get('SshKeys'):
        ssh_key_id = int(person_keys.get('SshKeys')[0].get('Id'))
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
        ssh_key_id = -1
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_edit(ssh_key_id: int, coperson_id: int = None, ssh_key: str = None, key_type: str = None,
#               comment: str = None, ssh_key_authenticator_id: int = None) -> bool
print('### ssh_keys_edit')
try:
    if ssh_key_id != -1:
        new_comment = 'NEW COMMENT'
        edit_key = api.ssh_keys_edit(
            ssh_key_id=ssh_key_id,
            coperson_id=CO_PERSON_ID,
            comment=new_comment
        )
        print(edit_key)
    else:
        print('No SSH Keys Found...')
except (NameError, ValueError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> dict
try:
    print('### ssh_keys_view_one')
    if ssh_key_id != -1:
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_delete() -> bool
print('### ssh_keys_delete')
try:
    # prevent key from being deleted at this time (demo purposes only)
    # ssh_key_id = -1
    if ssh_key_id != -1:
        delete_key = api.ssh_keys_delete(
            ssh_key_id=ssh_key_id
        )
        print(delete_key)
    else:
        print('No SSH Keys Found...')
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)

# ssh_keys_view_one(ssh_key_id: int) -> dict
print('### ssh_keys_view_one (previously deleted ssh key)')
try:
    if ssh_key_id != -1:
        one_key = api.ssh_keys_view_one(ssh_key_id=ssh_key_id)
        print(json.dumps(one_key, indent=4))
    else:
        print('No SSH Keys Found...')
except (NameError, HTTPError) as err:
    print('[ERROR] Exception caught')
    print('--> ', type(err).__name__, '-', err)
