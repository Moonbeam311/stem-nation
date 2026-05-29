# STEM Nation / Nation Builder

STEM Nation is an AI-integrated civic simulation and media lab for inquiry-based learning, civilization systems, and student decision-making.

## Current Audit Phase

This repository is under SN-AUDIT-0D: Control Layer Installation.

The purpose of this phase is to create a clear source of truth before reorganizing code, routes, templates, student experiences, teacher tools, or deployment behavior.

## Protected Deployed Version

The deployed/default state was preserved before this audit layer began.

- Archive branch: `archive/deployed-main-before-sn-audit-0`
- Audit branch: `audit/reorganize-stem-nation`
- Snapshot file: `DEPLOYED_SNAPSHOT_SN_AUDIT_0.md`

## Product Identity

- Platform: STEM Nation
- Core simulation engine: Nation Builder
- Student onboarding/training layer: The Academy
- Inquiry assessment layer: Academy Readiness Evaluation / Inquiry Trials
- Puzzle logic layer: Academy Training Exercises
- Main simulation interface: World Board / Civilization Operations Board
- Teacher layer: Teacher Command Center

## Audit Control Files

- `BUILD_REGISTRY.md` — status and purpose registry for features/routes/files
- `ROUTE_MAP.md` — intended route architecture
- `STUDENT_FLOW.md` — locked student experience spine
- `TEACHER_FLOW.md` — teacher/admin separation plan
- `DEPLOYMENT_STATUS.md` — deployed vs development classification
- `ARCHIVE_POLICY.md` — rules for preserving, archiving, and deprecating work

## Audit Rule

No production behavior should be changed during SN-AUDIT-0. This phase is documentation/control only.
