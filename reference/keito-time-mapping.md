# Keito time mapping

Standup **codes** (text before the colon) map to a **project_id** and a **task_id**. Matt's work is always one of three buckets: **Product**, **Partner**, or **Non-billable** (Keito label: **Non-billable Work**).

IDs pulled from the Keito API on **2026-09-21**, after the Harvest import. Uptech moved off Harvest that day (see `decisions/2026-09-21-move-time-tracking-from-harvest-to-keito.md`). Re-fetch with `.claude/skills/log-keito-time/fetch-mapping.sh` if projects or tasks change.

**Matt's Keito `user_id`: `cmtxaa0c203vq1365980oa41p`.** Use it directly for `user_id=` on time-entry reads instead of calling `GET /v2/users/me` first.

## Things that changed from Harvest (read before using an old snippet)

- **IDs are opaque strings** (CUIDs like `cmtundo0r00595gmk2zlnem9u`), not integers. **Always quote them** in a JSON body.
- **Tasks are workspace-level and shared across projects.** One task id works on every project it is assigned to, so the task table below is a single shared list rather than per-project IDs. This is why several projects show the same `task_id`.
- **Matt's API key is member-scoped, not admin.** `GET /clients` returns 403, and `GET /projects` returns only **projects assigned to Matt** (13 of them). That is a permissions fact, not a missing import.
- **Client names come back empty on time entries** as a side effect of that 403. Entries carry `project.name` but a blank `client.name`, so any report "filtered to partner clients" has to group by project name and map to client by hand, or be run from the Keito web UI instead.
- **History imported in full:** 658 entries, 1,773.3 hrs, 2025-10-01 through 2026-09-18, including projects Matt is no longer assigned to. The `billable` flag came across correctly (391.3 billable hrs in that window).
- **Do not send `billable` on a time entry.** Matt's account has `can_edit_time_billability: false`; billability comes from the task. Pick the right task instead.
- **The account rounds time up to 15 minutes** (`time_rounding: up_15`). Hours land on the next 0.25, so a 20 minute call bills 0.5. Propose quarter-hour numbers.

## Choosing the task (billability judgment)

Use best judgment from the standup line or chat. No single default.

| Lean toward… | Examples |
|--------------|----------|
| **Product** | Active development, hands-on building, product work scoped to the engagement (specs, backlog, delivery). |
| **Partner** | Billable partner-style client work that is not really "product" or "dev" (strategy, scoping, relationship-heavy work on the contract). If the project has no Partner task (KQED, Prism), use **Product** and say so in the proposal. |
| **Non-billable** | Setup and plumbing, recurring coordination, **meetings** that are mostly facilitation or sync, unblocking others without doing the core delivery yourself, internal prep that is not client-facing delivery. |

When unsure, pick the conservative option and **say one short reason** in the proposal so Matt can correct it.

**KQED billability during the Sept 2026 budget throttle (see `decisions/2026-09-11-throttle-kqed-billable-work-until-october-sow.md`):** Matt is slowing his billable KQED volume until the October SOW, but this is **not** a blanket non-billable rule. **Delivery work stays billable** (analytics, activation stats, product work → KQED - General / **Product**). **Work on a different SOW stays billable** (App Sec → SOW G / Product). **Non-billable** covers SOW and contracting work, internal coordination, and syncs with Uptech staff. Ask Matt when a line is ambiguous.

**Exception:** standup code **US** is internal Uptech time: for now everything goes to **US - Operations / Miscellaneous** (see below), not the three client buckets.

## Client projects

