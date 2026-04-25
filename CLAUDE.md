# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**fabric-comanage-api** — a Python 3 client wrapper for the [COmanage REST API v1](https://spaces.at.internet2.edu/display/COmanage/REST+API+v1), published to PyPI as `fabric-comanage-api` (current version 0.2.0). Part of the [FABRIC Testbed](https://github.com/fabric-testbed) project. MIT licensed.

## Build & Install

```bash
# Development setup with uv
uv venv --python 3.12
uv pip install -e ".[dev]"

# Install from PyPI
pip install fabric-comanage-api
```

Build is configured via `pyproject.toml` (PEP 621 metadata, setuptools backend). Version is sourced from `comanage_api.__VERSION__`. Requires Python >= 3.9.

## Dependencies

Runtime: `requests>=2.25.0`. Dev: `pytest`, `requests-mock`, `python-dotenv` (installed via `pip install -e ".[dev]"`).

## Testing

Unit tests use `pytest` + `requests-mock`. Run with:

```bash
uv run pytest -v
```

138 tests across 10 files in `tests/` cover all endpoint modules: successful responses, parameter validation (`ValueError`), HTTP error propagation, and edge cases (deduplication, 204 empty, `parent_id=0`).

The `examples/` directory contains per-endpoint scripts that exercise the API against a live COmanage instance. To run them, copy `template.env` to `.env`, fill in credentials, then run individual example scripts (e.g., `uv run python examples/cous_example.py`).

## Architecture

`ComanageApi` (in `comanage_api/__init__.py`) is the single public class. It holds connection state (`_CO_API_URL`, `_CO_API_USER`, `_CO_API_PASS`, `_CO_API_ORG_ID`, `_CO_API_ORG_NAME`) and a `requests.Session` for HTTP Basic Auth.

**HTTP helpers** on `ComanageApi` (`_get`, `_post`, `_put`, `_delete`, `_get_by_entity`) centralize all request/response handling. Each API domain module delegates to these helpers.

Each API domain lives in its own private module (`_copeople.py`, `_cous.py`, `_sshkeys.py`, etc.). These modules define standalone functions that accept a `ComanageApi` instance as `self`. The `__init__.py` imports these functions and wraps them as methods on `ComanageApi`, creating a facade.

**API endpoint modules:**
- `_coorgidentitylinks.py` — CoOrgIdentityLink (requires COmanage v4.0.0+)
- `_copeople.py` — CoPerson
- `_copersonroles.py` — CoPersonRole
- `_cous.py` — COU (Collaborative Organizational Unit)
- `_emailaddresses.py` — EmailAddress
- `_identifiers.py` — Identifier
- `_names.py` — Name
- `_orgidentities.py` — OrgIdentity
- `_sshkeys.py` — SshKey (requires COmanage v4.0.0+, experimental)

**Pattern for each module:** functions named `<resource>_<action>` (e.g., `cous_add`, `cous_view_all`, `cous_delete`) that build paths/params/bodies and delegate to `self._get()`, `self._post()`, `self._put()`, or `self._delete()`. Unimplemented endpoints raise `NotImplementedError`.

## Configuration

Environment variables (see `template.env`):
- `COMANAGE_API_USER` / `COMANAGE_API_PASS` — API credentials
- `COMANAGE_API_CO_NAME` / `COMANAGE_API_CO_ID` — target CO
- `COMANAGE_API_URL` — registry base URL
- `COMANAGE_API_SSH_KEY_AUTHENTICATOR_ID` — optional SSH key authenticator plugin ID

## Conventions

- Instance-level constants for valid option sets: `STATUS_OPTIONS`, `AFFILIATION_OPTIONS`, `SSH_KEY_OPTIONS`, `ENTITY_OPTIONS`, `PERSON_OPTIONS`, `EMAILADDRESS_OPTIONS`.
- All API methods validate parameters against these option sets before making HTTP calls.
- Commit messages reference GitHub issues with `[#N]` prefix.
