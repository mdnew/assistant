# Deal Update

Update the status and context for this deal: $ARGUMENTS

## Instructions

1. **Fetch live deal data from HubSpot** using MCP tools:
   - Search for the deal by name: `HUBSPOT_SEARCH_DEALS` or `HUBSPOT_GET_DEAL`
   - Pull associated contacts and company: `HUBSPOT_GET_CONTACTS_FOR_DEAL`, `HUBSPOT_GET_COMPANY`
   - Pull recent activity/notes: `HUBSPOT_GET_ENGAGEMENTS_FOR_DEAL`

2. **Cross-reference with local context** in `deals/pipeline.md`, `deals/COMPANY-NAME.md` (if present), and `stakeholders/roster.md` for notes and nuance that live outside HubSpot

3. **Ask me what changed** if not provided in $ARGUMENTS:
   - What happened since last update?
   - What's the new stage (if it changed)?
   - What's the next action and by when?
   - Any blockers or risks?

4. **Update HubSpot** via MCP (this is the **source of truth** for deal pipeline data):
   - Update deal stage: `HUBSPOT_UPDATE_DEAL`
   - Log a note or activity: `HUBSPOT_CREATE_ENGAGEMENT`
   - Update next action / close date if changed

5. **Update local / git files**:
   - **`deals/pipeline.md`** — add or refresh **notes and context** for this deal (risks, story, next steps in prose). Any **stage or value** summary in the file must **match HubSpot** after step 4.
   - `deals/COMPANY-NAME.md` in `business-development` (if it exists) — append deeper strategic or relationship notes that do not belong in HubSpot
   - Key contacts: update `stakeholders/roster.md` if new info surfaced

6. **Create any action items** in `meetings/actions/YYYY-MM-DD-dealname.md` if next steps were identified

7. **Summarize** what was updated in HubSpot, what was filed locally, and what's next

Deal files preserve the full history. Never delete old entries; append new updates. **HubSpot owns stages, amounts, dates, and CRM activity.** **`deals/pipeline.md` owns notes, context, and the human-readable pipeline story** (git history). Factual fields in markdown should always follow HubSpot after an update.
