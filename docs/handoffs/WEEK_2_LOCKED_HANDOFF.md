# STEM Nation — Week 2 Locked Handoff Summary

## Locked checkpoint

Week 2 now extends the Week 1 founding loop into survival pressure.

Current Week 2 route flow:

`/week2_survival_intro → /week2_survival_workspace → /week2_survival_archive → /week2_survival_print → /week2_survival_complete`

Week 1 remains locked and must not be rebuilt.

## Core educational logic

Week 1 established founding observation, responsibility, settlement defense, and archive creation.

Week 2 introduces the first survival test:

> Choosing land is not the same as surviving on it.

Students now move from founding direction into the early pressures that determine whether a settlement can endure.

Week 2 focuses on:
- food
- shelter
- labor
- scarcity
- risk
- consequence

The core transition is:

`Founding location → survival pressure → first survival plan → survival archive`

## Route details

### `/week2_survival_intro`

Role: Week 2 threshold intro.

Purpose:
- Introduces the idea that the settlement now faces survival pressure.
- Frames the lesson around food, shelter, labor, scarcity, risk, and consequence.
- Connects naturally from Week 1 completion and Project Hub.

Visible idea:

> Your people have a place to begin. Now they must survive there.

### `/week2_survival_workspace`

Role: First Survival Plan decision workspace.

Purpose:
- Students create the first survival plan for their civilization.
- This is the active drafting page.
- Students must complete all required fields before opening the survival archive.

Required fields:
1. Food Plan
2. Shelter Plan
3. Labor Assignment
4. Scarcity Rule
5. First Risk Response

Storage key:

`STEM_NATION_SURVIVAL_DECISION_V1`

Locked behavior:
- localStorage autosave
- visible save confirmation: **Survival plan saved locally.**
- completion counter updates
- Open Survival Archive remains locked until all five fields are complete
- Clear Draft / Start Over clears the saved draft and visible fields after confirmation
- user remains on workspace after clearing

Workspace buttons:
- Open Survival Archive
- Clear Draft / Start Over
- Back to Week 2 Intro
- Review Founding Archive

### `/week2_survival_archive`

Role: Survival Archive review/export page.

Purpose:
- Displays the saved Week 2 survival plan.
- Allows review, export, print/PDF path, reset, and completion.

Locked controls:
- Download Survival Archive
- Printable / Save as PDF
- Clear / Reset Survival Archive
- Return to Survival Workspace
- Week 2 Intro
- Week 1 Founding Archive
- Complete Week 2

Export filename:

`STEM_Nation_Week2_Survival_Archive.txt`

Reset behavior:
- Clear / Reset Survival Archive removes `STEM_NATION_SURVIVAL_DECISION_V1` from localStorage after confirmation.
- Archive page reloads.
- Returning to workspace should show cleared fields.

### `/week2_survival_print`

Role: Printable / Save-as-PDF survival archive.

Purpose:
- Teacher-friendly print view.
- Reads from `STEM_NATION_SURVIVAL_DECISION_V1`.
- Displays Food Plan, Shelter Plan, Labor Assignment, Scarcity Rule, and First Risk Response.
- Uses browser print dialog for PDF.

Important:
- Direct download is `.txt`.
- PDF is generated via browser **Print / Save as PDF**.

### `/week2_survival_complete`

Role: Week 2 closing / transition screen.

Purpose:
- Gives Week 2 a formal ending.
- Summarizes Survival Intro → Survival Workspace → Survival Archive → Export & Print.
- Reinforces the survival theme.
- Teases the next phase.

Key line:

> The first test of civilization is not power. It is survival.

Next phase teaser:

`Population, Production, and Growth`

## Current GitHub issue tracking

Issue #2 tracks the Week 2 survival workspace and archive build.

Confirmed in issue comments:
- survival workspace tested locally
- required fields validated
- localStorage saving confirmed
- survival archive accepted
- print/export accepted
- reset control accepted
- completion screen accepted

## Recent Week 2 commits

Known Week 2 commits include:

- `64a7f29 Add Week 2 survival intro`
- `884e68b Add Week 2 survival workspace and archive`
- `5c53faf Add Week 2 survival archive export and print view`

Additional local commits may include reset controls and the Week 2 completion screen if already committed/pushed from the desktop environment.

## Known design decisions

### Destructive actions

Workspace reset is called:

`Clear Draft / Start Over`

Archive reset is called:

`Clear / Reset Survival Archive`

Reason:
- workspace = active drafting
- archive = preserved review/export record

### Save layer

Week 2 uses localStorage only for now.

This is acceptable for prototype/classroom testing but not a backend teacher dashboard.

### Do not rebuild Week 1

Week 1 is locked and documented in:

`docs/handoffs/WEEK_1_LOCKED_HANDOFF.md`

Week 2 should build forward without rewriting Week 1 routes.

## Known limitations

1. Survival plan saves only in the same browser/device.
2. No backend database yet.
3. No teacher dashboard yet.
4. No student name/class/date metadata yet.
5. No combined Week 1 + Week 2 master archive export yet.
6. No simulation engine consequences have been applied from the survival decisions yet.
7. The next phase route has not been built yet.

## Recommended next build options

### Option A — Week 2 final polish

- Add student name/class/date to survival archive and print view.
- Add timestamp and record metadata to the export.
- Add a link from Week 1 completion screen to Week 2 intro if missing.
- Add a link from Week 2 intro to Week 2 workspace if missing.

### Option B — Combined archive

Create a combined Project Archive that displays both:
- Week 1 Settlement Decision Defense
- Week 2 First Survival Plan

Possible route:

`/civilization_archive`

### Option C — Start next phase

Begin:

`Week 3 — Population, Production, and Growth`

Core focus:
- population needs
- food production
- labor scaling
- storage
- growth pressure
- first prosperity/consequence tradeoffs

Suggested route:

`/week3_growth_intro`

## Safe resume directive

Use this directive in a future thread:

`Resume STEM Nation from Week 2 locked checkpoint. Do not rebuild Week 1 or Week 2. First verify git status, route flow, and localStorage keys. Then either build the combined civilization archive or begin Week 3 — Population, Production, and Growth.`
