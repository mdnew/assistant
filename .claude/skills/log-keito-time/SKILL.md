---
name: log-keito-time
description: >-
  Proposes Keito time entries from standup or chat, confirms with Matt, then creates them via Keito API v2.
  Use when Matt says "log time in Keito", "log my time", "log my timesheet", "keito time",
  or the legacy phrasings "log time in Harvest" / "harvest time" (Uptech moved off Harvest in Sept 2026),
  or after standup when he wants timesheet entries logged.
  Never POST to Keito until Matt explicitly approves the proposed list (or edited list).
---

# Log time in Keito

> **Migrated from Harvest, Sept 2026.** Uptech moved time tracking from Harvest to **Keito** (`keito.ai`). If Matt says "Harvest", he means this. Do not call the Harvest API. See `decisions/2026-09-21-move-time-tracking-from-harvest-to-keito.md`.

## Prerequisites

Matt needs **Keito API credentials** available in the environment when the agent runs shell commands:

| Variable | Source |
|----------|--------|
| `KEITO_API_KEY` | Keito web app → Settings → API & Developers → create a **full-access integration key** (`kto_...`, shown once) |
| `KEITO_ACCOUNT_ID` | Same page, labeled **Company ID** |

A **personal read-only sync key will not work**: it cannot write time entries or read `/tasks`. If the variables are missing, stop and tell Matt to add them (e.g. shell profile), then retry. Do not echo token values.

## Mapping file (required for reliable logging)

