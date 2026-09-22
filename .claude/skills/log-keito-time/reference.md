# Keito API v2 (reference)

Official docs: [API overview](https://keito.ai/docs/api-reference/overview), [Time entries](https://keito.ai/docs/api-reference/time-entries), [Projects](https://keito.ai/docs/api-reference/projects), [Users](https://keito.ai/docs/api-reference/users), [API keys](https://keito.ai/docs/auth/api-keys).

Base URL: `https://app.keito.ai/api/v2`

## Migrated from Harvest (Sept 2026)

Keito API v2 is **Harvest-compatible by design**: `snake_case` fields, `spent_date`, `hours`, `notes`, `from` / `to` date filters. The call shapes below are near-identical to the old Harvest ones. Three things changed:

| | Harvest (old) | Keito (new) |
|---|---|---|
| Base URL | `https://api.harvestapp.com` | `https://app.keito.ai/api/v2` |
| Account header | `Harvest-Account-Id` | `Keito-Account-Id` |
| Env vars | `HARVEST_ACCESS_TOKEN` / `HARVEST_ACCOUNT_ID` | `KEITO_API_KEY` / `KEITO_ACCOUNT_ID` |
| ID type | integers (`46383984`) | **opaque strings** (CUIDs, e.g. `cmtundo0r00595gmk2zlnem9u`) |
| `User-Agent` | required | not required |
| Task list | `/projects/{id}/task_assignments` (per project) | `/tasks?project_id={id}` (**workspace-level, shared across projects**) |

**IDs are strings now.** Always quote them in JSON bodies (`"project_id": "cmtundo0r00595gmk2zlnem9u"`, never bare). This is the single most likely thing to break when adapting an old Harvest snippet.

**Verified against Matt's account 2026-09-21:**

- His key is **member-scoped, not admin**. `GET /clients` returns 403, and `GET /projects` returns only the **13 projects assigned to him**. Reads are already scoped to him, so `user_id` is optional on time-entry reads.
- **Do not send `billable`.** `can_edit_time_billability` is false on his account; billability follows the task. Pick the right task instead.
- The account uses **`time_rounding: up_15`**, so hours round up to the next 0.25. Propose quarter-hour numbers.
- Tasks are **shared across projects**: one task id (e.g. Non-billable Work `cmtundmqr00c75vfdijy34xn0`) is valid on every project it is assigned to. A task still only works on a project it is assigned to, so check `GET /tasks?project_id=...` for unusual pairings.

## Credentials

Get both from the Keito web app under **Settings → API & Developers**:

- `KEITO_API_KEY` — a `kto_...` key. Needs to be a **full-access integration key**; the personal read-only sync key cannot write time entries or read `/tasks`.
- `KEITO_ACCOUNT_ID` — the **Company ID** shown on the same page.

The key is shown **once** at creation. Never echo either value.

Headers for every request:

```bash
-H "Authorization: Bearer ${KEITO_API_KEY}"
-H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
-H "Content-Type: application/json"
```

## Current user (filter reads to Matt)

A full-access key may return the whole team's entries. To get just Matt's, fetch his user id and pass `user_id`:

```bash
curl -sS "https://app.keito.ai/api/v2/users/me" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

Then read his entries for a date range:

```bash
curl -sS "https://app.keito.ai/api/v2/time_entries?user_id=USER_ID&from=YYYY-MM-DD&to=YYYY-MM-DD" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

Matt's Keito `user_id` is **`cmtxaa0c203vq1365980oa41p`** (also in `reference/keito-time-mapping.md`), so this call can usually be skipped. His key only returns his own entries anyway.

## List projects

```bash
curl -sS "https://app.keito.ai/api/v2/projects?is_active=true&per_page=100" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

Paginate with `page` / `per_page`. Responses carry `page`, `per_page`, `total_pages`, `total_entries`, `links`.

## Tasks for a project

Tasks are workspace-level in Keito and scoped to a project by query param (this differs from Harvest's per-project `task_assignments`):

```bash
curl -sS "https://app.keito.ai/api/v2/tasks?project_id=${PROJECT_ID}&is_active=true" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

Use the task's `id` as `task_id`.

## Create time entry (duration)

```bash
curl -sS -X POST "https://app.keito.ai/api/v2/time_entries" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}" \
  -H "Content-Type: application/json" \
  -d '{"project_id":"PROJECT_ID","task_id":"TASK_ID","spent_date":"YYYY-MM-DD","hours":1.0,"notes":"Optional","source":"api"}'
```

Body fields: `project_id` (string, required), `task_id` (string, required), `spent_date` (`YYYY-MM-DD`, required), `hours` (number), `notes` (string), `source` (string), `metadata` (object), `is_running`, `replace_running`, `started_time`, `ended_time`. The API also documents `billable`, but **Matt's account cannot set it** (see above), so leave it off.

Set `"source":"api"` on entries this skill creates so Matt can filter them later with `?source=api`.

## Create time entry (start / end)

If the workspace uses timestamp timers rather than durations:

```bash
curl -sS -X POST "https://app.keito.ai/api/v2/time_entries" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}" \
  -H "Content-Type: application/json" \
  -d '{"project_id":"PROJECT_ID","task_id":"TASK_ID","spent_date":"YYYY-MM-DD","started_time":"09:00","ended_time":"10:30","notes":"Optional","source":"api"}'
```

Note `started_time` / `ended_time` are **`HH:mm` 24-hour** in Keito, not Harvest's `9:00am` format.

## Filtering time entries

`GET /api/v2/time_entries` accepts `page`, `per_page`, `source`, `project_id`, `task_id`, `user_id`, `client_id`, `from`, `to`, `is_billed`, `is_running`, `updated_since`.

Useful for the reporting Matt does at SOW time, for example all partner-client billing since a date:

```bash
curl -sS "https://app.keito.ai/api/v2/time_entries?from=2025-10-01&to=2026-09-21&per_page=100" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

## Optional: Keito CLI

Keito ships a CLI that wraps the same API. Not required for this skill, but handy for ad hoc checks:

```bash
brew install osodevops/tap/keito
keito auth login
keito projects list --json
keito time log --project "NAME" --task TASK --duration H:MM --notes TEXT
```

Every command supports `--json`. Env vars `KEITO_API_KEY` / `KEITO_ACCOUNT_ID` take precedence over its config file.
