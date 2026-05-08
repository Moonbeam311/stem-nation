# STEM Nation — Educator Experience Locked Handoff Summary

## Locked educator-side checkpoint

This handoff documents the current educator-side architecture of STEM Nation.

Current teacher-side routes and prototype layers:

- `/teacher` — Teacher Command Center
- `/teacher_resource_library` — Teacher Resource Library prototype
- `/teacher_resource_attach` — Resource-to-Simulation Attachment Workflow prototype
- `/teacher_facilitation_engine` — Teacher Facilitation Engine prototype

Student-side Week 1 and Week 2 remain locked and should not be rebuilt while extending the educator layer.

## Core educator-side vision

The educator experience is not only a page of lesson plans. It is becoming a teacher operating system that wraps the student civilization simulation.

The educator side is designed to help teachers:

- understand what to teach
- know where to click
- pace the experience
- facilitate inquiry
- collect artifacts
- customize resources
- attach evidence to simulation stages
- eventually align lessons to district/state standards
- eventually use AI-assisted supports

Core principle:

> The student simulation creates decisions. The teacher engine deepens reasoning.

## Current stable student foundation

### Week 1 — Founding & Settlement

Locked flow:

`Academy Reflection → Responsibility → Decision Threshold → Strategic Map Defense → Project Hub → Download Text Archive / Printable Save-as-PDF Archive → Clear / Reset Archive → Restart Week 1 Flow → Week 1 Completion Screen`

### Week 2 — Survival & Consequence

Locked flow:

`/week2_survival_intro → /week2_survival_workspace → /week2_survival_archive → /week2_survival_print → /week2_survival_complete`

The educator experience wraps these flows and should not rewrite them.

## `/teacher` — Teacher Command Center

Role: main educator command center.

Current function:

- explains teacher as facilitator, not just lecturer
- restores Module 0 curriculum architecture
- includes Essential Question and Enduring Understandings
- explains Baseline Inquiry as observation/orientation rather than obvious pre-assessment
- clarifies the current build uses the active Academy pathway, not the older `region_experience` pathway
- includes pacing guide models
- includes Week 1 and Week 2 lesson-plan framing
- includes artifact collection workflow
- includes assessment/reflection categories
- includes implementation notes
- includes Auto District Alignment as a planned system
- links to Resource Library and Facilitation Engine

### Important curriculum alignment restored

Week 1 is explicitly:

`Module 0: Cartography & Orientation`

Teacher-side framing now includes:

- Essential Question
- Enduring Understandings
- Baseline Inquiry clarification
- Strategic Map Defense artifact logic
- inquiry/questioning emphasis

### Auto District Alignment planned system

This is a restored original educator-side requirement.

Current status: visible planned architecture only, not functional automation.

Future intended inputs:

- District / School System
- State
- Grade Band
- Subject / Course
- Standards Framework

Future intended outputs:

- standards-aligned objectives
- pacing suggestions
- assessment language
- artifact mapping
- implementation guidance

Important honesty rule:

> Do not claim live district standards automation is functional until built.

## `/teacher_resource_library` — Teacher Resource Library Prototype

Role: prototype architecture for teacher-controlled instructional resources.

Purpose:

Teachers should eventually upload, organize, edit, attach, and align instructional materials directly to simulation experiences.

Current status:

- UI/architecture prototype only
- no real uploads yet
- no file storage yet
- no authentication yet

Current resource categories:

- Lesson Plans
- Primary Sources
- Archives & Government Records
- Maps & Geography
- Media & Visuals
- Assessment Materials

### Archives & Government Records correction

The earlier narrow category `Congressional Records` was broadened to:

`Archives & Government Records`

This better includes:

- National Archives materials
- congressional records
- treaties
- hearings
- court records
- public laws
- government reports
- census records
- official historical documents

This category should be treated as a focused public-records / primary-source subcategory.

### Security/storage warning

Real uploads are intentionally not active yet.

Before enabling uploads, design must address:

- allowed file types
- maximum file size
- storage location
- authentication
- ownership
- classroom/district separation
- deletion policy
- privacy rules
- malware/virus scanning strategy

## `/teacher_resource_attach` — Resource-to-Simulation Attachment Workflow

Role: bridge between teacher resources and student simulation stages.

Purpose:

Teachers should eventually attach resources directly to simulation moments instead of merely storing them in a library.

Core workflow:

`Select Resource → Choose Tags → Attach to Simulation Stage → Add Teacher Notes → Preview Student Experience → Save to Lesson Packet`

Current prototype includes:

- sample resource cards
- simulation attachment targets
- student-facing evidence explanation
- no real upload/storage yet

