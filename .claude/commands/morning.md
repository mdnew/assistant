# Morning Briefing

Run the morning sync workflow:

1. **Sync Granola first** — run the **granola-sync** skill to pull any new meeting notes into `meetings/notes/` and `meetings/actions/`, so the action-item scan below includes yesterday's meetings. If nothing is new, say so in one line and move on
2. Check `meetings/actions/` for any pending action items (unchecked `- [ ]` items)
3. Check today's calendar using Google Calendar MCP tools (`GOOGLECALENDAR_EVENTS_LIST` with today's timeMin/timeMax in UTC)
4. Check HubSpot for deals needing attention today (pipeline **source of truth**):
   - Use `HUBSPOT_SEARCH_DEALS` filtered by close date (this week) or last activity (stale > 7 days)
   - Read **`deals/pipeline.md`** and any per-deal notes in `deals/` for **notes and context** (facts still come from HubSpot)
5. Summarize in this format:

```
## Good morning. Here's your day.

**Today's focus** (from `to-do.txt` portfolio priority + this week's standup goals):
[1-2 sentence summary of what matters most today]

**Meetings today**:
[List from calendar — time, title, who]

**Since yesterday** (from Granola):
[New meetings synced, one line each. "Nothing new" if none.]

**Pending action items**:
[Unchecked items from meetings/actions/, grouped by urgency]

**Deal check-in** (from HubSpot):
[Deals closing this week or with no activity in 7+ days]

**One thing to handle before noon**:
[Most important single task based on the above]
```

Keep it tight. No fluff. Everything should be actionable.
