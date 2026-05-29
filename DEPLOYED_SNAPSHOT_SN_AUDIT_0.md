# DEPLOYED SNAPSHOT — SN-AUDIT-0

## Purpose

This document records the deployed/default repository state before the STEM Nation reorganization and audit-control layer begins.

## Snapshot

- Repository: `Moonbeam311/stem-nation`
- Preserved branch: `archive/deployed-main-before-sn-audit-0`
- Audit branch: `audit/reorganize-stem-nation`
- Source branch at snapshot: `main`
- Snapshot commit SHA: `ec68faba1986bc9b4320b26f0d1b788f64cbd432`
- Date context: 2026-05-28

## Deployment Signals Observed

- `Procfile` entry: `web: gunicorn web_app:app`
- Runtime dependencies observed in `requirements.txt`:
  - `Flask==3.0.0`
  - `gunicorn==21.2.0`

## Protection Rule

No student-facing files, teacher-facing files, routes, templates, simulation logic, or deployment settings should be changed during SN-AUDIT-0. This phase is documentation/control only.

## Why This Exists

The deployed version must remain recoverable while the project is reorganized into stable, active, experimental, and archived layers.
