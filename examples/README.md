# Examples

Examples demonstrating basic usage for each wrapped endpoint. Some of the values used herein are specific to the ImPACT project registry and thus would not work for other registries, but the concept would be the same for any registry.

- Example code tested against COmanage v4.0.0

## Table of Contents

- [Configuration](#config) `__init__.py` used by all examples
- [CoGroupMember API](#cogroupmember) example output
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

All example presented herein use the same base configuration as defined by the `examples/__init__.py` file

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

## <a name="cogroupmember"></a>CoGroupMember API

Example: `cogroupmember_example.py`

```console
$ python examples/cogroupmember_example.py
### cogroupmember_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### cogroupmember_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### cogroupmember_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### cogroupmember_view_all
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### cogroupmember_view_per_group
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### cogroupmember_view_one
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local

```

## <a name="coorgidentitylink"></a>CoOrgIdentityLink API

Example: `co_org_identity_links_example.py`

```console
$ python examples/coorg_identity_links_example.py
### coorg_identity_links_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### coorg_identity_links_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### coorg_identity_links_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### coorg_identity_links_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry-test.cilogon.org/registry/co_org_identity_links.json
### coorg_identity_links_view_by_identity
{
    "ResponseType": "CoOrgIdentityLinks",
    "Version": "1.0",
    "CoOrgIdentityLinks": [
        {
            "Version": "1.0",
            "Id": "44",
            "CoPersonId": "163",
            "OrgIdentityId": "190",
            "Created": "2018-01-24 19:08:47",
            "Modified": "2018-01-24 19:08:47",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
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
            "Id": "44",
            "CoPersonId": "163",
            "OrgIdentityId": "190",
            "Created": "2018-01-24 19:08:47",
            "Modified": "2018-01-24 19:08:47",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
```

## <a name="coperson"></a>CoPerson API

Example: `copeople_example.py`

```console
$ python examples/copeople_example.py
### copeople_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_find
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### copeople_match
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### copeople_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/co_people.json
### copeople_view_per_co
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "29",
            "CoId": "3",
            "Status": "Active",
            "Created": "2018-11-05 20:48:55",
            "Modified": "2018-11-06 03:23:00",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/241998"
        },
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "1558",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-10 18:32:32",
            "Modified": "2021-09-10 18:33:46",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/227641"
        },
        {
            "Version": "1.0",
            "Id": "1573",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-14 11:06:03",
            "Modified": "2021-09-14 11:06:57",
            "Revision": "7",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/2604273"
        },
        {
            "Version": "1.0",
            "Id": "1603",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:36:02",
            "Revision": "7",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
### copeople_view_per_identifier
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "1135",
            "CoId": "3",
            "Status": "Active",
            "Created": "2021-03-17 16:03:02",
            "Modified": "2021-03-17 16:04:23",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### copeople_view_one
{
    "ResponseType": "CoPeople",
    "Version": "1.0",
    "CoPeople": [
        {
            "Version": "1.0",
            "Id": "29",
            "CoId": "3",
            "Status": "Active",
            "Created": "2018-11-05 20:48:55",
            "Modified": "2018-11-06 03:23:00",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/241998"
        }
    ]
}
```

## <a name="copersonrole"></a>CoPersonRole API

Example: `coperson_roles_example.py`

```console
$ python examples/coperson_roles_example.py
### coperson_roles_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "CoPersonRole",
    "Id": "1727"
}
### coperson_roles_view_one
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "student",
            "O": "Impact",
            "Status": "PendingApproval",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:44",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
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
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### coperson_roles_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/co_person_roles.json
### coperson_roles_view_per_coperson
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1648",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:36:02",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
### coperson_roles_view_per_cou
{
    "ResponseType": "CoPersonRoles",
    "Version": "1.0",
    "CoPersonRoles": [
        {
            "Version": "1.0",
            "Id": "1622",
            "Person": {
                "Type": "CO",
                "Id": "1558"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-10 18:32:32",
            "Modified": "2021-09-10 18:33:46",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/227641"
        },
        {
            "Version": "1.0",
            "Id": "1628",
            "Person": {
                "Type": "CO",
                "Id": "1573"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-14 11:06:09",
            "Modified": "2021-09-14 11:06:57",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/2604273"
        },
        {
            "Version": "1.0",
            "Id": "1648",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "Status": "Active",
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:36:02",
            "Revision": "5",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:45",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
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
            "Version": "1.0",
            "Id": "1727",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "CouId": "39",
            "Affiliation": "member",
            "O": "Impact",
            "Status": "Active",
            "Created": "2021-09-30 01:22:44",
            "Modified": "2021-09-30 01:22:46",
            "Revision": "1",
            "Deleted": true,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
```

## <a name="cou"></a>COU API

Example: `cous_example.py` 

```console
$ python examples/cous_example.py
### cous_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "Cou",
    "Id": "105"
}
### cous_view_all
{
    "ResponseType": "Cous",
    "Version": "1.0",
    "Cous": [
        {
            "Version": "1.0",
            "Id": "38",
            "CoId": "3",
            "Name": "enrollment-approval",
            "Description": "Enrollment Approval Personnel - can approve or deny new registry members",
            "Lft": "66",
            "Rght": "67",
            "Created": "2021-09-10 14:33:11",
            "Modified": "2021-09-10 14:33:11",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "39",
            "CoId": "3",
            "Name": "impact-users",
            "Description": "ImPACT Users - Registering with the ImPACT site will add new user's to this group",
            "Lft": "68",
            "Rght": "69",
            "Created": "2021-09-10 14:44:09",
            "Modified": "2021-09-10 14:44:09",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "105",
            "CoId": "3",
            "Name": "cou test",
            "Description": "cou test description",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:33",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
        }
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
            "Id": "105",
            "CoId": "3",
            "Name": "cou test - edited",
            "Description": "cou test description - edited",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:34",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_3.development"
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
            "Version": "1.0",
            "Id": "105",
            "CoId": "3",
            "Name": "cou test - edited",
            "Description": "cou test description - edited",
            "Lft": "96",
            "Rght": "97",
            "Created": "2021-10-01 20:45:33",
            "Modified": "2021-10-01 20:45:34",
            "Revision": "1",
            "Deleted": true,
            "ActorIdentifier": "co_3.development"
        }
    ]
}
```

## <a name="emailaddress"></a>EmailAddress API

Example: `email_addresses_example.py`

```console
$ python examples/email_addresses_example.py
### email_addresses_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### email_addresses_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### email_addresses_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### email_addresses_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/email_addresses.json
### email_addresses_view_per_person
{
    "ResponseType": "EmailAddresses",
    "Version": "1.0",
    "EmailAddresses": [
        {
            "Version": "1.0",
            "Id": "810",
            "Mail": "mjstealey@gmail.com",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceEmailAddressId": "809",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "811",
            "Mail": "mjstealey@gmail.com",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:35:22",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
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
            "Id": "810",
            "Mail": "mjstealey@gmail.com",
            "Type": "official",
            "Verified": true,
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceEmailAddressId": "809",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
```

## <a name="identifier"></a>Identifier API

Example: `identifiers_example.py`

```console
$ python examples/identifiers_example.py
### identifiers_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_assign
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### identifiers_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/identifiers.json
### identifiers_view_per_entity
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "1552",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1550",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1553",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "sorid",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1551",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "1554",
            "Identifier": "ImPACT1000006",
            "Type": "impactid",
            "Login": false,
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "Created": "2021-09-15 12:36:01",
            "Modified": "2021-09-15 12:36:01",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        }
    ]
}
### identifiers_view_one
{
    "ResponseType": "Identifiers",
    "Version": "1.0",
    "Identifiers": [
        {
            "Version": "1.0",
            "Id": "1552",
            "Identifier": "http://cilogon.org/serverA/users/226066",
            "Type": "oidcsub",
            "Status": "Active",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceIdentifierId": "1550",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
```

## <a name="name"></a>Name API

Example: `names_example.py`

```console
$ python examples/names_example.py
### names_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### names_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/names.json
### names_view_per_person
{
    "ResponseType": "Names",
    "Version": "1.0",
    "Names": [
        {
            "Version": "1.0",
            "Id": "923",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": false,
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "924",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "SourceNameId": "922",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        },
        {
            "Version": "1.0",
            "Id": "926",
            "Honorific": "",
            "Given": "mj",
            "Middle": "",
            "Family": "stealey",
            "Suffix": "",
            "Type": "official",
            "Language": "",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": true,
            "Created": "2021-09-15 12:34:47",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
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
            "Id": "923",
            "Given": "mj",
            "Family": "stealey",
            "Type": "official",
            "Person": {
                "Type": "CO",
                "Id": "1603"
            },
            "PrimaryName": false,
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:47",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
```

## <a name="orgidentity"></a>OrgIdentity API

Example: `org_identities_example.py`

```console
$ python examples/org_identities_example.py
### org_identities_add
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### org_identities_delete
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### org_identities_edit
[ERROR] Exception caught
-->  HTTPError - 501 Server Error: Not Implemented for url: mock://not_implemented_501.local
### org_identities_view_all
[ERROR] Exception caught
-->  HTTPError - 401 Client Error: Unauthorized for url: https://registry.cilogon.org/registry/org_identities.json
### org_identities_view_per_co
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": [
        {
            "Version": "1.0",
            "Id": "12",
            "Status": "SY",
            "Affiliation": "member",
            "O": "National Center for Supercomputing Applications",
            "CoId": "3",
            "Created": "2018-11-05 20:40:19",
            "Modified": "2018-11-05 20:40:19",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/37233"
        },
        {
            "Version": "1.0",
            "Id": "13",
            "Status": "SY",
            "Affiliation": "member",
            "O": "University of North Carolina at Chapel Hill",
            "CoId": "3",
            "Created": "2018-11-05 20:48:47",
            "Modified": "2018-11-05 20:48:47",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/241998"
        },
        {
            "Version": "1.0",
            "Id": "321",
            "Status": "SY",
            "Affiliation": "member",
            "O": "University of North Carolina at Chapel Hill",
            "CoId": "3",
            "Created": "2021-03-17 16:02:48",
            "Modified": "2021-03-17 16:02:48",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/242181"
        },
        {
            "Version": "1.0",
            "Id": "418",
            "Status": "SY",
            "Affiliation": "member",
            "O": "University of North Carolina at Chapel Hill",
            "CoId": "3",
            "Created": "2021-09-10 18:32:22",
            "Modified": "2021-09-10 18:32:22",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/227641"
        },
        {
            "Version": "1.0",
            "Id": "430",
            "Status": "SY",
            "Affiliation": "member",
            "O": "University of Wisconsin-Madison",
            "CoId": "3",
            "Created": "2021-09-14 11:06:03",
            "Modified": "2021-09-14 11:06:03",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/2604273"
        },
        {
            "Version": "1.0",
            "Id": "435",
            "Status": "SY",
            "Affiliation": "member",
            "O": "Google",
            "CoId": "3",
            "Created": "2021-09-15 12:34:37",
            "Modified": "2021-09-15 12:34:37",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverA/users/226066"
        }
    ]
}
### org_identities_view_per_identifier
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": []
}
### org_identities_view_one
{
    "ResponseType": "OrgIdentities",
    "Version": "1.0",
    "OrgIdentities": [
        {
            "Version": "1.0",
            "Id": "12",
            "Status": "SY",
            "Affiliation": "member",
            "O": "National Center for Supercomputing Applications",
            "CoId": "3",
            "Created": "2018-11-05 20:40:19",
            "Modified": "2018-11-05 20:40:19",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "http://cilogon.org/serverT/users/37233"
        }
    ]
}
```

## <a name="sshkey"></a>SshKey API


Example: `ssh_keys_example.py `

```console
$ python examples/ssh_keys_example.py
### ssh_keys_add
{
    "ResponseType": "NewObject",
    "Version": "1.0",
    "ObjectType": "SshKey",
    "Id": "38"
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
            "Id": "36",
            "Person": {
                "Type": "CO",
                "Id": "163"
            },
            "Comment": "SshKey API test",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-10-18 15:04:22",
            "Modified": "2021-10-18 15:04:22",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_6.impact-development",
            "SshKeyAuthenticatorId": "7"
        },
        {
            "Version": "1.0",
            "Id": "38",
            "Person": {
                "Type": "CO",
                "Id": "163"
            },
            "Comment": "SshKey API test",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-10-18 15:07:07",
            "Modified": "2021-10-18 15:07:07",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_6.impact-development",
            "SshKeyAuthenticatorId": "7"
        }
    ]
}
### ssh_keys_view_one
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "36",
            "Person": {
                "Type": "CO",
                "Id": "163"
            },
            "Comment": "SshKey API test",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-10-18 15:04:22",
            "Modified": "2021-10-18 15:04:22",
            "Revision": "0",
            "Deleted": false,
            "ActorIdentifier": "co_6.impact-development",
            "SshKeyAuthenticatorId": "7"
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
            "Version": "1.0",
            "Id": "36",
            "Person": {
                "Type": "CO",
                "Id": "163"
            },
            "Comment": "NEW COMMENT",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-10-18 15:04:22",
            "Modified": "2021-10-18 15:07:08",
            "Revision": "1",
            "Deleted": false,
            "ActorIdentifier": "co_6.impact-development",
            "SshKeyAuthenticatorId": "7"
        }
    ]
}
### ssh_keys_delete
True
### ssh_keys_view_one (previously deleted ssh key)
{
    "ResponseType": "SshKeys",
    "Version": "1.0",
    "SshKeys": [
        {
            "Version": "1.0",
            "Id": "35",
            "Person": {
                "Type": "CO",
                "Id": "163"
            },
            "Comment": "NEW COMMENT",
            "Type": "ssh-rsa",
            "Skey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQCqlE3to9rJzLb5pUldEEeFi9gYlrIQ7WGFVvx4azWY95+nN8DkOukaK6IMnXP8t0icCWKN4ib6Q5Avea99HD8LQtsmxQjDIgwB/McX3cjXzwB6y8InEBB213bD6koHnsf/fELTTFt6MkJdNUbqOGFvHSUnN6BPUGQ42jXqPw6wVXzOR5nUX9bLc4uPS8moMVXWWK+lG7odGPXHju8AP/6gdjuRaFJnYE3OYoLNbEDnn6cneTtnz5AuQW0KBocc56MyOelNSzxoz/XcNvZH/Hp7wPAJNZhmN6/futZBjG0AzIBHs/J9JXszxq4FO3M4oqg0G+UgFQccXXi1afkJxu7z",
            "Created": "2021-10-18 15:00:08",
            "Modified": "2021-10-18 15:04:24",
            "Revision": "1",
            "Deleted": true,
            "ActorIdentifier": "co_6.impact-development",
            "SshKeyAuthenticatorId": "7"
        }
    ]
}
```
