# STEM Nation

STEM Nation is an interactive learning project that combines student-facing story flow, inquiry missions, advisor/council experiences, classroom tools, and visual/audio assets.

## Current project areas

- Flask web app entry point: `web_app.py`
- Student and teacher screens: `templates/`
- Visual, audio, avatar, and JavaScript assets: `static/`
- Recovery notes, audits, version locks, and handoff records: `docs/`, `archive/`, `recovery_audit/`, and `version_locks/`
- Deployment package snapshots: `STEM_NATION_DEPLOY_PACKAGE/`

## Local setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python web_app.py
```

This repository is being organized as the working home for continued STEM Nation development.
