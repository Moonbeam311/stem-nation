# SN-AUDIT-2AD — Intro 5 Navigation Decision

## Finding

Intro 5 text and audio now match, and the visible words stay long enough for the narration.

The page does not need to auto-advance to `/backpack-lab`.

## Decision

Keep Intro 5 as a manual transition page.

Student-facing behavior:

1. Intro 5 narration plays.
2. Text remains visible long enough to match the narration.
3. Student uses the button to continue to the Backpack Puzzle.

## Approved Button

Continue to Backpack Puzzle

## Route

`/intro5`
→ `/backpack-lab`

## Reason

Manual continuation is safer for classroom use because students may need a moment before entering the puzzle activity. It also prevents audio/text cutoff issues caused by fixed timers or browser playback timing.
