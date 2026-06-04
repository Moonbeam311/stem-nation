# CI-1G — STEM Nation Opening Flow Route Map Lock

## Locked Student-Facing Opening Flow

/student
↓
/academy_opening
↓
/academy_identity
↓
/academy_cinematic
↓
/academy_arrival
↓
/first_gathering
↓
/baseline_inquiry

## Confirmed QA Result

The full browser flow has been confirmed working:

- /student loaded successfully
- Enter STEM Nation routed to /academy_opening
- Create Academy Identity routed to /academy_identity
- Begin Your Journey routed to /academy_cinematic
- Cinematic routed to /academy_arrival
- Follow the Gathering routed to /first_gathering
- Begin Observation routed to /baseline_inquiry

## Purpose of Each Route

### /student
Student-facing entry point.

### /academy_opening
Short cinematic prologue and STEM Nation invitation.

### /academy_identity
Student creates Academy identity.

Student begins as:
- New Arrival
- Academy Learner

Council advisors are not student avatars.

### /academy_cinematic
Full journey cinematic after identity creation.

Uses existing STEM Nation cinematic, Academy, and World Board assets.

Personalizes with localStorage key:

stemNationStudentIdentity

### /academy_arrival
Arrival at the Academy.

Includes:
- stillness
- bell
- movement toward the Council Hall
- transition into the First Gathering

### /first_gathering
Council Hall inquiry bridge.

Student overhears disagreement.

Guardian says:
- "Ah. You made it."
- "We need another set of eyes."
- "Come take a look."

Student sees unlabeled evidence.

### /baseline_inquiry
Academy Readiness Evaluation / The Washed-Out Crossing.

This is where the first formal inquiry begins.

## Explicitly Not Student-Facing in This Opening Path

The following routes are not part of the locked student opening path:

/avatar_select
/avatar_confirm
/backpack-lab
/backpack-lab-advanced
/academy_transition
/intro1
/intro2
/intro3
/intro4
/intro5

These may remain in the repository as archived, legacy, testing, or future reference pages, but they are not the locked student opening path.

## Future Experience Layering Plan

Layer 2 — Animation polish  
Layer 3 — Realistic portrait / avatar upgrade  
Layer 4 — Audio / narration / sound cues  
Layer 5 — Inquiry interaction polish  
