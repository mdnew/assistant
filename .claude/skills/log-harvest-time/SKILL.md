---
name: log-harvest-time
description: >-
  Proposes Harvest time entries from standup or chat, confirms with Matt, then creates them via Harvest API v2.
  Use when Matt says "log time in Harvest", "log my Harvest time", "harvest time",
  or similar, or after standup when he wants timesheet entries logged.
  Never POST to Harvest until Matt explicitly approves the proposed list (or edited list).
---

# Log time in Harvest

## Prerequisites

Matt needs **Harvest API credentials** available in the environment when the agent runs shell commands:

| Variable | Source |
|----------|--------|
| `HARVEST_ACCESS_TOKEN` | [Harvest ID](https://id.getharvest.com) → Developers → Create personal access token |
| `HARVEST_ACCOUNT_ID` | Same page (Account ID), or Harvest → Settings |

Optional: `HARVEST_USER_AGENT` (default below). Harvest requires a `User-Agent` that identifies the integration.

If variables are missing, stop and tell Matt to add them (e.g. shell profile), then retry. Do not echo token values.

## Mapping file (required for reliable logging)

Harvest needs numeric **`project_id`** and **`task_id`** per entry.

1. **Look for** a mapping file, in order:
   - `reference/harvest-time-mapping.md` in the assistant repo
   - `.claude/skills/log-harvest-time/mapping.md`
2. If none exists or a client code is missing, use [reference.md](reference.md) to list projects (`GET /v2/projects`) and task assignments, then **create or update** `reference/harvest-time-mapping.md` in the assistant repo with the IDs Matt confirms. Use [mapping.example.md](mapping.example.md) as the shape.

Client codes in standups (Gameday, KQED, Tanita, Halite, US, Fit3D, etc.) should each map to a `project_id` and default `task_id` (and optional alternate tasks).

## Workflow

### Phase 1: Propose (no Harvest writes)

1. **Date**: Use system "today" unless Matt specifies a `spent_date` (ISO `YYYY-MM-DD`).
2. **Source of work**: Prefer Matt's explicit list in chat. If he points at standup, read `standups/YYYY-MM-DD.md` or `daily standup.txt` for that date and treat each bullet as a candidate line item.
3. **Calendar-informed hours (suggested)**: When building or refining a proposal for a given `spent_date`, **pull Matt's Google Calendar for that day** and use it to **suggest** hours per line. Use the **Google Calendar MCP** (see the **Google Calendar** guidance in `CLAUDE.md`: primary calendar id `matt@uptechstudio.com`, timezone America/Los_Angeles unless he says otherwise; prefer `search-events` with `timeMin` / `timeMax` for that local day if `list-events` fails). For each standup bullet, match likely events by **title**, **attendees**, or **obvious client keywords**. For each matched event, compute **duration** from start and end (e.g. 30 minutes → **0.5** hours) and note it as a **Suggested (calendar)** value. For **blocks without a clear client** (internal syncs, newsletter, happy hour, US), map to **Uptech / US** lines or list as **unallocated** so Matt can merge into one US row. **Suggestions are not final:** label them clearly so Matt can **edit, ignore, or replace** them. If Calendar is unavailable or a line has no match, use **"?"** and still **ask once** for missing hours (or one total to split) before posting.
4. **Hours**: If Matt did not give hours per line and calendar suggestions do not cover a row, **ask once** for hours (or one total to split) as part of building the proposal. **Never invent durations** for the final POST without Matt agreeing; calendar-derived numbers are **proposed** until he confirms (placeholders like "?" are OK in a draft only until he fills them in).
5. **Resolve IDs + billability**: Map the standup **code** to `project_id` via `reference/harvest-time-mapping.md`. Choose **Product**, **Partner**, or **Non-billable** `task_id` using the judgment rules in that file (summary: **Product** for active dev and product delivery work; **Partner** for billable partner-style client work that is not really dev/PM delivery; **Non-billable** for setup, meetings, facilitation, unblocking others without core delivery). If a line mixes both, split into two rows or pick the dominant activity and note the assumption. For **US**, use the Operations / Miscellaneous row only (no Product/Partner/Non-billable split for now).
6. **Build the proposal**: Output a clear table (or numbered list) Matt can scan:
   - `spent_date`
   - Project (Harvest name) and **`project_id`**
   - Task bucket (**Product** / **Partner** / **Non-billable**), Harvest task name, and **`task_id`**
   - **Why** (one short phrase: billable vs non-billable reasoning)
   - **Suggested (calendar)** when available (duration from matched events for that day)
   - **Hours** (required before posting; do not POST with missing hours)
   - **Notes** (from standup bullet or chat)
7. **Stop and confirm**: Ask Matt to **approve**, **edit** (change hours, project, task, merge/split lines), or **cancel**. **Do not call the Harvest API until he explicitly approves** (e.g. "yes, post it", "looks good, log it", "go ahead").

### Phase 2: Create (only after approval)

8. **Account timer mode**: Duration vs start/end is per Harvest company settings. Prefer **duration** (`hours` in JSON) unless Matt uses start/end; if API returns an error about timer mode, switch using [reference.md](reference.md).
9. **Create entries**: `POST https://api.harvestapp.com/v2/time_entries` with JSON body. Use curl from a shell with the env vars set.

Headers for every request:

```bash
-H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}"
-H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}"
-H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
-H "Content-Type: application/json"
```

**Duration mode** body (typical):

```json
{
  "project_id": 12345678,
  "task_id": 87654321,
  "spent_date": "2026-04-10",
  "hours": 1.5,
  "notes": "Gameday: call with Blaine"
}
```

10. **After POST**: Give a short table: date, project, task, hours, notes. On failure, show status and API error body (redact secrets).

## Safety

- **Idempotency**: If Matt might run twice, ask whether to skip duplicate lines for the same day or always create new entries.
- **No secrets** in standup files or mapping file beyond IDs (tokens never go in git).

## Related

- Same day's `standups/YYYY-MM-DD.md` (from the **log-standup** skill) is a good input list when Matt says "log yesterday's standup to Harvest".
