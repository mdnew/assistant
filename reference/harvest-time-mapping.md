# Harvest time mapping

Standup **codes** (text before the colon) map to a **project_id** and a **task_id**. Matt’s work is always one of three buckets: **Product**, **Partner**, or **Non-billable** (Harvest label: **Non-billable Work** on client projects).

**Choosing the task (billability judgment):** Use best judgment from the standup line or chat. No single default.

| Lean toward… | Examples |
|--------------|----------|
| **Product** | Active development, hands-on building, product work scoped to the engagement (specs, backlog, delivery). |
| **Partner** | Billable partner-style client work that is not really “product” or “dev” (strategy, scoping, relationship-heavy work on the contract). If Harvest has no Partner task on that project (KQED), use **Product** and say so in the proposal. |
| **Non-billable** | Setup and plumbing, recurring coordination, **meetings** that are mostly facilitation or sync, unblocking others without doing the core delivery yourself, internal prep that is not client-facing delivery. |

When unsure, pick the conservative option and **say one short reason** in the proposal so Matt can correct it.

**Exception:** standup code **US** is internal Uptech time: for now everything goes to **US - Operations / Miscellaneous** (see below), not the three client buckets.

IDs were pulled from the Harvest API on **2026-04-10**. Re-fetch or edit if tasks change.

## Client projects (Product / Partner / Non-billable)

| code | harvest project | project_id | Product `task_id` | Partner `task_id` | Non-billable `task_id` |
|------|-----------------|------------|---------------------|---------------------|-------------------------|
| Gameday | SOW A - Ad Hoc Snowflake Support (Gameday Men's Health) | 47789977 | 17364879 | 16963897 | 15349582 |
| KQED | SOW F - Ongoing Development (KQED) | 46089857 | 15335712 | see note | 15349582 |
| KQED-general | KQED - General | 46383984 | 15335712 | see note | 15349582 |
| Tanita | SOW F - Q2 2026 (Tanita) | 47877672 | 17364879 | 16963897 | 15349582 |
| Tanita-Q1 | SOW E - Q1 2026 (Tanita) | 46860819 | 17364879 | 16963897 | 15349582 |
| Halite | SOW A - Initial Android App (Halite Medical) | 47912687 | 17364879 | 16963897 | 15349582 |
| Fit3D | SOW B - Ongoing Support (Fit3D, Inc.) | 42768154 | 17364879 | 16963897 | 15349582 |

**KQED note:** These KQED projects do not have a **Partner** task in Harvest (only Product, Non-billable Work, Development, etc.). For Partner-style work, either add a **Partner** task in Harvest and paste the new `task_id` here, or temporarily use **Product** `15335712` and note it in the time entry.

Harvest task names on client rows are like **Product - Contributor**; the table uses the short bucket name **Product**.

## Uptech internal (US in standups)

**For now:** standup code **US** always logs to **US - Operations** (Uptech Studio), project **`26747772`**, task **Miscellaneous** **`15557342`**. Use that for Product, Partner, and Non-billable internal time until this file changes.

Other tasks on that project (if you split later): Finance `15557351`, HR `15421156`.

## All active projects (reference)

Use this when adding new codes. For each new project, add a row to the client table with the three task IDs from Harvest.

| project_id | project name | client |
|------------|--------------|--------|
| 40901059 | SOW F - Ad-hoc | Specially Designed Education Services |
| 41890343 | Mobile Apps & Horizon/XTRA | Phillips Connect |
| 42768154 | SOW B - Ongoing Support | Fit3D, Inc. |
| 44955013 | Ongoing Dev Support | EVmatch |
| 45172097 | SOW B - Mobile App | FlipperForce |
| 45873329 | SOW D | Holistic Pet Hub |
| 46014637 | Ad-hoc Support | Digital Diagnostic Imaging |
| 46089857 | SOW F - Ongoing Development | KQED |
| 46129340 | School Transition Workbooks | Specially Designed Education Services |
| 46209839 | Design Support 2025 | UNest |
| 46383984 | KQED - General | KQED |
| 46471167 | Ad Hoc Support (Agreement 2) | Callbird |
| 46784423 | SUM Website | Startup Mavericks |
| 46796063 | Flutter Conversion | Holistic Pet Hub |
| 46860819 | SOW E - Q1 2026 | Tanita |
| 46862378 | Prism Labs - SOW T - Ongoing Support | Greyscale Holdings, Inc |
| 47789977 | SOW A - Ad Hoc Snowflake Support | Gameday Men's Health |
| 47828780 | Discovery | MintAgent |
| 47871242 | SOW B - 2026 Q2 | MintAgent |
| 47877672 | SOW F - Q2 2026 | Tanita |
| 47912687 | SOW A - Initial Android App | Halite Medical |
| 26332070 | US - Miscellaneous | Uptech Studio |
| 26332218 | US - Business Development | Uptech Studio |
| 26747772 | US - Operations | Uptech Studio |
| 27316511 | OrangeCal | Uptech Studio Software |
| 27897471 | AppFit | Uptech Studio Software |
| 28160691 | US - Reusable Work | Uptech Studio |
| 34297897 | US - Investing | Uptech Studio |

## Re-fetching from the API

From a shell with `HARVEST_ACCESS_TOKEN` and `HARVEST_ACCOUNT_ID` set:

```bash
curl -sS "https://api.harvestapp.com/v2/projects?is_active=true&per_page=2000" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: UptechAssistant (cursor-agent)"
```

Task assignments for one project:

```bash
curl -sS "https://api.harvestapp.com/v2/projects/PROJECT_ID/task_assignments?per_page=200" \
  -H "Authorization: Bearer ${HARVEST_ACCESS_TOKEN}" \
  -H "Harvest-Account-Id: ${HARVEST_ACCOUNT_ID}" \
  -H "User-Agent: UptechAssistant (cursor-agent)"
```

Full workflow detail: `~/.cursor/skills/log-harvest-time/reference.md`.
