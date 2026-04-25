# Examples

Examples demonstrating basic usage for each wrapped endpoint. Examples dynamically discover valid IDs from the configured CO at runtime, so they work across different registries without modification.

- Example code tested against COmanage v4.0.0
- Examples use the alpha tier configuration from `.env` (registry-test.cilogon.org)
- Run examples from the project root: `uv run python examples/<name>.py`

## Table of Contents

- [Configuration](#config) `__init__.py` used by all examples
- [CoOrgIdentityLink API](#coorgidentitylink) example output
- [CoPerson API](#coperson) example output
- [CoPersonRole API](#copersonrole) example output
- [Cou API](#cou) example output
- [EmailAddress API](#emailaddress) example output
- [Identifier API](#identifier) example output
- [Name API](#name) example output
- [OrgIdentity API](#orgidentity) example output
- [SshKey API](#sshkey) example output

## <a name="config"></a>Configuration

All examples presented herein use the same base configuration as defined by the `examples/__init__.py` file

```python
# examples/__init__.py
# Configuration for example code

import json
import os
import sys

from dotenv import load_dotenv
from requests.exceptions import HTTPError

# Use .env file to set environment variables
load_dotenv()

COMANAGE_API_USER = os.getenv('COMANAGE_API_USER')
COMANAGE_API_PASS = os.getenv('COMANAGE_API_PASS')
COMANAGE_API_CO_NAME = os.getenv('COMANAGE_API_CO_NAME')
COMANAGE_API_CO_ID = int(os.getenv('COMANAGE_API_CO_ID'))
COMANAGE_API_URL = os.getenv('COMANAGE_API_URL')
COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID = int(os.getenv('COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID'))

# DEVELOPMEMNT: account for comanage_api directory being one level up for development purposes
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# import fabric-comanage-api package (uses directory for development purposes)
from comanage_api import ComanageApi

# create a new ComanageApi object and set the connection attributes
api = ComanageApi(
    co_api_url=COMANAGE_API_URL,
    co_api_user=COMANAGE_API_USER,
    co_api_pass=COMANAGE_API_PASS,
    co_api_org_id=COMANAGE_API_CO_ID,
    co_api_org_name=COMANAGE_API_CO_NAME,
    co_ssh_key_authenticator_id=COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID
)
```

## <a name="coorgidentitylink"></a>CoOrgIdentityLink API

Example: `coorg_identity_links_example.py`

```console
$ uv run python examples/coorg_identity_links_example.py
### coorg_identity_links_add
[NOT IMPLEMENTED]  NotImplementedError - coorg_identity_links_add() is not implemented
### coorg_identity_links_delete
[NOT IMPLEMENTED]  NotImplementedError - coorg_identity_links_delete() is not implemented
### coorg_identity_links_edit
[NOT IMPLEMENTED]  NotImplementedError - coorg_identity_links_edit() is not implemented
### discover CO Person ID
Using CO Person ID: <Id>
### coorg_identity_links_view_by_identity
{
    "ResponseType": "CoOrgIdentityLinks",
    "Version": "1.0",
    "CoOrgIdentityLinks": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "CoPersonId": "<CoPersonId>",
            "OrgIdentityId": "<OrgIdentityId>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### coorg_identity_links_view_one
{
    "ResponseType": "CoOrgIdentityLinks",
    "Version": "1.0",
    "CoOrgIdentityLinks": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "CoPersonId": "<CoPersonId>",
            "OrgIdentityId": "<OrgIdentityId>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
```

## <a name="coperson"></a>CoPerson API

Example: `copeople_example.py`

**NOTE**: This example exits early after `email_addresses_view_per_person`. The unimplemented methods (`copeople_add`, `copeople_delete`, `copeople_edit`, `copeople_find`) and remaining view methods are after `exit(0)` and only run if that line is removed.

```console
$ uv run python examples/copeople_example.py
### discover CO Person ID
Using CO Person ID: <Id>
### discover identifier for CO Person
Using identifier: <Identifier>
### copeople_view_per_identifier
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "CoId": "<CoId>",
            "Status": "Active",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### email_addresses_view_per_person
{
    "ResponseType": "EmailAddresses",
    "Version": "1.0",
    "EmailAddresses": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Mail": "<email@example.com>",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
<email@example.com>
```

When run with `exit(0)` removed, the unimplemented methods produce:

```console
### copeople_add
[NOT IMPLEMENTED]  NotImplementedError - copeople_add() is not implemented
### copeople_delete
[NOT IMPLEMENTED]  NotImplementedError - copeople_delete() is not implemented
### copeople_edit
[NOT IMPLEMENTED]  NotImplementedError - copeople_edit() is not implemented
### copeople_find
[NOT IMPLEMENTED]  NotImplementedError - copeople_find() is not implemented
```

## <a name="copersonrole"></a>CoPersonRole API

Example: `coperson_roles_example.py`

This example dynamically discovers a valid CO Person ID and COU ID, then performs a full CRUD cycle: add a role, view it, edit it, list roles, and delete it.

```console
$ uv run python examples/coperson_roles_example.py
### discover CO Person ID and COU ID
Using CO Person ID: <Id>
Using COU ID: <Id>
### coperson_roles_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "CoPersonRole",
    "Id": "<Id>"
}
### coperson_roles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "CouId": "<CouId>",
            "Affiliation": "student",
            "O": "<CO_API_ORG_NAME>",
            "Status": "PendingApproval",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### coperson_roles_edit
True
### coperson_roles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "CouId": "<CouId>",
            "Affiliation": "member",
            "O": "<CO_API_ORG_NAME>",
            "Status": "Active",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### coperson_roles_view_all
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        ...
    ]
}
### coperson_roles_view_per_coperson
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        ...
    ]
}
### coperson_roles_view_per_cou
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        ...
    ]
}
### coperson_roles_delete
True
### coperson_roles_view_one (previously deleted co person role)
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            ...
            "Deleted": true,
            ...
        }
    ]
}
```

## <a name="cou"></a>COU API

Example: `cous_example.py` 

This example performs a full CRUD cycle: add a COU, view all, edit it, view one, delete it, and attempt to view the deleted COU.

```console
$ uv run python examples/cous_example.py
### cous_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "Cou",
    "Id": "<Id>"
}
### cous_view_all
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "CoId": "<CoId>",
            "Name": "<name>",
            "Description": "<description>",
            "Lft": "<Lft>",
            "Rght": "<Rght>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        },
        ...
    ]
}
### cous_view_per_co
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        ...
    ]
}
### cous_edit
True
### cous_view_one
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "CoId": "<CoId>",
            "Name": "cou test - edited",
            "Description": "cou test description - edited",
            "Lft": "<Lft>",
            "Rght": "<Rght>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### cous_delete
True
### cous_view_one (previously deleted cou)
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            ...
            "Deleted": true,
            ...
        }
    ]
}
```

## <a name="emailaddress"></a>EmailAddress API

Example: `email_addresses_example.py`

```console
$ uv run python examples/email_addresses_example.py
### discover CO Person ID
Using CO Person ID: <Id>
### email_addresses_add
[NOT IMPLEMENTED]  NotImplementedError - email_addresses_add() is not implemented
### email_addresses_delete
[NOT IMPLEMENTED]  NotImplementedError - email_addresses_delete() is not implemented
### email_addresses_edit
[NOT IMPLEMENTED]  NotImplementedError - email_addresses_edit() is not implemented
### email_addresses_view_per_person
{
    "ResponseType": "EmailAddresses",
    "Version": "1.0",
    "EmailAddresses": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Mail": "<email@example.com>",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### email_addresses_view_one
{
    "ResponseType": "EmailAddresses",
    "Version": "1.0",
    "EmailAddresses": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Mail": "<email@example.com>",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
```

## <a name="identifier"></a>Identifier API

Example: `identifiers_example.py`

```console
$ uv run python examples/identifiers_example.py
### discover CO Person ID
Using CO Person ID: <Id>
### identifiers_add
[NOT IMPLEMENTED]  NotImplementedError - identifiers_add() is not implemented
### identifiers_assign
[NOT IMPLEMENTED]  NotImplementedError - identifiers_assign() is not implemented
### identifiers_delete
[NOT IMPLEMENTED]  NotImplementedError - identifiers_delete() is not implemented
### identifiers_edit
[NOT IMPLEMENTED]  NotImplementedError - identifiers_edit() is not implemented
### identifiers_view_per_entity
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Identifier": "<Identifier>",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        },
        ...
    ]
}
### identifiers_view_one
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Identifier": "<Identifier>",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
```

## <a name="name"></a>Name API

Example: `names_example.py`

```console
$ uv run python examples/names_example.py
### discover CO Person ID
Using CO Person ID: <Id>
### names_add
[NOT IMPLEMENTED]  NotImplementedError - names_add() is not implemented
### names_delete
[NOT IMPLEMENTED]  NotImplementedError - names_delete() is not implemented
### names_edit
[NOT IMPLEMENTED]  NotImplementedError - names_edit() is not implemented
### names_view_per_person
{
    "ResponseType": "Names",
    "Version": "1.0",
    "Names": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Given": "<Given>",
            "Family": "<Family>",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "PrimaryName": true,
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
### names_view_one
{
    "ResponseType": "Names",
    "Version": "1.0",
    "Names": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Given": "<Given>",
            "Family": "<Family>",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "PrimaryName": true,
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
```

## <a name="orgidentity"></a>OrgIdentity API

Example: `org_identities_example.py`

```console
$ uv run python examples/org_identities_example.py
### org_identities_add
[NOT IMPLEMENTED]  NotImplementedError - org_identities_add() is not implemented
### org_identities_delete
[NOT IMPLEMENTED]  NotImplementedError - org_identities_delete() is not implemented
### org_identities_edit
[NOT IMPLEMENTED]  NotImplementedError - org_identities_edit() is not implemented
### org_identities_view_per_co
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Status": "SY",
            "Affiliation": "member",
            "O": "<Organization>",
            "CoId": "<CoId>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        },
        ...
    ]
}
### org_identities_view_per_identifier
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": [
        ...
    ]
}
### org_identities_view_one
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Status": "SY",
            "Affiliation": "member",
            "O": "<Organization>",
            "CoId": "<CoId>",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>"
        }
    ]
}
```

## <a name="sshkey"></a>SshKey API

Example: `ssh_keys_example.py`

This example dynamically discovers a CO Person ID, then performs a full CRUD cycle: add an SSH key, view all, view per person, view one, edit it, and delete it.

```console
$ uv run python examples/ssh_keys_example.py
### discover CO Person ID
Using CO Person ID: <Id>
### ssh_keys_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "SshKey",
    "Id": "<Id>"
}
### ssh_keys_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry-test.cilogon.org/registry/ssh_key_authenticator/ssh_keys.json
### ssh_keys_view_per_coperson
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "<Id>",
            "Person": {
                "Type": "CO",
                "Id": "<Id>"
            },
            "Comment": "SshKey API test",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC...",
            "Created": "<CreateTime>",
            "Modified": "<ModTime>",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "<ActorIdentifier>",
            "SshKeyAuthenticatorId": "<SshKeyAuthenticatorId>"
        }
    ]
}
### ssh_keys_view_one
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            ...
            "Comment": "SshKey API test",
            ...
        }
    ]
}
### ssh_keys_edit
True
### ssh_keys_view_one
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            ...
            "Comment": "NEW COMMENT",
            "Revision": "1",
            ...
        }
    ]
}
### ssh_keys_delete
True
### ssh_keys_view_one (previously deleted ssh key)
[ERROR] Exception caught
-->  HTTPError - 404 Client Error: Not Found for url: ...
```

**NOTE**: `ssh_keys_view_all` returns 401 because the endpoint requires specific authorization beyond the API user credentials. Use `ssh_keys_view_per_coperson` to retrieve keys for a specific person.
