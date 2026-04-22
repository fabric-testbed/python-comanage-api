import json
import logging

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ._coorgidentitylinks import CoOrgIdentityLinksMixin
from ._copeople import CoPeopleMixin
from ._copersonroles import CoPersonRolesMixin
from ._cous import COUsMixin
from ._emailaddresses import EmailAddressesMixin
from ._identifiers import IdentifiersMixin
from ._names import NamesMixin
from ._orgidentities import OrgIdentitiesMixin
from ._sshkeys import SshKeysMixin

# fabric-comanage-api version
__VERSION__ = "0.1.5"

# Library logging: NullHandler prevents "last resort" output for callers
# who don't configure logging. Callers who want logs should add their own
# handler to the 'comanage_api' logger.
logging.getLogger(__name__).addHandler(logging.NullHandler())


class ComanageApi(
    CoOrgIdentityLinksMixin,
    CoPeopleMixin,
    CoPersonRolesMixin,
    COUsMixin,
    EmailAddressesMixin,
    IdentifiersMixin,
    NamesMixin,
    OrgIdentitiesMixin,
    SshKeysMixin,
):
    """
    fabric-comanage-api:

    Provide a limited Python 3 client implementation (wrapper) for
    COmanage REST API v1: https://spaces.at.internet2.edu/display/COmanage/REST+API+v1


    Attributes
    ----------
    co_api_url: str
        COmanage registry URL (required)
    co_api_user: str
        COmanage API username (required)
    co_api_pass: str
        COmanage API password (required)
    co_api_org_id: int
        COmanage Org ID (required)
    co_api_org_name: str
        COmanage Org Name (required)
    co_ssh_key_authenticator_id: int = None
        SSH Authenticator Plugin ID (optional)
    timeout: int = 30
        HTTP request timeout in seconds (optional, default 30)
    """

    _log = logging.getLogger(__name__)

    def __init__(self, co_api_url: str, co_api_user: str, co_api_pass: str, co_api_org_id: int,
                 co_api_org_name: str, co_ssh_key_authenticator_id: int = None, timeout: int = 30):
        # COmanage API user and pass
        self._CO_API_USER = str(co_api_user)
        self._CO_API_PASS = str(co_api_pass)
        # COmanage CO information
        self._CO_API_ORG_NAME = str(co_api_org_name)
        self._CO_API_ORG_ID = int(co_api_org_id)
        # COmanage Registry URL
        if str(co_api_url).endswith('/'):
            self._CO_API_URL = str(co_api_url)[:-1]
        else:
            self._CO_API_URL = str(co_api_url)
        # COmanage SshKeyAuthenticatorId
        if co_ssh_key_authenticator_id:
            self._CO_SSH_KEY_AUTHENTICATOR_ID = int(co_ssh_key_authenticator_id)
        else:
            self._CO_SSH_KEY_AUTHENTICATOR_ID = 0
        # HTTP request timeout
        self._timeout = timeout
        # Status Type options
        self.STATUS_OPTIONS = ['Active', 'Approved', 'Confirmed', 'Declined', 'Deleted', 'Denied', 'Duplicate',
                               'Expired',
                               'GracePeriod', 'Invited', 'Pending', 'PendingApproval', 'PendingConfirmation',
                               'Suspended']
        # Affiliation Type options
        self.AFFILIATION_OPTIONS = ['affiliate', 'alum', 'employee', 'faculty', 'member', 'staff', 'student']
        # EmailAddress Type options
        self.EMAILADDRESS_OPTIONS = ['codeptid', 'copersonid', 'organizationid', 'orgidentityid']
        # Entity Type options
        self.ENTITY_OPTIONS = ['codeptid', 'cogroupid', 'copersonid', 'organizationid', 'orgidentityid']
        # Person Type options
        self.PERSON_OPTIONS = ['copersonid', 'orgidentityid']
        # SSH Key Type options
        self.SSH_KEY_OPTIONS = ['ssh-dss', 'ecdsa-sha2-nistp256', 'ecdsa-sha2-nistp384', 'ecdsa-sha2-nistp521',
                                'ssh-ed25519', 'ssh-rsa', 'ssh-rsa1']
        # create comanage_api session with retry logic
        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=['GET', 'POST', 'PUT', 'DELETE'],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._s = Session()
        self._s.mount('https://', adapter)
        self._s.mount('http://', adapter)
        self._s.headers = {'Content-Type': 'application/json'}
        self._s.auth = (self._CO_API_USER, self._CO_API_PASS)

    # HTTP helpers
    def _get(self, path: str, params: dict = None) -> dict:
        url = f"{self._CO_API_URL}/{path}"
        self._log.debug('GET %s params=%s', url, params)
        resp = self._s.get(url, params=params, timeout=self._timeout)
        if not resp.ok:
            self._log.warning('GET %s returned %s', url, resp.status_code)
        resp.raise_for_status()
        self._log.info('GET %s OK', url)
        return resp.json()

    def _post(self, path: str, data: dict) -> dict:
        url = f"{self._CO_API_URL}/{path}"
        self._log.debug('POST %s', url)
        resp = self._s.post(url, data=json.dumps(data), timeout=self._timeout)
        if not resp.ok:
            self._log.warning('POST %s returned %s', url, resp.status_code)
        resp.raise_for_status()
        self._log.info('POST %s OK (%s)', url, resp.status_code)
        return resp.json()

    def _put(self, path: str, data: dict) -> bool:
        url = f"{self._CO_API_URL}/{path}"
        self._log.debug('PUT %s', url)
        resp = self._s.put(url, data=json.dumps(data), timeout=self._timeout)
        if not resp.ok:
            self._log.warning('PUT %s returned %s', url, resp.status_code)
        resp.raise_for_status()
        self._log.info('PUT %s OK', url)
        return True

    def _delete(self, path: str, params: dict = None) -> bool:
        url = f"{self._CO_API_URL}/{path}"
        self._log.debug('DELETE %s params=%s', url, params)
        resp = self._s.delete(url, params=params, timeout=self._timeout)
        if not resp.ok:
            self._log.warning('DELETE %s returned %s', url, resp.status_code)
        resp.raise_for_status()
        self._log.info('DELETE %s OK', url)
        return True

    def _get_by_entity(self, path: str, entity_type: str, entity_id: int,
                       valid_options: list, field_name: str) -> dict:
        if not entity_type:
            entity_type = 'copersonid'
        else:
            entity_type = str(entity_type).lower()
        if entity_type not in valid_options:
            raise ValueError(f"Invalid Fields '{field_name}'")
        return self._get(path, params={entity_type: str(entity_id)})
