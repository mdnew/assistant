# Gameday internal — Lobbie integration, data hub, landing pages (post-Lobbie call)

**Date:** 2026-05-21 (follow-up after Lobbie sync; Gameday + Uptech only)

**Granola transcript:** https://notes.granola.ai/t/6af47aac-0ebd-4fb1-8186-19b951ff18dc

**Prior same day:** `meetings/notes/2026-05-21-gameday-lobbie-webhook-etl-sync.md`

## Lobbie integration progress

- Strong working session with **Russ** on payments and integration questions.
- Deep dive on **MX Merchant** connection data and ETL.
  - Incoming data is **recent** but **matching is inconsistent**.
  - **Lobbie** does matching in their ETL, which helps.
  - Without a stable **merchant ID** reference, **attribution** is hard.
- **Canonical Gameday user** expected to resolve many data problems.
  - **Gameday** as source of truth for **locations** (corporate vs franchise).
  - Each location mapped to **merchant ID**.
  - **Centralized locations** should fix current fragmentation.

## Data architecture and webhooks

- Direction: **fewer sources of truth**, simpler data story.
- **Gameday as central hub** for integrations.
  - **Lobbie webhooks → Gameday enriches →** fan-out to **Braze**, **data warehouse**, **Facebook ads**.
  - Replaces today’s pattern where messages move **between systems without Gameday in the middle**.
- **API vs webhook** (clarified on call):
  - **API:** proactive pulls (e.g. user logs in → fetch billing/profile).
  - **Webhooks:** passive events (e.g. appointment created → push notification).
- **Telehealth:** same **appointment webhook** with a **type** parameter.
  - No separate bespoke **Segment** path required.
  - Supports different **Braze** flows for telehealth vs in-clinic.

## Timeline and technical details

- **API endpoints** expected **tomorrow**; **webhooks** in roughly **1–2 weeks** (Gameday-side framing on this call).
- Webhooks are **critical for Braze** and **Jackson’s** requirements.
- **Single source of truth** for appointment creation unlocks proper **attribution**.
- **Gameday** will own **metrics/counters** centrally instead of relying on Lobbie alone.

## Landing page development

- Team using **Claude** successfully for landing page creation.
  - Current pattern: **Claude desktop** for basic pages.
- **Gift card** landing page ready to deploy on **Go High Level**.
  - **UTM parameter passing** still missing (must add before live).
  - Attribution tracking required for performance measurement.
- Need a **template system**: standard tracking codes and rules baked into **Claude prompts**.

## Web development and maintenance

- **Webflow** site hard to maintain after **Ignite** customizations.
  - Custom code blocks throughout; not visually editable.
  - Mixed templates and external components.
  - Simple updates require **developer** access.
- **Quiz funnel** with location logic needs **custom app** (not GHL).
  - Show only the franchisee’s clinics.
  - Dynamic questions from user attributes.
- **Future vision:** centralized **booking flows** + customizable landing pages.
  - Agencies build landers that funnel into **standard booking**.
  - **Attribution** preserved end to end.
  - One franchisee reportedly moved booking rate **40% → 80%** with a better flow.

## Next steps

| Owner | Item |
|-------|------|
| Nicole | Add **UTM tracking** to current landing page before go-live |
| Clay | Own **landing page** development going forward |
| Gameday / team | **Next week:** meeting to review overall **data flow** proposal |
| Russ, Anthony | Schedule **technical update** meeting next week |
| Uptech | **Weekend coverage:** team off **Friday PM through Tuesday AM**; flag any **Monday launch** needs **today/tomorrow** |
| Anthony | Out **3pm Eastern** tomorrow |

## Related notes

- Lobbie vendor call (same day): `meetings/notes/2026-05-21-gameday-lobbie-webhook-etl-sync.md`
- Architecture rollup: `context/gameday-architecture-attention.md`
- Follow-ups: `meetings/actions/2026-05-21-gameday-internal-follow-ups.md`
