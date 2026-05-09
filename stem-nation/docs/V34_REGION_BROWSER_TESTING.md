# STEM Nation V34 — Browser Region Testing Guide

## Purpose

This guide verifies that the V34 civilization engine responds correctly to founding regions.

The browser stores simulation state locally using:

- `STEM_NATION_SETTLEMENT_DEFENSE_V1`
- `STEM_NATION_CIVILIZATION_STATE_V34`

Because of this, each region test should begin with a clean reset.

---

## Safe Reset Before Each Region Test

1. Open:

```text
http://127.0.0.1:5000/hub
