> **Source:** `gameday/meeting-notes/2026-05-13-trt-lead-funnel-questions.md` (synced 2026-06-02)

# Review TRT lead funnel questions

**Date:** 2026-05-13  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Game Day / Uptech:** Matthew New, Russell Cloak, Anthony Castelli, Blaine LaBron

## Summary

The meeting **reframed** the TRT funnel work from “rebuild flows inside **Go High Level (GHL)**” toward a **proprietary web application** (`app.gameday.com` per discussion) as the **system of record for identity and intake**, with a future **Game Day user ID** (patient spine) to reduce **fragmentation** between **GHL**, **Lobby**, and **Braze**.

**GHL’s role:** Shift toward **clinical / two-way communication** and local ops—not the **primary marketing lead-capture engine**. **Braze** owns **promotional automation**; corporate comms should still **surface in GHL** so clinic staff see **full interaction history**.

**Product strategy:** **Happy path first**—working web app to iterate; **standardized Game Day onboarding** over **per-franchise styling** that breaks flows; MVP anchored on **core TRT volume** (~95% of network per Blaine). Simpler booking (“**initial consultation**”) cited as **+38% conversion** vs overloaded booking types. **Early capture** of **email** (mint ID immediately) and **zip** to route clinics; future **virtual** routing and **treatment-line** segmentation (e.g. ED vs TRT) acknowledged as later.

**Data:** Phone as **legacy join**; forward path favors **accounts / logged-in state** (Supabase-class central DB discussed). **Deduping** improves revenue integrity; **historical perfection** explicitly deprioritized vs forward capture. Incentivized **login/claim** campaigns mentioned for **backfill**.

**Clinical-adjacent content:** **SHIM** (sexual health inventory) survey planned to inform clinics and upsell paths with clearer protocols.

**Process:** Treat as **app initiative** (design + PM resourcing); **Jira** backlog + **weekly grooming** with Blaine on a **separate prioritization board**; policy to **decline low-value franchise one-offs** that threaten integrity.

## Architecture direction (target state)

| Layer | Intended role |
|--------|----------------|
| Custom web backend | **Central hub** for patient/user record, routing, intake, events. |
| GHL | **Comms** + clinic-visible thread; not CRM-as-database for marketing capture. |
| Braze | Lifecycle/promotional automation fed from canonical events/attributes. |
| Lobby | Booking/scheduling handoff (widget consolidation discussed as ideal end state). |

## Product and GTM notes

- Replace **per-location GHL microsites** with **one centralized** lead experience for consistency and maintenance.  
- **Geo routing** (zip / geo data) and **virtual** paths for uncovered markets; Russell aligned on **query strings / short codes** for dynamic clinic context.  
- **A/B messaging** (e.g. “free body scan” vs other hooks) within a **tight funnel** for learning.  
- **Pilot:** **Tyler [surname]** at **Flat Iron** flagged as possible test partner (technical owner, high spend)—**verify spelling** (“Wnney” in notes).  
- **Prism body scan:** Anthony to **flag** possible **long-term removal** from the flow.

## Action items

| Owner | Action |
|--------|--------|
| Anthony Castelli | **Document** long-term option to **drop Prism body scan** from the lead flow. |
| Matthew New | **Rethink** prior technical comments with new architecture context; **sketch** application architecture. |
| Matthew New | **Jira:** enter requirements as **user stories**; create **separate backlog board** for **weekly prioritization** with **Blaine**. |
| Blaine LaBron | **Slack:** send **self-contained HTML prototype** file. |

## Detailed themes (from notes)

1. Fragmentation; need central ID.  
2. Growth-created mess; agreement on Game Day user ID.  
3. Supabase-class DB; logged-in future; phone for historical stitching.  
4. Simplified booking wins; mint ID on email capture.  
5. GHL as comms layer vs capture engine.  
6. Retire one-off GHL microsites per franchise.  
7. Geo + virtual routing; query/short-code deep links.  
8. Lead gen testing; early email + zip.  
9. Future treatment categorization; custom booking widget vision.  
10. Standardization vs franchise customization tension.  
11. Core TRT MVP vs edge cases.  
12. SHIM survey rationale.  
13. Deduping and revenue reporting expectations.  
14. Hub-and-spoke to GHL, Braze, Lobby.  
15. Braze vs GHL visibility for clinic staff.  
16. Resourcing: app squad, design, PM.  
17. Happy path delivery philosophy.  
18. Migration via campaigns / account claim.  
19. Governance: say no to low-value requests.  
20. Pilot clinic + Jira operating model.

## Review checklist

- [ ] Confirm **Tyler** last name and **Flat Iron** franchise naming in CRM.  
- [ ] Align this strategy doc with **May 12 TRT funnel** technical notes (API server, secrets, GHL pipelines).  
- [ ] Create **Jira** project/board links and add to this note when available.  
- [ ] Legal/compliance review for **SHIM** collection and consent copy.
