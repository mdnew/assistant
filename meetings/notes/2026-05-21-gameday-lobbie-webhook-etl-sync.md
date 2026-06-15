> **Source:** `gameday/meeting-notes/2026-05-21-gameday-lobbie-webhooks-integration.md` (synced 2026-06-02)

# Gameday × Lobbie — webhooks & data integration

**Date:** 2026-05-21  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/25cb926b-8008-461b-b143-4b795a6951b7)

## Participants

**Game Day:** Russell Cloak (webhook consumer, event list recipient)

**Lobbie:** Engineering / integration (webhook API, ETL, payment consolidation)

**Referenced:** Kippy (legacy ETL requirements), corporate clinics (API credential scope)

## Summary

**Webhooks:** Basic **webhook registration via API** is in place; **appointment created** event testing nearly complete with **fast-follow** for remaining events. Lobbie sending **event list** to Russ.

**ETL vs webhooks:** Current **S3 nightly ETL** (legacy **Kippy** shape) won’t align with **webhook/REST** payloads; standard pattern is **enrich webhook events via REST API**. **Native IDs** may be missing from ETL today—Lobbie can **add native IDs to dumps** (code release) to enable **historical backfill** matching future webhooks. Post-webhook, ETL shifts to **reconciliation** (missed webhooks, location onboarding, **MX→Lobbie** payment migration).

**Payments:** Fragmented **MX Merchant** (UI over **Priority Gateway**) vs **Lobbie**; goal is **all payment data in Lobbie**, drop MX dependency, Lobbie as payment SoT with **Priority** still processing. **Telehealth** moving from **Segment-only** to webhooks; **appointment types** distinguish telehealth vs in-clinic; **UTM endpoints** planned for attribution.

**Next:** Lobbie provides **API credentials** for **3 corporate clinics**; release target **tonight or Monday** with **appointment webhooks**; **payment endpoints** after next release; **appointment created** as implementation starting point.

## Webhook implementation progress

| Topic | Notes |
|--------|--------|
| **Infrastructure** | Basic **webhook registration via API** complete. |
| **In flight** | Testing **appointment created** event—wrapping up soon. |
| **Roadmap** | **Fast follow** for remaining events. |
| **Documentation** | **Event list** being sent to **Russ** for reference. |

## Data integration & ETL discussion

| Topic | Notes |
|--------|--------|
| **ETL mismatch** | **S3 nightly drops** won’t match webhook payloads—ETL built for **legacy/Kippy** requirements. |
| **Webhook model** | **Discrete** structure via webhook/REST vs bulk ETL files. |
| **Enrichment pattern** | Standard: **enrich webhook events** with follow-up **REST API** calls. |
| **Native IDs** | Current ETL may lack IDs needed for API enrichment. |
| **Lobbie fix** | Can add **native IDs to ETL dumps** (requires **code release**). |
| **Backfill** | Enables **historical backfill** aligned with future webhook stream. |
| **ETL future role** | Primarily **reconciliation** after webhooks live: missed/failed webhooks; **location onboarding** reconciliation; **payment reconciliation** during **MX → Lobbie** migration. |

## Payment system consolidation

| Topic | Notes |
|--------|--------|
| **Current state** | Split between **MX Merchant** and **Lobbie**. |
| **MX** | UI layer over **Priority Gateway**; many franchises prefer MX workflow. |
| **Target state** | **All payment data in Lobbie**; **eliminate MX Merchant dependency**. |
| **SoT** | **Lobbie** single source of truth for payments. |
| **Processor** | **Priority Gateway** remains underlying processor. |
| **Telehealth** | Today **Segment-only**; moving to **webhook system**. |
| **Appointment metadata** | Types indicate **telehealth vs in-clinic**. |
| **Attribution** | **UTM tracking endpoints** planned. |

## Action items

| Owner | Action |
|--------|--------|
| Lobbie | Provide **API credentials** (**client ID**, tokens) for **3 corporate clinics**. |
| Lobbie | Ship release **tonight or Monday** including **appointment webhooks**. |
| Lobbie | Deliver **payment endpoints** after **next release**. |
| Lobbie | Send **event list** to **Russ**. |
| Lobbie | Plan **native ID** fields in ETL dumps (code release). |
| Russ / Game Day | Implement consumer starting with **appointment created** webhook; design enrichment + reconciliation paths. |
| Game Day | Plan ETL role transition to **reconciliation-only** post-webhook. |

## Review checklist

- [ ] Confirm release landed (**tonight vs Monday** after 2026-05-21).  
- [ ] Verify **3 corporate clinic** credential delivery and environments.  
- [ ] Match Lobbie **event list** to Gameday Central ingestion design.  
- [ ] Track **payment endpoint** release vs MX→Lobbie migration timeline.  
- [ ] Confirm **native ID** ETL release date for backfill.  
- [ ] Document **UTM endpoint** spec when available.  
- [ ] Align telehealth **appointment type** values with Braze/Segment cutover.

## Related

- Prior: `meetings/notes/2026-05-07-gameday-lobbie-webhooks-infrastructure.md`
- Internal follow-up: `meetings/notes/2026-05-21-gameday-internal-data-architecture-landing-pages.md`
- Actions: `meetings/actions/2026-05-21-gameday-lobbie-webhook-follow-ups.md`
- Architecture rollup: `context/gameday-architecture-attention.md`
