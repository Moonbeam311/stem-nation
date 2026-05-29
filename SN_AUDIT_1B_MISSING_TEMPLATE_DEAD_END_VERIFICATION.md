# SN-AUDIT-1B — Missing Template & Dead-End Route Verification

## Purpose

Verify route/template gaps and student-flow dead ends before modifying the deployed build.

## Confirmed Missing Templates

| Route | Expected Template | Status | Severity | Notes |
|---|---|---|---|---|
| `/hub` | `templates/project_hub.html` | Missing from GitHub audit branch | High | Multiple public-facing pages link to `/hub`; likely broken route. |
| `/region_river` | `templates/region_river.html` | Missing from GitHub audit branch | Medium | Route exists in `web_app.py`, but template is absent. |

## Confirmed Existing Templates Previously Unverified

| Route | Template | Status | Notes |
|---|---|---|---|
| `/academy_thinking` | `templates/academy_thinking.html` | Exists | But contains a likely bad redirect to `academy_individual.html` instead of `/academy_individual`. |
| `/partners` | `templates/partners.html` | Exists | Public-facing partnership/grants page. Links to `/hub`, which appears broken. |

## Dead-End / Broken Flow Findings

### `/academy_thinking`

The page exists but redirects to:

```text
academy_individual.html
```

This does not match the Flask route:

```text
/academy_individual
```

Recommended classification:

```text
BROKEN REDIRECT / LEGACY PATH
```

### `/hub`

`web_app.py` defines:

```text
@app.route("/hub")
def hub():
    return render_template("project_hub.html")
```

But `templates/project_hub.html` was not found.

Recommended classification:

```text
BROKEN ROUTE / MISSING TEMPLATE
```

### `/region_river`

`web_app.py` defines:

```text
@app.route("/region_river")
def region_river():
    return render_template("region_river.html")
```

But `templates/region_river.html` was not found.

Recommended classification:

```text
BROKEN ROUTE / MISSING TEMPLATE
```

### `/academy_decision`

The page exists and displays a transition message, but no continuation route is visible in the inspected template.

Recommended classification:

```text
INCOMPLETE STUDENT FLOW END
```

## Public Page Link Risk

The following inspected pages link to `/hub`:

- `teacher.html`
- `map.html`
- `partners.html`

Since `/hub` appears to be missing its template, these buttons likely create errors in the deployed GitHub version.

## Immediate Recommendations

Do not redesign yet. First perform a safe stabilization pass on the audit branch.

Recommended next step:

```text
SN-AUDIT-1C — Broken Route Stabilization Plan
```

Possible safe fixes to propose, not yet apply:

1. Create a temporary `project_hub.html` placeholder so `/hub` stops breaking.
2. Redirect `/region_river` to `/region_experience?region=river` or create a placeholder page.
3. Fix `/academy_thinking` redirect from `academy_individual.html` to `/academy_individual`.
4. Add a continuation button to `/academy_decision` leading to a future World Board placeholder.
5. Update `BUILD_REGISTRY.md` with confirmed broken statuses.

## Key Conclusion

The deployed route system is not just incomplete; it contains at least two likely broken routes and at least one legacy redirect mismatch. These must be stabilized before major student experience redesign.
