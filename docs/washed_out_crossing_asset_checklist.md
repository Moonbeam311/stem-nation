# Washed-Out Crossing Asset Checklist

## Purpose

This checklist tracks the visual assets needed for the illustrated Washed-Out Crossing mission prototype.

## Current Asset Status

- **Background**
  - Key: `background`
  - Path: `world_river.jpg`
  - Status: **READY**
  - Note: Existing mapped background is acceptable for now.

- **Bridge**
  - Key: `bridge`
  - Path: `images/missions/washed_out_crossing/bridge_damaged.png`
  - Status: **MISSING**
  - Note: Custom damaged bridge art still needed.

- **River**
  - Key: `river`
  - Path: `images/missions/washed_out_crossing/river_current.png`
  - Status: **MISSING**
  - Note: Custom animated/current river image still needed.

- **Guardian Neutral**
  - Key: `guardian_neutral`
  - Path: `avatars/student/guardian.png`
  - Status: **READY**
  - Note: Mapped to existing Guardian avatar.

- **Guardian Alert**
  - Key: `guardian_alert`
  - Path: `avatars/student/guardian.png`
  - Status: **READY**
  - Note: Currently mapped to same Guardian image; future expression state optional.

- **Guardian Speaking**
  - Key: `guardian_speaking`
  - Path: `avatars/student/guardian.png`
  - Status: **READY**
  - Note: Currently mapped to same Guardian image; future speaking state optional.

- **Guardian Success**
  - Key: `guardian_success`
  - Path: `avatars/student/guardian.png`
  - Status: **READY**
  - Note: Currently mapped to same Guardian image; future success state optional.

## Custom Art Still Needed

These files should eventually be created or exported:

```text
static/images/missions/washed_out_crossing/bridge_damaged.png
static/images/missions/washed_out_crossing/river_current.png
```

Optional future Guardian expression files:

```text
static/images/missions/washed_out_crossing/guardian_neutral.png
static/images/missions/washed_out_crossing/guardian_alert.png
static/images/missions/washed_out_crossing/guardian_speaking.png
static/images/missions/washed_out_crossing/guardian_success.png
```

For now, the mission correctly uses the existing Guardian asset:

```text
static/avatars/student/guardian.png
```

## Rule

Do not treat missing Bridge/River custom images as a failure. CSS placeholders are active until final mission art is added.