| code | keito project | project_id | Product `task_id` | Partner `task_id` | Non-billable `task_id` |
|------|---------------|------------|-------------------|-------------------|------------------------|
| Gameday | SOW C - Ongoing Work (Gameday Men's Health) | `cmtundnyc004p5gmkwykloccj` | `cmtundmo200bd5vfdnv3vn9yh` | `cmtundmol00bj5vfddcy4vfib` | `cmtundmqr00c75vfdijy34xn0` |
| KQED **(default)** | KQED - General | `cmtundo0r00595gmk2zlnem9u` | `cmtundms400cl5vfdwa1stkxb` | none, see note | `cmtundmqr00c75vfdijy34xn0` |
| KQED-appsec | SOW G - Application Security (KQED) | `cmtundnz2004v5gmk2qsmdbpv` | `cmtundms400cl5vfdwa1stkxb` | none, see note | `cmtundmqr00c75vfdijy34xn0` |
| KQED-sowf | SOW F - Ongoing Development (KQED) | `cmtundo0z005b5gmkohmxm78o` | `cmtundms400cl5vfdwa1stkxb` | none, see note | `cmtundmqr00c75vfdijy34xn0` |
| Fit3D | SOW B - Ongoing Support (Fit3D, Inc.) | `cmtundo1w005j5gmkswheb6a2` | `cmtundmo200bd5vfdnv3vn9yh` | `cmtundmol00bj5vfddcy4vfib` | `cmtundmqr00c75vfdijy34xn0` |
| Prism | Prism Labs - SOW U - Ongoing Support (Greyscale Holdings, Inc) | `cmtundnyl004r5gmk0y0xy08w` | `cmtundmo200bd5vfdnv3vn9yh` | none, see note | `cmtundmqr00c75vfdijy34xn0` |

**Note the two different Product tasks.** KQED projects use **Product** `cmtundms400cl5vfdwa1stkxb`; Gameday, Fit3D and Prism use **Product - Contributor** `cmtundmo200bd5vfdnv3vn9yh`. This mirrors the old Harvest split (`15335712` vs `17364879`). Do not cross them.

**Gameday changed project (2026-09-21):** Harvest logged Gameday to *SOW A - Ad Hoc Snowflake Support* (28 hrs of history, imported). The only Gameday project assigned to Matt in Keito is **SOW C - Ongoing Work**, which has **no logged time yet**, consistent with a fresh SOW. Use SOW C. Worth a one-line confirmation from Matt the first time it comes up.

**No Partner task on KQED or Prism.** Still true after the migration. For Partner-style work on those, use **Product** and note it in the entry, or have an admin add a Partner task and paste the id here. The Keito move is a good moment to fix this properly rather than carry the workaround forward.

**Tanita and Halite are not assigned to Matt in Keito, because those engagements are done.** Neither appears in his 13 assigned projects, but **their history imported fine**: Tanita *SOW E - Q1 2026* (112.5 hrs) and *SOW F - Q2 2026* (7.5 hrs), Halite *SOW A - Initial Android App* (7.5 hrs). His last standup mention of either was June 2026. So this is a clean wrap, not a broken import. If work restarts, an admin has to assign him before he can log against them.

## Uptech internal (US in standups)

**For now:** standup code **US** always logs to **US - Operations**, project **`cmtundo3l005x5gmkpy7wjl40`**, task **Miscellaneous** **`cmtundmqe00c35vfdqz24zupc`**. Use that for all internal time until this file changes.

Other tasks on US - Operations: Non-billable Work `cmtundmqr00c75vfdijy34xn0`, Finance `cmtundmq700c15vfdyvvkvcio`, HR `cmtundmql00c55vfdt8611ckd`.

**Worth revisiting:** Keito gives Matt a **US - Business Development** project (`cmtundo3t005z5gmkkpxj7dhi`) with dedicated **Business Development** `cmtundmru00cj5vfdp9bdpbd1` and **Marketing** `cmtundmqx00c95vfdd29gwx5m` tasks. Given how much of his week is BD and the weekly BD/marketing check-in, splitting those out of Operations/Miscellaneous would make his internal time readable. Not doing it until Matt says so.

## Other projects assigned to Matt

| keito project | project_id | notable tasks |
|---------------|------------|---------------|
| US - Business Development | `cmtundo3t005z5gmkkpxj7dhi` | Business Development `cmtundmru00cj5vfdp9bdpbd1`, Marketing `cmtundmqx00c95vfdd29gwx5m`, Miscellaneous `cmtundmqe00c35vfdqz24zupc` |
| US - Investing | `cmtundo2l005p5gmkk68kxwah` | Research `cmtunajqi00305vfdpmz73j1t`, Non-billable Work, Miscellaneous |
| US - Miscellaneous | `cmtundo4100615gmkx18l2xi0` | HR, Miscellaneous, Professional Development `cmtundmq100bz5vfd400ofrs8`, Team Event `cmtundmn800b55vfdiew7wer8`, Travel `cmtundmne00b75vfdwl2t4a6l` |
| US - Reusable Work | `cmtundo2u005r5gmk5ns2dbe4` | Product, Development, Design, UX, Miscellaneous |
| US - Time Off | `cmtundnzk004z5gmkcca2070c` | Vacation `cmtundmm500at5vfdd6ewsrxp`, Holiday `cmtundmmc00av5vfdvfuwuqnp`, Sick Time `cmtundmly00ar5vfdo8zwo6z8`, Other Paid Time Off `cmtundmli00an5vfdqi2q3yew`, Unpaid Time Off `cmtundmlr00ap5vfdyjsw4fy0` |
| AppFit (Uptech Studio Software) | `cmtundo32005t5gmkgr1jiq23` | Product, Development, Design, UX, Marketing, Miscellaneous |

**US - Time Off is new** (no Harvest equivalent in the old mapping). Use it for PTO rather than an Operations row.

## Shared task IDs (workspace-level)

One id, reusable on any project it is assigned to.

| task | task_id | billable by default |
|------|---------|---------------------|
| Product | `cmtundms400cl5vfdwa1stkxb` | yes |
| Product - Contributor | `cmtundmo200bd5vfdnv3vn9yh` | yes |
| Partner | `cmtundmol00bj5vfddcy4vfib` | yes |
| Development | `cmtunajqi002x5vfd3sd6fbjf` | yes |
| Developer - Contributor | `cmtundmnw00bb5vfdikw2gfhz` | yes |
| Developer - Sr. Contributor | `cmtundmof00bh5vfdrglvy4iy` | yes |
| Developer - Lead | `cmtundmpu00bx5vfdb5487r6l` | yes |
| Design | `cmtunajqi002w5vfdatt9jriz` | yes |
| UX | `cmtundmrh00cf5vfdv2y45yq8` | yes |
| UX/Design - Contributor | `cmtundmo900bf5vfd91uif9y9` | yes |
| UX/Design - Sr. Contributor | `cmtundmnp00b95vfdvyqnv7ue` | yes |
| Research | `cmtunajqi00305vfdpmz73j1t` | yes |
| Non-billable Work | `cmtundmqr00c75vfdijy34xn0` | no |
| Miscellaneous | `cmtundmqe00c35vfdqz24zupc` | no |
| Business Development | `cmtundmru00cj5vfdp9bdpbd1` | no |
| Marketing | `cmtundmqx00c95vfdd29gwx5m` | no |
| Finance | `cmtundmq700c15vfdyvvkvcio` | no |
| HR | `cmtundmql00c55vfdt8611ckd` | no |
| Professional Development | `cmtundmq100bz5vfd400ofrs8` | no |
| Team Event | `cmtundmn800b55vfdiew7wer8` | no |
| Travel | `cmtundmne00b75vfdwl2t4a6l` | no |

A task only works on a project it is **assigned to**. The client table above already pairs valid combinations; if you need an unusual pairing, confirm with `GET /api/v2/tasks?project_id=...` first.

## Re-fetching from the API

```bash
.claude/skills/log-keito-time/fetch-mapping.sh
```

By hand, with `KEITO_API_KEY` and `KEITO_ACCOUNT_ID` set:

```bash
curl -sS "https://app.keito.ai/api/v2/projects?is_active=true&per_page=100" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"

curl -sS "https://app.keito.ai/api/v2/tasks?project_id=PROJECT_ID&is_active=true" \
  -H "Authorization: Bearer ${KEITO_API_KEY}" \
  -H "Keito-Account-Id: ${KEITO_ACCOUNT_ID}"
```

Full workflow detail: `.claude/skills/log-keito-time/reference.md`.
