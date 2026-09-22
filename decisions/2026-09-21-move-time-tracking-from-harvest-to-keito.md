# Decision: Move Uptech time tracking from Harvest to Keito

**Date**: 2026-09-21
**Status**: decided
**Made by**: Matt New

## Context

Uptech has tracked billable time in **Harvest** for years. Matt's whole timesheet workflow runs through this repo: the **log-harvest-time** skill proposed entries from standup with a Product / Partner / Non-billable billability judgment and posted them via Harvest API v2, and **standup-from-calendar-harvest** read Harvest back to help draft `daily standup.txt`. Project and task IDs lived in `reference/harvest-time-mapping.md`.

Matt moved to **Keito** (`keito.ai`), an AI-native time tracking product that bills human and agent work in one place. His Keito workspace was created **2026-09-11** and the repo tooling was cut over **2026-09-21**.

## Decision

**Uptech tracks time in Keito. Harvest becomes a read-only historical archive until the import is reconciled, then it is retired.**

## Rationale

*Matt's specific reason for the switch is not yet captured here. Ask him and fill this in.* What is recorded so far is the practical fit: Keito's API v2 is deliberately **Harvest-compatible** (`snake_case` fields, `spent_date`, `hours`, `notes`, `from` / `to` filters), and Keito ships a first-party Harvest importer, so the migration cost on our side was low.

## Alternatives Considered

| Option | Why Rejected |
|--------|-------------|
| Stay on Harvest | Matt decided to move; see Rationale |
| Run Harvest and Keito in parallel indefinitely | Double entry, and two systems disagreeing about billable hours is worse than either alone. Parallel running is time-boxed to reconciliation only |

## Tradeoffs Accepted

- **A reconciliation window where neither system is fully trusted.** Keito's own migration guide warns: "Do not treat a green completion message as the end of a business-data migration." Keep Harvest readable until the imported time, clients, projects and invoices are checked.
- **Retainers do not migrate.** Harvest's API does not expose retainer balances, project links, or draw history. Any retainer has to be recreated by hand in Keito under Invoices → Retainers.
- **Every project and task ID changed.** Keito issues opaque string CUIDs where Harvest used integers, so `reference/keito-time-mapping.md` was rebuilt from the API. The old integers are useless except as a crosswalk.
- **Tasks are now workspace-level**, shared across projects, rather than Harvest's per-project task assignments. Simpler, but a task is still only valid on a project it is assigned to.
- Team members are imported but **not automatically invited**, so the rest of Uptech needs a separate nudge.

## Migration state as of 2026-09-21

Verified directly against the Keito API:

- **Credentials work.** `KEITO_API_KEY` and `KEITO_ACCOUNT_ID` are in `~/.zshrc`; `GET /users/me` returns Matt (`cmtxaa0c203vq1365980oa41p`) at Uptech Studio.
- **Matt's key is member-scoped, not admin.** `GET /clients` returns 403 and `GET /projects` returns only the **13 projects assigned to him**. Fine for logging his own time; it means he cannot pull team-wide or client-level reports through the API.
- **`reference/keito-time-mapping.md` is fully populated** with real project and task IDs. The Product / Partner / Non-billable billability model survived intact.
- **Time history imported in full:** 658 entries covering 2025-10-01 to 2026-09-18, 1,773.3 hours, with the `billable` flag intact (391.3 billable). Wrapped engagements came across too, including Tanita and Halite, even though Matt is no longer assigned to those projects.
- **The KQED and Prism "no Partner task" gap persists.** Same workaround as Harvest: log Product and note it. Worth fixing properly in Keito.

Three things still need Matt's confirmation:

1. **Gameday changed project.** Harvest logged Gameday to *SOW A - Ad Hoc Snowflake Support*; the only Gameday project assigned to him in Keito is **SOW C - Ongoing Work**. Probably a genuine SOW rollover since the mapping was built in April 2026, but unconfirmed.
2. **Tanita and Halite are not assigned to him in Keito**, though their history imported. Both look genuinely wrapped (last standup mention June 2026). Only an issue if that work restarts.
3. **Billability is no longer overridable per entry** (`can_edit_time_billability: false`), and the account **rounds up to 15 minutes** (`time_rounding: up_15`). Both are account settings, not migration artifacts, but they change how proposals should be built.

## Expected Consequences

- `log-keito-time` and `standup-from-calendar-keito` replace the Harvest skills. Neither one calls Harvest again.
- The **Sep 9 action item** to run a billing report Oct 1 2025 to now before setting the KQED SOW number is **unblocked**: that full window imported into Keito. One catch, the API returns blank client names for a member-scoped key, so a report "filtered to partner clients" either groups by project name manually or gets run from the Keito web UI.
- The KQED "no Partner task" workaround (using Product and noting it) is worth fixing properly in Keito rather than carrying forward.
- Once the imported history is reconciled: revoke the Harvest personal access token, and remove `HARVEST_ACCESS_TOKEN` / `HARVEST_ACCOUNT_ID` from `~/.zshrc`. Both are still set as of 2026-09-21.

## Related

- `reference/keito-time-mapping.md` (real IDs, pulled 2026-09-21)
- `.claude/skills/log-keito-time/` (workflow, API reference, `fetch-mapping.sh`)
- `.claude/skills/standup-from-calendar-keito/`
- `decisions/2026-09-11-throttle-kqed-billable-work-until-october-sow.md` (the billability rules this migration must preserve)
- `meetings/actions/2026-09-09-uptech-bd-marketing.md` (the Oct 1 2025 to now billing report)
- [Keito migration guide](https://keito.ai/blog/migrate-from-harvest-to-keito/), [Keito API reference](https://keito.ai/docs/api-reference/overview)
