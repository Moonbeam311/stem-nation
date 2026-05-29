# SN-AUDIT-1C — GitHub vs Local vs Deployed Divergence Audit + Broken Route Stabilization Plan

## Purpose

Determine what can be proven from GitHub, what remains unknown locally, and what should be stabilized before any feature rebuild.

## Proven GitHub State

The audit branch was compared against the archived deployed branch:

- Base: `archive/deployed-main-before-sn-audit-0`
- Head: `audit/reorganize-stem-nation`
- Status: audit branch is ahead only by documentation commits
- App files changed: none
- Template files changed: none
- Deployment files changed: none

## Files Added on Audit Branch Only

- `ARCHIVE_POLICY.md`
- `BUILD_REGISTRY.md`
- `DEPLOYED_SNAPSHOT_SN_AUDIT_0.md`
- `README.md`
- `SN_AUDIT_1_REPOSITORY_ROUTE_INVENTORY.md`
- `SN_AUDIT_1B_MISSING_TEMPLATE_DEAD_END_VERIFICATION.md`
- `STUDENT_FLOW.md`
- `TEACHER_FLOW.md`

## Confirmed Protection Status

The archived deployed branch remains clean and unchanged from the pre-audit commit.

`main` has not been intentionally modified during SN-AUDIT-0 or SN-AUDIT-1.

## Divergence Types

### 1. GitHub vs Audit Branch

Known divergence: documentation only.

No product behavior divergence has been introduced by the audit process.

### 2. GitHub vs Deployed

Likely same as archived `main` unless external deployment is using a different commit, cached build, or another branch.

Needs deployment-provider confirmation if available.

### 3. Local vs GitHub

Unknown.

Evidence suggests local may contain files that GitHub does not, especially:

- `templates/project_hub.html`
- possibly other recent student/teacher builds
- possible River Crossing / baseline inquiry variants

## Confirmed Broken Route Risks in GitHub

| Route | Problem | Severity | Stabilization Recommendation |
|---|---|---|---|
| `/hub` | `project_hub.html` missing | High | Create temporary Hub placeholder or restore local template. |
| `/region_river` | `region_river.html` missing | Medium | Redirect to `/region_experience?region=river` or create placeholder. |
| `/academy_thinking` | Redirects to `academy_individual.html` instead of `/academy_individual` | Medium | Correct redirect path. |
| `/academy_decision` | No visible continuation | Medium | Add continuation button to World Board placeholder or Hub. |
| `/map` | Simulation Mode is informational, not actual World Board | Strategic | Reclassify as placeholder; later replace with World Board. |
| `/teacher` | Educator page is informational, not Teacher Dashboard | Strategic | Reclassify as placeholder; later build Teacher Command Center. |

## Stabilization Plan

### Stabilization Principle

Fix broken navigation without redesigning the product.

Do not introduce major new UI, simulation logic, data models, or teacher systems during stabilization.

### Step 1 — Protect Current State

Already complete:

- Deployed archive branch exists.
- Audit branch exists.
- Documentation-only audit commits exist.

### Step 2 — Verify Local Files Manually

Before creating placeholders, check local machine for:

```bash
cd ~/Desktop/stem-nation/stem-nation

find templates -maxdepth 2 -type f | sort
find . -iname '*project*hub*' -o -iname '*region*river*' -o -iname '*river*crossing*' -o -iname '*baseline*'

git status --short
git branch --show-current
git log --oneline -5
```

If local files exist, restore them from local to GitHub instead of creating placeholders.

### Step 3 — If Local Files Are Missing, Create Safe Placeholders

Safe placeholder files:

- `templates/project_hub.html`
- optional `templates/region_river.html`

Purpose: stop broken navigation.

### Step 4 — Patch Legacy Redirect

In `templates/academy_thinking.html`, change:

```text
academy_individual.html
```

to:

```text
/academy_individual
```

### Step 5 — Add Student Flow Continuation

In `templates/academy_decision.html`, add a button or timed continuation to:

```text
/map
```

Short-term label:

```text
Continue to Simulation Mode
```

Later this should become:

```text
Continue to World Board
```

### Step 6 — Update Build Registry

Classify routes as:

- STABLE
- ACTIVE
- PLACEHOLDER
- BROKEN
- EXPERIMENTAL
- ARCHIVED

## Recommended Immediate Fix Order

1. Local verification first.
2. Restore real `project_hub.html` if local exists.
3. Otherwise create temporary `project_hub.html` placeholder.
4. Redirect `/region_river` safely.
5. Fix `academy_thinking` redirect.
6. Add continuation to `academy_decision`.
7. Update `BUILD_REGISTRY.md`.

## Do Not Do Yet

- Do not rename every route yet.
- Do not move templates into folders yet.
- Do not merge into `main` yet.
- Do not rebuild teacher dashboard yet.
- Do not replace Simulation Mode with World Board yet.

## Conclusion

The audit process has not changed the product behavior. The main divergence risk is not from the audit branch. The main divergence risk is between the current GitHub repository and the user's local working folder, where several more advanced files may exist but are not committed.

The next safest practical step is local verification before applying route stabilization patches.
