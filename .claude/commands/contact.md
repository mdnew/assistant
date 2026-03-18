# Add or Update Contact

Add or update a stakeholder in the roster: $ARGUMENTS

## Instructions

1. **Look up the contact in HubSpot** first:
   - Use `HUBSPOT_SEARCH_CONTACTS` by name or email
   - If found: pull their record, associated company, and deal history
   - If not found: create them with `HUBSPOT_CREATE_CONTACT`

2. **Gather any additional information** from $ARGUMENTS or ask me:
   - Name, title, company, email
   - How we met / relationship type (client, prospect, partner, investor, advisor)
   - What they care about / their priorities
   - Any relevant context that won't live in HubSpot

3. **Update HubSpot** if the contact exists but info is stale:
   - `HUBSPOT_UPDATE_CONTACT` for title, company, or other properties

4. **Update `stakeholders/roster.md`** with relationship context that belongs here (not in HubSpot):
   - If new: add a new entry in the appropriate section
   - If existing: append new context (never delete old entries)

5. **Create/update their one-on-one history file** at `stakeholders/one-on-ones/[name].md` if there's a meaningful relationship to track over time

6. **Confirm** what was added or changed in both HubSpot and local files

HubSpot owns contact/company data and activity history. Local files own relationship nuance, strategic context, and things you wouldn't want in a CRM.
