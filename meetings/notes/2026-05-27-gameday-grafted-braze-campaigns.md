> **Source:** `gameday/meeting-notes/2026-05-27-gameday-grafted-braze-campaigns.md` (synced 2026-06-02)

# Gameday × Grafted — Braze campaigns & platform readiness

**Date:** 2026-05-27  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/b83289b3-4a34-4d77-b2d5-b5927f6ed8df)

## Participants

**Game Day:** Timothy Rempher (SSL), Blaine LaBron (SMS ops application), Russell Cloak (Gameday Central timeline—referenced)

**Grafted:** Campaign / lifecycle team (cross-sell, welcome series, dev comms)

**Referenced:** IT (SSL blockers), executive project priorities

## Summary

**SSL** is the gating item for live sends: Timothy targeting completion **by next Wednesday**, delayed by **IT and executive projects**. Required before **ad hoc campaigns**, **Father’s Day** (now pivoted), and broader launches.

**Gameday Central** needs **~8 weeks** for full **Braze event** support (canonical user/location IDs, events to **Snowflake** and **Braze**, live lifecycle publishing). **Contract ends July 23**—extends past current scope. Possible **stub events** for priority automations and **earlier canonical IDs** (~**4–5 weeks**); **manual CSV** imports until full automation.

**IP warming** requires **21 days** (Braze schedule: **50 users day 1 → 1M day 21**), **3 campaigns** to reach full base without duplicates, starting with **most engaged** segments. **Blocked without canonical user IDs** from Central (personalization/service-line conditionals). Partial alternative: **GHL engaged export** (90-day email engagement; **Royal Oak** smart lists)—still needs **user ID mapping** for dedupe.

**Campaigns:** Father’s Day → **summer promotion** (**June 1** launch target); **peptide of the month** performing. **Grafted** deliverables this week; **Blaine** finishing **SMS ops** application changes. Need **contract extension** discussion past **July 23**.

## SSL certificate & technical blockers

| Topic | Notes |
|--------|--------|
| **Owner** | **Timothy Rempher** — SSL cert implementation. |
| **Target** | Completion **by next Wednesday** (from meeting date—**verify** on calendar). |
| **Blockers** | **IT projects** and **executive project** priorities. |
| **Impact** | **No live campaigns** until SSL in place—blocks **ad hoc** sends and **Father’s Day** / seasonal promos. |

## Gameday Central backend timeline

| Topic | Notes |
|--------|--------|
| **Full Braze support** | **~8 weeks** for canonical **user IDs**, **locations**, **events** (Snowflake + Braze). |
| **Live events** | Lifecycle events—**appointments**, **contact updates**, etc. |
| **Contract** | Current term ends **July 23**—timeline **extends beyond** scoped engagement. |
| **Workaround** | **Stub events** for priority automations; **high-confidence canonical IDs** possibly **4–5 weeks** earlier. |
| **Interim** | **Manual CSV imports** before full automation. |

## IP warming requirements & constraints

| Topic | Notes |
|--------|--------|
| **Duration** | **21-day** IP warming for **million+** user sends. |
| **Schedule** | **Day 1: 50 users** → **Day 21: 1M users** (per Braze warming schedule). |
| **Segmentation** | Start with **most engaged** (internal contacts, recent clickers). |
| **Campaign structure** | **3 separate campaigns** to reach full base **without duplicates**. |
| **Dependency** | **Cannot proceed** without **canonical user IDs** from Gameday Central. |
| **Why** | Existing automations need **conditional personalization** / **service line** data—no viable workaround at current scope. |
| **Partial alternative** | **GHL** export of **90-day email-engaged** users; **Royal Oak** smart lists for recent clicks; still requires **user ID mapping** for future deduplication. |

## Campaign planning & next steps

| Topic | Notes |
|--------|--------|
| **Father’s Day pivot** | Shift to **summer promotion**; **June 1** launch target. |
| **Rationale** | Revenue during **summer downturn**; **peptide of the month** showing success. |
| **Grafted (this week)** | **Cross-sell/upsell copy** revisions by **Friday**; **welcome series** email design tests for review. |
| **Grafted (next week)** | Dev team building **remaining communications**. |
| **Blaine** | Complete **SMS operations application** changes for submission. |
| **Contract** | Timeline discussion for **extension beyond July 23**. |

## Action items

| Owner | Action |
|--------|--------|
| Timothy Rempher | Complete **SSL cert** by **next Wednesday**; unblock live campaigns. |
| Russell Cloak / platform | Deliver **Gameday Central** canonical IDs + events; evaluate **stub events** / **4–5 week** partial path. |
| Grafted | **Cross-sell/upsell copy** revisions by **Friday**; **welcome series** design tests for review. |
| Grafted dev | Build **remaining communications** **next week**. |
| Blaine LaBron | Finish **SMS ops application** changes and submit. |
| Leadership | Discuss **contract extension** past **July 23** vs 8-week Central timeline. |
| Campaign team | Execute **summer promotion** plan (**June 1** target) post-SSL. |
| Data | Plan **IP warming** segments + **3-campaign** structure once canonical IDs available; assess **GHL 90-day engaged** export + ID mapping interim. |

## Review checklist

- [ ] Confirm **SSL** completion date (Wednesday after 2026-05-27).  
- [ ] Reconcile **8-week Central** timeline with **July 23** contract end.  
- [ ] Document **stub event** scope for priority Braze automations.  
- [ ] Define **canonical user ID** readiness gate for IP warming start.  
- [ ] Confirm **June 1** summer promo still valid after Father’s Day pivot.  
- [ ] Verify **Royal Oak** / GHL smart list export process and dedupe mapping.  
- [ ] Track **SMS ops application** submission status (Blaine).
