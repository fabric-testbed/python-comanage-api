# Changelog

All notable changes to `fabric-comanage-api` are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-25

A substantial refactor focused on robustness, testability, and packaging
modernization. The public API is fully preserved — all existing methods retain
their names, signatures, and return types.

### Added

- Configurable HTTP request `timeout` parameter on `ComanageApi` (default: 30s).
- Automatic retry with exponential backoff on transient failures (HTTP 429, 500,
  502, 503, 504) via `urllib3.util.Retry` mounted on an `HTTPAdapter`. Retries
  are applied to all HTTP methods.
- Structured logging under the `comanage_api` logger. A `NullHandler` is
  registered so callers who don't configure logging see no output; callers who
  enable logging get DEBUG (request URL/method/params), INFO (success), and
  WARNING (non-2xx before raise) messages. Credentials and request/response
  bodies are never logged.
- 138 unit tests across 10 files in `tests/`, using `pytest` + `requests-mock`,
  covering all 9 endpoint modules plus the core `ComanageApi` class. Tests
  exercise success paths, parameter validation, HTTP error propagation, and
  edge cases (deduplication, 204 empty responses, `parent_id=0`).
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) running `ruff` lint
  on Python 3.12 and `pytest` across Python 3.9, 3.10, 3.11, and 3.12.
- `ruff` configuration in `pyproject.toml` (line-length 120, rules E/F/I/W).
- Centralized HTTP helpers on `ComanageApi`: `_get`, `_post`, `_put`, `_delete`,
  and `_get_by_entity` — every endpoint module now delegates to these.

### Changed

- **Refactored to mixin architecture.** Each `_*.py` module now exports a mixin
  class (e.g. `CoPeopleMixin`, `COUsMixin`, `SshKeysMixin`) and `ComanageApi`
  inherits from all 9. The 60-method passthrough wrapper layer in `__init__.py`
  is gone.
- Migrated all packaging metadata to `pyproject.toml` (PEP 621). Removed
  `setup.cfg`, `requirements.txt`, and `MANIFEST.in`.
- Bumped minimum supported Python from 3.6 to 3.9.
- Adopted `uv` as the recommended package manager for development.
- Invalid enum values now raise `ValueError` instead of `TypeError` across
  `_copersonroles`, `_emailaddresses`, `_identifiers`, `_names`, `_sshkeys`,
  and `_coorgidentitylinks`.
- Replaced four copies of the validate-and-GET pattern in `view_per_*` methods
  with a single `_get_by_entity` helper.

### Fixed

- `cous_edit()` now correctly distinguishes the three `parent_id` cases —
  *value provided* (set), *0* (clear parent), *None* (keep existing) — using
  explicit `is not None` checks.
- `ssh_keys_add()` no longer stringifies a missing comment as the literal
  `"None"`; it now sends an empty string when no comment is supplied.
- `org_identities_view_all()` docstring corrected (previously a copy-paste of
  the EmailAddresses docstring).

### Removed

- `requests-mock` removed from runtime `install_requires` (it remains in dev
  dependencies). The `_MOCK_501_URL` / `_mock_session` machinery in
  `__init__.py` is gone; unimplemented endpoints now raise `NotImplementedError`.

## [0.1.5]

Prior releases — see git history.
