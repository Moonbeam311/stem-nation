# SN-AUDIT-1 — Repository & Route Inventory Audit

## Scope

Read-only audit of the active GitHub repository and deployed Flask entry point.

Repository: `Moonbeam311/stem-nation`
Audit branch: `audit/reorganize-stem-nation`
Protected deployed archive: `archive/deployed-main-before-sn-audit-0`

## Confirmed Deployment Entry

`Procfile` points deployment to:

```text
web: gunicorn web_app:app
```

Primary app file:

```text
web_app.py
```

No `app.py` was found during this audit pass.

## Confirmed Flask Routes in `web_app.py`

| Route | Template / Response | Current Classification | Audience | Notes |
|---|---|---|---|---|
| `/` | `landing.html` | STABLE / ACTIVE | Public / Student / Teacher | Main entry surface. |
| `/decision_bridge.html` | `decision_bridge.html` | ACTIVE | Student | Bridge after cinematic intro. Uses old `.html` route naming. |
| `/intro1` | `intro1.html` | ACTIVE | Student | Cinematic sequence. |
| `/intro2` | `intro2.html` | ACTIVE | Student | Cinematic sequence. |
| `/intro3` | `intro3.html` | ACTIVE | Student | Cinematic sequence. |
| `/intro4` | `intro4.html` | ACTIVE | Student | Cinematic sequence. |
| `/intro5` | `intro5.html` | ACTIVE | Student | Auto-routes to decision bridge when audio ends. |
| `/world_select.html` | `world_select.html` | ACTIVE | Student | World selection exists but route naming is legacy. |
| `/region_experience` | `region_experience.html` | ACTIVE | Student | Currently titled Baseline Inquiry; actually functions as first land inquiry. |
| `/academy_individual` | `academy_individual.html` | ACTIVE | Student | Phase 2: Shape the Nation / map marker placement. |
| `/academy_role` | `academy_role.html` | ACTIVE | Student | Phase 3: Assign Responsibility. |
| `/academy_thinking` | `academy_thinking.html` | UNVERIFIED | Student | Route exists, template not inspected in this pass. |
| `/academy_decision` | `academy_decision.html` | ACTIVE / INCOMPLETE | Student | Applies test decision and shows transition text; no next route found. |
| `/teacher` | `teacher.html` | ACTIVE / PLACEHOLDER | Teacher | Educator info page; not yet a true teacher dashboard. |
| `/map` | `map.html` | ACTIVE / PLACEHOLDER | Student / Simulation | Simulation Mode explanation, not full world board. |
| `/partners` | `partners.html` | UNVERIFIED | Public / Grants | Route exists, template not inspected in this pass. |
| `/region_river` | `region_river.html` | UNVERIFIED | Student | Route exists, likely older region-specific page. |
| `/decision` POST | JSON `{ok: True}` | EXPERIMENTAL | Engine/API | Placeholder endpoint. |
| `/hub` | `project_hub.html` | BROKEN / MISSING IN REPO PASS | Student / Teacher? | Route exists, but template was not found by GitHub fetch. |

## Current Student Path Observed

```text
/ 
-> /intro1
-> /intro2
-> /intro3
-> /intro4
-> /intro5
-> /decision_bridge.html
-> /world_select.html
-> /region_experience?region=<world>
-> /academy_individual?world=<world>
-> /academy_role
-> /academy_decision
```

## Critical Findings

### 1. The deployed product already has a strong public landing page.

Landing page has four doors:

- Student Experience
- Educator Access
- Simulation Mode
- Partnerships & Grants

This is strategically useful, but the behind-the-door experiences are uneven.

### 2. Student flow exists, but naming is inconsistent.

The student path includes cinematic intro, bridge, world selection, baseline inquiry, Phase 2 nation shaping, Phase 3 responsibility, and a decision transition.

However, student-facing language still mixes:

- Baseline Inquiry
- Phase 2
- Phase 3
- Academy
- Simulation Mode
- Project Hub

Recommended correction: make these all part of a coherent Academy-to-Nation Builder sequence.

### 3. `region_experience.html` is mislabeled.

It is titled `Baseline Inquiry`, but it functions as the first land observation/inquiry mission after world selection.

Recommended student-facing name:

```text
Inquiry Trial 1: The Living Land
```

Internal file name can remain unchanged until refactor.

### 4. `/map` is not yet the true World Board.

`map.html` is currently a Simulation Mode information surface. It describes strategic systems thinking but does not yet function as the main simulation board.

Recommended classification:

```text
ACTIVE PLACEHOLDER
```

### 5. `/teacher` is not yet a true teacher dashboard.

`teacher.html` is an Educator Access information surface. It is useful for public/investor/demo purposes, but it is not yet the Teacher Command Center.

Recommended classification:

```text
ACTIVE PLACEHOLDER
```

### 6. `/hub` route may be broken in the deployed GitHub version.

`web_app.py` routes `/hub` to `project_hub.html`, but GitHub fetch did not find `templates/project_hub.html` during this pass.

Recommended next verification:

- confirm whether `project_hub.html` exists locally but not in GitHub
- confirm whether the deployed app errors when `/hub` is opened
- either restore the missing template or remove/redirect the route

### 7. `/academy_decision` appears incomplete.

The route applies a hardcoded test decision using the engine pipeline and renders a transition page. The template has no visible continuation route.

Recommended classification:

```text
ACTIVE / INCOMPLETE
```

### 8. There is an engine layer present.

`web_app.py` imports:

```text
from engines.engine_pipeline import apply_decision
```

This confirms the simulation/engine architecture has begun, but route integration is not mature yet.

## Recommended Status Labels

| Layer | Current Status | Recommendation |
|---|---|---|
| Public Landing | STABLE | Keep in deployed demo. |
| Cinematic Intro | ACTIVE | Keep, but later consolidate route naming. |
| Decision Bridge | ACTIVE | Rename/reframe as Academy Transition later. |
| World Select | ACTIVE | Keep; change wording and route alias later. |
| Region Experience | ACTIVE | Reframe as Inquiry Trial 1. |
| Academy Individual | ACTIVE | Reframe as Build / Settlement Mission. |
| Academy Role | ACTIVE | Reframe as Governance / Responsibility Mission. |
| Academy Decision | INCOMPLETE | Needs continuation or deprecation. |
| Simulation Mode `/map` | PLACEHOLDER | Later replace with actual World Board. |
| Teacher `/teacher` | PLACEHOLDER | Later replace with Teacher Command Center. |
| Project Hub `/hub` | BROKEN / NEEDS VERIFY | Confirm missing template. |

## Surgical Recommendation

Do not build new features yet.

Next step should be:

```text
SN-AUDIT-1B — Missing Template and Broken Route Verification
```

Focus:

1. Confirm missing templates.
2. Confirm dead-end routes.
3. Confirm student path completion.
4. Confirm which local files are not in GitHub.
5. Update BUILD_REGISTRY.md with classifications.