Keito needs **string** `project_id` and `task_id` per entry (opaque CUIDs like `cmtundo0r00595gmk2zlnem9u`, not Harvest's integers). Tasks are **workspace-level and shared across projects**, so one task id is valid on every project it is assigned to.

1. **Look for** a mapping file, in order:
   - `reference/keito-time-mapping.md` in the assistant repo
   - `.claude/skills/log-keito-time/mapping.md`
2. If none exists or a client code is missing, run `./fetch-mapping.sh` in this skill folder (or use [reference.md](reference.md) directly: `GET /api/v2/projects`, then `GET /api/v2/tasks?project_id=...`) and **create or update** `reference/keito-time-mapping.md` with the IDs Matt confirms. Use [mapping.example.md](mapping.example.md) as the shape.

Client codes in standups (Gameday, KQED, Tanita, Halite, US, Fit3D, Prism, etc.) should each map to a `project_id` and default `task_id` (and optional alternate tasks).

**If a client code is missing from the mapping**, stop and tell Matt rather than guessing an ID. Two known gaps as of 2026-09-21: **Tanita and Halite are not assigned to Matt in Keito**, so they cannot be logged until an admin assigns him; and **Gameday moved from Harvest's SOW A to Keito's SOW C - Ongoing Work**.

## Workflow

### Phase 1: Propose (no Keito writes)

1. **Date**: Use system "today" unless Matt specifies a `spent_date` (ISO `YYYY-MM-DD`).
2. **Source of work**: Prefer Matt's explicit list in chat. If he points at standup, read `standups/YYYY-MM-DD.md` or `daily standup.txt` for that date and treat each bullet as a candidate line item.
3. **Calendar-informed hours (suggested)**: When building or refining a proposal for a given `spent_date`, **pull Matt's Google Calendar for that day** and use it to **suggest** hours per line. Use the **Google Calendar MCP** (see the **Google Calendar** guidance in `CLAUDE.md`: primary calendar id `matt@uptechstudio.com`, timezone America/Los_Angeles unless he says otherwise; prefer `search-events` with `timeMin` / `timeMax` for that local day if `list-events` fails). For each standup bullet, match likely events by **title**, **attendees**, or **obvious client keywords**. For each matched event, compute **duration** from start and end (e.g. 30 minutes → **0.5** hours) and note it as a **Suggested (calendar)** value. For **blocks without a clear client** (internal syncs, newsletter, happy hour, US), map to **Uptech / US** lines or list as **unallocated** so Matt can merge into one US row. **Suggestions are not final:** label them clearly so Matt can **edit, ignore, or replace** them. If Calendar is unavailable or a line has no match, use **"?"** and still **ask once** for missing hours (or one total to split) before posting.
4. **Hours**: If Matt did not give hours per line and calendar suggestions do not cover a row, **ask once** for hours (or one total to split) as part of building the proposal. **Never invent durations** for the final POST without Matt agreeing; calendar-derived numbers are **proposed** until he confirms (placeholders like "?" are OK in a draft only until he fills them in).
5. **Resolve IDs + billability**: Map the standup **code** to `project_id` via `reference/keito-time-mapping.md`. Choose **Product**, **Partner**, or **Non-billable** `task_id` using the judgment rules in that file (summary: **Product** for active dev and product delivery work; **Partner** for billable partner-style client work that is not really dev/PM delivery; **Non-billable** for setup, meetings, facilitation, unblocking others without core delivery). If a line mixes both, split into two rows or pick the dominant activity and note the assumption. For **US**, use the Operations / Miscellaneous row only (no Product/Partner/Non-billable split for now).
6. **Build the proposal**: Output a clear table (or numbered list) Matt can scan:
   - `spent_date`
   - Project (Keito name) and **`project_id`**
   - Task bucket (**Product** / **Partner** / **Non-billable**), Keito task name, and **`task_id`**
   - **Why** (one short phrase: billable vs non-billable reasoning)
   - **Suggested (calendar)** when available (duration from matched events for that day)
   - **Hours** (required before posting; do not POST with missing hours)
   - **Notes** (from standup bullet or chat)
6b. **Note formatting (required).** Matt wants time-entry notes as **bullet points, one sentence per line**. Each line starts with `• ` and lines are separated by a real newline (`\n` in the JSON body). No trailing periods needed.

```
• Operations and admin
• Call with Mark Wallin
• Weekly BD and marketing check-in
```

Never write notes as a single run-on sentence or a comma-separated list.

7. **Stop and confirm**: Ask Matt to **approve**, **edit** (change hours, project, task, merge/split lines), or **cancel**. **Do not call the Keito API until he explicitly approves** (e.g. "yes, post it", "looks good, log it", "go ahead").

### Phase 2: Create (only after approval)

8. **Timer mode**: Prefer **duration** (`hours` in JSON). If the API returns an error about timer mode, switch to `started_time` / `ended_time`, which Keito expects as **`HH:mm` 24-hour** (not Harvest's `9:00am`). See [reference.md](reference.md).
9. **Create entries**: `POST https://app.keito.ai/api/v2/time_entries` with a JSON body. Use curl from a shell with the env vars set.

Headers for every request:

```bash
-H "Authorization: Bearer ${KEITO_API_KEY}"
-H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
-H "Content-Type: application/json"
```

**Duration mode** body (typical):

```json
{
  "project_id": "cmtundnyc004p5gmkwykloccj",
  "task_id": "cmtundmo200bd5vfdnv3vn9yh",
  "spent_date": "2026-09-21",
  "hours": 1.5,
  "notes": "• Gameday sync\n• Call with Blaine",
  "source": "api"
}
```

**Quote the IDs.** Keito IDs are strings; an unquoted integer copied from an old Harvest snippet will fail. Set `"source":"api"` so these entries are filterable later with `?source=api`.

**Do not send `billable`.** Matt's account has `can_edit_time_billability: false`; billability follows from the task, which is what the Product / Partner / Non-billable choice already encodes.

**Round to quarter hours.** The account rounds up to 15 minutes (`time_rounding: up_15`), so a 20 minute call bills 0.5 either way. Propose 0.25 increments so the proposal matches what Keito stores.

Note the `\n` between bullets: Keito renders these as separate lines.

10. **After POST**: Give a short table: date, project, task, hours, notes. On failure, show status and API error body (redact secrets).

## Safety

- **Idempotency**: If Matt might run twice, ask whether to skip duplicate lines for the same day or always create new entries.
- **No secrets** in standup files or mapping file beyond IDs (tokens never go in git).
- **Never write to Harvest.** The Harvest account is a read-only historical archive during the transition, and the `HARVEST_*` env vars may still be set in Matt's shell. Ignore them.

## Related

- Same day's `standups/YYYY-MM-DD.md` (from the **log-standup** skill) is a good input list when Matt says "log yesterday's standup".
- `.claude/skills/standup-from-calendar-keito/SKILL.md` reads Keito (read only) to draft the standup. This skill is the only one that writes.
