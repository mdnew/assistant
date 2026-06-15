> **Source:** `gameday/meeting-notes/2026-06-01-weekly-apps-platform-prioritization.md` (synced 2026-06-02)

# Gameday — Weekly Apps & Platform Prioritization

**Date:** 2026-06-01  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/bb355cbb-d24b-463e-95b5-d3000f149d49)

## Participants

**Referenced:** Anthony Castelli (AWS/Terraform), Russell Cloak (data integration / Braze), Nicole (Jira billing), Nate and Nic (separate Monday website/SEO meetings), Barry (attribute clarification), Outliant (legacy infra vendor)

## Summary

**Platform infrastructure:** Anthony is advancing **AWS/Terraform** despite problematic **Outliant** configuration—no real **dev environment** (production-only; prior “dev/staging” duplicated instances against the **same database**). Mitigation: **parallel stack** at **`api2.gamedaymenshealth.com`** to avoid breaking live services. Target **Terraform deploy by Wednesday**; full epic **next week** (RDS, lambdas, load balancers)—then **data ingestion** can start. Longer-term debt: proper **dev/staging** via new AWS sub-accounts and domain work (**140+ DNS records**).

**Data & Braze:** Russ owns **alignment and source validation** (**PLAT-126**, ~two weeks)—mapping sources/delivery, flagging questionable attributes (working with **Barry**). Lead flow clarified: **email → GHL → Gameday Central (webhook) → Braze re-engagement if no appointment → Lobby booking dedupes/updates**. **Event publishing** epic recreated as **PLAT-127** after accidental removal.

**Priorities / ops:** **Sentry** monitoring for API endpoints (**PLAT-123**); **Friday backlog grooming**; **Monday 2pm** website/SEO cadence with Nate and Nic (separate from this meeting); **Jira billing renewal** (Nicole has card); **revenue integration** deferred until **~70% Lobby adoption** issue is resolved.

## Platform infrastructure progress

| Topic | Notes |
|--------|--------|
| **Outliant legacy** | Problematic AWS setup; no true dev—**production-only** operations. |
| **Fake environments** | “Dev/staging” were **duplicate instances** pointing at the **same database**. |
| **Parallel build** | **`api2.gamedaymenshealth.com`** (verify hostname) to avoid breaking existing services. |
| **Anthony / Terraform** | Progress despite legacy constraints. |
| **Timeline** | **Terraform deployment by Wednesday**; full epic completion **next week**. |
| **Scope (epic)** | **RDS**, **lambdas**, **load balancers**; enable **data ingestion** post-deploy. |
| **Technical debt** | Real **dev/staging** later → new **AWS sub-accounts** + **domain restructuring**; **140+ DNS records** complicate migration. |

## Data integration & Braze setup

| Topic | Notes |
|--------|--------|
| **PLAT-126** | Russ: **alignment and source validation**—identify sources and delivery processes; questionable attributes under review with **Barry**; **~two-week** completion target. |
| **Lead capture flow** | 1) Visitor enters **email** on website → **Go High Level** first. 2) Webhook creates contact in **Gameday Central**. 3) No appointment → **Braze** re-engagement. 4) Later **Lobby** booking → **dedupe** and update existing contact. |
| **PLAT-127** | **Event publishing system** recreated after accidental removal. |

## Next steps & priorities

| Item | Direction |
|------|-----------|
| **PLAT-123** | **Sentry** monitoring for API endpoints. |
| **Backlog grooming** | **Fridays**—upcoming epics. |
| **Website / SEO** | Separate **Monday 2pm** meetings with **Nate** and **Nic** (prioritization track). |
| **Jira billing** | Renewal needed—**Nicole** has credit card access. |
| **Revenue integration** | **Postponed** until **70% Lobby adoption** blocker resolved. |

## Action items

| Owner | Action |
|--------|--------|
| Anthony Castelli | **Terraform deploy** by **Wednesday**; complete infra epic (**RDS**, lambdas, ALBs) **next week**. |
| Anthony Castelli / platform | Stand up **`api2`** parallel stack without disrupting production. |
| Russell Cloak | Complete **PLAT-126** (source validation, attribute cleanup with Barry) within **~two weeks**. |
| Russell Cloak / team | Execute **PLAT-127** (event publishing system). |
| TBD | Implement **PLAT-123** (**Sentry** on API endpoints). |
| Team | **Friday** backlog grooming for upcoming epics. |
| Nicole | **Jira billing** renewal. |
| Leadership / product | Revisit **revenue integration** after **Lobby adoption** (~70%) improves. |
| Platform (future) | Plan real **dev/staging** (sub-accounts, DNS/domain migration). |

## Review checklist

- [ ] Confirm **`api2.gamedaymenshealth.com`** hostname and cutover plan vs legacy API.  
- [ ] Link **PLAT-123**, **PLAT-126**, **PLAT-127** in Jira.  
- [ ] Verify **Barry** spelling/role (person vs vendor).  
- [ ] Document **70% Lobby adoption** metric source and target date for revenue integration.  
- [ ] Confirm **Wednesday** Terraform milestone against calendar.  
- [ ] Align **Friday grooming** time and attendees.
