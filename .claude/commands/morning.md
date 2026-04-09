# Morning Briefing

Run the morning sync workflow:

1. Read `priorities/weekly-focus.md` for the current week's priorities
2. Check `meetings/actions/` for any pending action items (unchecked `- [ ]` items)
3. Check today's calendar using Google Calendar MCP tools (`GOOGLECALENDAR_EVENTS_LIST` with today's timeMin/timeMax in UTC)
4. Check HubSpot for deals needing attention today (pipeline **source of truth**):
   - Use `HUBSPOT_SEARCH_DEALS` filtered by close date (this week) or last activity (stale > 7 days)
   - Read **`deals/pipeline.md`** and per-deal notes in `business-development` for **notes and context** (facts still come from HubSpot)
5. Summarize in this format:

```
## Good morning. Here's your day.

**Today's focus** (from weekly priorities):
[1-2 sentence summary of what matters most today]

**Meetings today**:
[List from calendar — time, title, who]

**Pending action items**:
[Unchecked items from meetings/actions/, grouped by urgency]

**Deal check-in** (from HubSpot):
[Deals closing this week or with no activity in 7+ days]

**One thing to handle before noon**:
[Most important single task based on the above]
```

Keep it tight. No fluff. Everything should be actionable.
