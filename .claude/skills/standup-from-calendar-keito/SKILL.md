---
name: standup-from-calendar-keito
description: Draft or refresh daily standup.txt by merging Google Calendar events and Keito time entries for yesterday + today. Use when Matt says "create standup", "draft standup from calendar", "pull my calendar and time entries into standup", "populate standup from calendar", or the legacy "draft standup from calendar and Harvest" (Uptech moved off Harvest in Sept 2026), or similar. This is NOT the same as "log standup" (that archives to standups/ — use the log-standup skill).
---

# Standup from Calendar + Keito

> **Migrated from Harvest, Sept 2026.** Uptech tracks time in **Keito** (`keito.ai`). If Matt says "Harvest", he means Keito. Do not call the Harvest API. See `decisions/2026-09-21-move-time-tracking-from-harvest-to-keito.md`.

When Matt wants to **create or refresh** `daily standup.txt` using **Calendar and Keito**, do this in order.

## 1. Dates and timezone

- Use the **actual current calendar date** from system context as **today**.
- **Yesterday** and **today** are in **America/Los_Angeles** unless Matt says otherwise (match his primary Google Calendar timezone).
- Weekday labels in the file (e.g. `*Thursday*`) are **yesterday** and **today** by name.

## 2. Google Calendar (read)

- Use the **Google Calendar MCP**: `get-current-time` for timezone if needed, then load **yesterday 00:00 through end of today** (inclusive) on calendars he actually uses (at least primary `matt@uptechstudio.com`; include other selected calendars if useful). Follow the **Google Calendar** guidance in `CLAUDE.md` (primary calendar id `matt@uptechstudio.com`; prefer `search-events` or `get-freebusy` with the explicit id if `list-events` errors).
- Turn events into **short standup bullets**: title, and location or Meet link only if it helps. Omit private details he would not want in a team standup. Times are omitted by default.
- Map obvious work events to **client codes** when clear (Gameday, KQED, Tanita, Halite, Fit3D, US, etc.) using titles, attendees, or calendar name. If unclear, use a neutral bullet without forcing a code.

## 3. Keito (read only)

- **Do not post or log time** as part of this workflow unless Matt separately asks. This step is **read only** to suggest standup lines (to log time, use the log-keito-time skill).
- Require env vars `KEITO_API_KEY` and `KEITO_ACCOUNT_ID` (never print token values). Full API detail: `.claude/skills/log-keito-time/reference.md`.
- Keito returns entries for the whole team if the key is a full-access admin key. **Filter to Matt's entries**: use the `user_id` recorded in `reference/keito-time-mapping.md`, or fetch it from `GET /api/v2/users/me`, then pass `user_id=<id>`.
- Fetch time entries for **yesterday and today** (same local dates as Calendar):

```bash
curl -sS "https://app.keito.ai/api/v2/time_entries?user_id=USER_ID&from=YYYY-MM-DD&to=YYYY-MM-DD" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

- Use `from` / `to` as ISO dates for yesterday and today. Paginate with `page` / `per_page` if the response is truncated (`total_pages` / `links` in the response).
- For each entry, capture **project name**, **hours**, **task name**, and **notes** (if any). Turn into bullets (e.g. `Client: 1.5h Product, notes…`). Cross-check project names with `reference/keito-time-mapping.md` for standup codes when helpful.

If Keito env is missing or the API errors, say so briefly and still complete the standup from Calendar. If the Calendar MCP is unavailable, say so and complete it from Keito.

## 4. Write `daily standup.txt`

- Path: repo root `daily standup.txt` (space in filename).
- **Read the file first.** Preserve existing `*Goals*` and `*Blockers*` sections when present unless Matt asked to replace everything.
- Top line style: `_Mon Apr 10, 2026 - Standup_` (adjust date and weekday).
- Two day sections: `*YesterdayWeekday*` and `*TodayWeekday*` with bullets merged from Calendar + Keito. **De-duplicate** when the same work appears in both.
- Bullets use `•` and optional client prefix `Client:` like the existing file.
- **No em dashes** in standup text (use commas, colons, or separate sentences).

### Calendar merge is additive and anchored to the day the event happens

- **Never erase or overwrite existing bullets.** Only **add** new lines. Anything Matt already wrote stays exactly as it is.
- Place each calendar event as a bullet **under the day section for the date it actually occurs on** (yesterday's events under `*YesterdayWeekday*`, today's under `*TodayWeekday*`). Match the event's local date, not just "put everything under today."
- **Append** new bullets **below** the existing bullets in that day's section (add to the bottom, do not reorder or replace what's there).
- If a day section for the event's date does not exist yet, create it (keeping day order), then add the bullet under it.
- Before adding, skip events that already appear as a bullet in that day (de-duplicate) so repeated pulls do not stack duplicates.

## 5. Not the same as "log standup"

- **This skill:** draft or refresh standup **from** Calendar + Keito into `daily standup.txt`.
- **log standup / archive to `standups/`:** use the **log-standup** skill (copy to `standups/YYYY-MM-DD.md`). Only do that if Matt asks.
