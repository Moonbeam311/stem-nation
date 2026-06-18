# SN-AUDIT-2S — Board / Gameboard / Command Center Definitions

## Purpose

The project currently contains several board-like or hub-like surfaces. They are related, but they should not be treated as the same page.

This document locks the working distinction between:

- Gameboard
- World Board
- Scout Mission
- Strategic Map
- Civilization Command Center / Hub

---

## Gameboard

Route:

`/gameboard`

Role:

Full system overview.

Purpose:

Explains the complete STEM Nation simulation architecture, including:

- Situation Room
- World Board
- Build Chamber
- Council Chamber
- Civilization HUD
- Student multiplayer layer
- Hybrid classroom experience

Status:

Architecture / overview surface.

Not the primary student action surface yet.

---

## World Board

Route:

`/world-board`

Role:

Living world / region intelligence board.

Purpose:

Allows students to view regions and launch scouting missions.

Connected route:

`/scout/<region>`

Status:

World intelligence layer.

---

## Scout Mission

Route:

`/scout/<region>`

Role:

Field intelligence loop.

Purpose:

Students inspect water, food, travel, risks, and cultural sites, then return intelligence to the World Board.

Status:

World Board side loop.

---

## Strategic Map

Route:

`/map`

Role:

Active student decision surface.

Purpose:

Students choose a settlement region, observe land, record evidence, defend a founding decision, and unlock the Civilization Command Center.

Status:

Main student simulation action page.

---

## Civilization Command Center / Hub

Route:

`/hub`

Template:

`project_hub.html`

Student-facing name:

Civilization Command Center.

Purpose:

Displays the civilization record, founding archive, saved settlement defense, scores, competency profile, governance actions, and progress.

Status:

Student record / archive / command surface.

---

## Naming Rule

Keep the technical route:

`/hub`

Use the student-facing name:

Civilization Command Center

Do not rename the route until deployment and internal links are stable.

---

## Relationship

Recommended relationship:

Intro / Baseline Inquiry  
→ Region Investigation  
→ First Decision  
→ Strategic Map  
→ Civilization Command Center

World Board and Scout Mission may operate as a side loop:

Strategic Map  
↔ World Board  
↔ Scout Mission

Gameboard remains the full system overview.

---

## Working Principle

Do not collapse these pages into one.

They should be connected clearly, but each has a distinct job:

- Gameboard explains the full system.
- World Board shows the world.
- Scout Mission gathers field intelligence.
- Strategic Map makes the founding decision.
- Civilization Command Center records and evaluates progress.
