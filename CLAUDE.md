# fabric-comanage-api

## What this is
Python 3 client wrapper for the [COmanage REST API v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1), published to PyPI as `fabric-comanage-api`. Part of the FABRIC Testbed. MIT.

## Stack
Python >=3.10. Runtime deps: `requests`, `urllib3`, `idna` (pinned directly for CVE floors). Dev: `pytest`, `requests-mock`, `python-dotenv`, `ruff`. setuptools backend (PEP 621); version sourced dynamically from `comanage_api.__VERSION__`.

## Conventions
- `ComanageApi` (`comanage_api/__init__.py`) is the single public class. It holds connection state + a `requests.Session` (HTTP Basic Auth) and centralizes all I/O in helpers `_get`/`_post`/`_put`/`_delete`/`_get_by_entity`.
- Each API domain lives in its own private module as a mixin class (e.g. `COUsMixin`, `SshKeysMixin`); `ComanageApi` inherits all nine and they call the shared HTTP helpers via `self`. Methods named `<resource>_<action>` (e.g. `cous_add`, `cous_view_all`).
  - `_coorgidentitylinks.py` — CoOrgIdentityLink (requires COmanage v4.0.0+)
  - `_copeople.py` — CoPerson
  - `_copersonroles.py` — CoPersonRole
  - `_cous.py` — COU (Collaborative Organizational Unit)
  - `_emailaddresses.py` — EmailAddress
  - `_identifiers.py` — Identifier
  - `_names.py` — Name
  - `_orgidentities.py` — OrgIdentity
  - `_sshkeys.py` — SshKey (requires COmanage v4.0.0+, experimental)
- Methods validate params against instance-level option sets (`STATUS_OPTIONS`, `AFFILIATION_OPTIONS`, `SSH_KEY_OPTIONS`, `ENTITY_OPTIONS`, `PERSON_OPTIONS`, `EMAILADDRESS_OPTIONS`) before any HTTP call; bad input raises `ValueError`.
- Unimplemented endpoints raise `NotImplementedError`.
- Commit messages reference GitHub issues with `[#N]` prefix.

## Commands
```bash
uv venv --python 3.12 && uv pip install -e ".[dev]"   # dev setup
uv run pytest -v                                        # tests (requests-mock, no live calls)
uv run ruff check . && uv run ruff format .            # lint/format (line-length 120, examples/ excluded)
```
Examples in `examples/` hit a LIVE COmanage instance: copy `template.env` -> `.env`, fill creds, then `uv run python examples/cous_example.py`.

## Gotchas
- All requests have a configurable timeout (default 30s) and auto-retry w/ exponential backoff on 429/500/502/503/504.
- `_coorgidentitylinks.py` requires COmanage v4.0.0+; `_sshkeys.py` requires v4.0.0+ and is experimental.
- Logging via stdlib `logging` under the `comanage_api` logger — silent by default.
- Config env vars: `COMANAGE_API_USER`/`_PASS`, `COMANAGE_API_CO_NAME`/`_CO_ID`, `COMANAGE_API_URL`, optional `COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID`.

## Don't
- Don't run `examples/` against production without verifying `.env` points at a test CO — they perform real add/delete.