### Attachment targets

Resources may eventually attach to:

- Module 0 / Baseline Inquiry
- Academy Reflection
- Responsibility Chamber
- Decision Threshold
- Strategic Map Defense
- Founding Archive
- Week 2 Survival Intro
- Week 2 Survival Workspace
- Week 2 Survival Archive
- future governance/growth modules

### Student-facing result

Attached resources may appear as:

- evidence cards
- primary-source prompts
- teacher context notes
- media references
- discussion prompts
- archive support materials

Goal:

> Transform STEM Nation into an evidence-driven civilization inquiry system.

## `/teacher_facilitation_engine` — Teacher Facilitation Engine Prototype

Role: real-time pedagogical orchestration layer.

Purpose:

The Teacher Facilitation Engine helps teachers know how to guide the lesson in real time.

It answers:

- when to pause
- what to ask
- what to challenge
- what misconceptions to watch for
- how to deepen reasoning
- when to collect evidence
- how to support struggling groups
- how to extend advanced groups

### Current sections

- Facilitation Philosophy
- Teacher Moves
- Suggested Pause Points
- Discussion Prompts
- Common Misconceptions To Watch For
- Differentiation & Support
- Evidence & Reasoning Checks

### Teacher Moves currently represented

- Pause & Probe
- Evidence Challenge
- Consequence Prediction
- Compare Civilizations
- Redirect Assumptions
- Archive Checkpoint

### Current misconceptions represented

- Good land guarantees survival.
- Resources solve every problem.
- Defense matters more than trade.
- One decision cannot affect the future.
- Scarcity only means food shortage.
- Expansion always improves civilization strength.

### Differentiation supports represented

- Sentence starters
- Partner discussion before writing
- Visual evidence cards
- Role-based responsibilities
- Oral-response option
- Advanced extension challenges

## AI-assisted teacher support — bookmarked for later

The original educator-side concept also included AI-generated or AI-assisted support.

Current decision:

- AI support belongs in the architecture.
- Do not build active AI automation yet.
- Human facilitation architecture comes first.

Future AI-assisted features may include:

- pacing suggestions
- lesson-plan draft generation
- discussion prompt generation
- differentiation suggestions
- standards alignment support
- uploaded resource summarization
- primary-source reading-level adaptation
- student-facing question generation
- misconception detection prompts
- teacher move recommendations

Important rule:

> AI should amplify strong pedagogy later, not replace the pedagogy now.

## Current repo / issue tracking

Relevant GitHub issue:

- Issue #4 — Original Teacher Experience Engine: lesson upload, edit, and artifact/media library

Recent educator-side commits include:

- `e42b9e7 Align Teacher Command Center with curriculum architecture`
- `e7fd055 Add teacher resource and attachment workflow prototypes`

If the Teacher Facilitation Engine commit has been pushed locally, include it after these in future updates.

## Known limitations

1. Teacher Resource Library is UI-only.
2. No real uploads yet.
3. No lesson editing persistence yet.
4. No authentication or teacher accounts yet.
5. No backend resource database yet.
6. No actual district standards automation yet.
7. No AI-assisted generation active yet.
8. No attached resources appear inside student routes yet.
9. No classroom packet builder yet.
10. No teacher dashboard/roster/artifact tracker yet.

## Recommended next build options

### Option A — Commit/lock Teacher Facilitation Engine

If not already pushed, commit:

- `web_app.py`
- `templates/teacher.html`
- `templates/teacher_facilitation_engine.html`

Suggested commit message:

`Add teacher facilitation engine prototype`

### Option B — Build Teacher Packet Builder Prototype

Possible route:

`/teacher_packet_builder`

Purpose:

- show how selected resources, lesson notes, and archive artifacts become a classroom packet
- still UI-only; no real file bundling yet

### Option C — Build Lesson Builder Prototype

Possible route:

`/teacher_lesson_builder`

Purpose:

- editable-looking lesson plan structure
- objective, essential question, teacher notes, pacing, artifact, discussion prompts
- no backend persistence yet

### Option D — Begin safe local JSON resource registry

Add a non-upload local data layer:

- `data/teacher_resources.json`
- sample resource records
- render sample resources dynamically

This is safer than real uploads and can prepare later backend work.

## Safe resume directive

Use this in a future thread:

`Resume STEM Nation from the Educator Experience locked checkpoint. Do not rebuild Week 1 or Week 2 student routes. Verify git status and the teacher routes: /teacher, /teacher_resource_library, /teacher_resource_attach, /teacher_facilitation_engine. Then either lock the facilitation engine commit, build a Teacher Packet Builder prototype, or design the Lesson Builder prototype.`
