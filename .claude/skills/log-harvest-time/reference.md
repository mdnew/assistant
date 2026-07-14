# Harvest API v2 (reference)

Official docs: [Time entries](https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/), [Authentication](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/).

Base URL: `https://api.harvestapp.com`

## Current user (filter reads to Matt)

The token may be an admin token that returns the whole team's entries. To get just Matt's, fetch his user id and pass `user_id`:

```bash
curl -sS "https://api.harvestapp.com/v2/users/me" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
```

Then read his entries for a date range:

```bash
curl -sS "https://api.harvestapp.com/v2/time_entries?user_id=USER_ID&from=YYYY-MM-DD&to=YYYY-MM-DD" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
```

## List projects

```bash
curl -sS "https://api.harvestapp.com/v2/projects" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
```

Paginate with `?page=2` if needed. Each project has `id` and `name`.

## Task assignments for a project

Task assignments are per project. Use:

```bash
curl -sS "https://api.harvestapp.com/v2/projects/${PROJECT_ID}/task_assignments" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
```

Use the `task` object's `id` as `task_id`.

## Create time entry (duration)

Use when the Harvest account tracks by duration (`wants_timestamp_timers` false in Company API).

```bash
curl -sS -X POST "https://api.harvestapp.com/v2/time_entries" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}" \
  -H "Content-Type: application/json" \
  -d '{"project_id":PROJECT_ID,"task_id":TASK_ID,"spent_date":"YYYY-MM-DD","hours":1.0,"notes":"Optional"}'
```

Omit `hours` to start a running timer (0 hours); usually Matt wants explicit hours.

## Create time entry (start / end)

Use when the account uses timestamp timers (`wants_timestamp_timers` true).

```bash
curl -sS -X POST "https://api.harvestapp.com/v2/time_entries" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}" \
  -H "Content-Type: application/json" \
  -d '{"project_id":PROJECT_ID,"task_id":TASK_ID,"spent_date":"YYYY-MM-DD","started_time":"9:00am","ended_time":"10:30am","notes":"Optional"}'
```

## Company settings (timer mode)

```bash
curl -sS "https://api.harvestapp.com/v2/company" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: ${HARVEST_USER_AGENT:-UptechAssistant (claude-code)}"
```

Check `wants_timestamp_timers` in the response.
