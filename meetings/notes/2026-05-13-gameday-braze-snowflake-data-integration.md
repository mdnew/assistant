> **Source:** `gameday/meeting-notes/2026-05-13-braze-snowflake-data-integration.md` (synced 2026-06-02)

# Florencia Martinez Carranza and Matthew New — Braze, Snowflake, and data integration

**Date:** 2026-05-13  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Game Day:** Matthew New, Russell Cloak, Timothy Rempher, Blaine LaBron

**Ignite:** Florencia Martinez Carranza, Jefferson Soares, Jake Daniels, William Morales

**Invited (calendar):** Erwin Landaw (`erwin.landaw@ignitevisibility.com`)

## Summary

Discussion centered on **feeding Braze** with trustworthy customer data when **Go High Level (GHL)** and **Lobby** update on different cadences (**Lobby in-person** data **1–2× daily** per Jake, vs **telehealth webhooks** more “live”), and when **appointments views** lack a true **activity log** (limited cancellation timing / history).

**Keys / joins:** Prefer **Lobby patient UUID** as the **primary join spine** where available (first-hand vs GHL IDs); still need a path for **GHL-only** records. Linking **GHL `contact_id`** ↔ **Lobby patient id** likely needs **custom code** beyond out-of-the-box Segment wiring. Russell flagged the **missing global unique user id** across systems.

**MVP path:** Ship **minimal attributes** (e.g. name, email, phone) before chasing complex **UTM** enrichment; **audit** combined outputs from Lobby + GHL **before** turning on aggressive **daily backfill** jobs. Webhooks can create **orphaned/incomplete** fields—consider **enrichment on arrival** for metrics like completion counters.

**Comms architecture:** GHL automations use **~2–5 minute** delays for intake stability; longer-term **Braze**-centric comms may require **Lobby** to publish broader **webhooks** for full-funnel visibility. **Calendar fragmentation:** strategic push to **Lobby self-scheduling** vs continued **GHL calendar** use by users/vendors → sync failures between systems.

**dbt / Snowflake:** dbt (contractor **Kevin** per notes) runs joins/transforms in Snowflake—currently filtering for **initial appointments** to support **Google Ads** and **PostHog**, with room to expand. Russell wants clearer **production lineage** visibility for dbt-built tables.

**Access / governance:** **GitHub Enterprise** login still broken (**404** on links post–trial migration bug per Timothy). Snowflake permission review: **Irwin L.** tied to existing dashboards (**likely misspelling of Erwin Landaw—verify before any removal**); updates discussed for **Sarah E.** and **Lucas Dantis** (spelling per notes—**verify vs “Lucas Lima”** if same person). Unknown account **Andreas R.**—if owner not found, **deprecate access** (per discussion).

## Decisions and alignment

| Topic | Agreement / direction |
|--------|-------------------------|
| Braze spine | Prioritize **Lobby patient UUID** for joins when present. |
| MVP | Essential attributes first; **audit outputs** before **daily backfill**. |
| Webhooks | Expect gaps/orphans; plan **enrichment** and careful metrics definitions. |
| Segment | Still a integration path GHL + Lobby → Braze; custom join logic likely. |
| Snowflake hygiene | **Remove or deprecate** unrecognized/stale users after identification pass. |

## Action items

| Owner | Action |
|--------|--------|
| William Morales | Look up unknown Snowflake user **Andreas R.** once name/context lands in chat. |
| Blaine LaBron | At **end of week**, remove **`Irwin L.`** from Snowflake access list **per meeting**—**first confirm** this is not **Erwin Landaw**’s active login and that dashboards have a new owner if needed. |

## Risks / open questions

- **GHL-only leads** vs Braze `external_id` = Lobby patient id mapping semantics.  
- **Appointment status history** not in current views → downstream attribution and “canceled at” analytics incomplete.  
- **Calendar dual-use** (GHL vs Lobby) causing operational and data inconsistency.  
- **GitHub Enterprise** blocker continues to slow engineering access and audits.

## Detailed themes (from notes)

1. Braze historic import schema questions (Russell).  
2. Lobby refresh cadence vs same-day appointments; telehealth vs bulk paths.  
3. Location id vs patient id; Lobby UUID as preferred join key.  
4. Webhook completeness, enrichment, counters.  
5. Appointments table not an activity log; final statuses vs cancel tracking.  
6. GHL automation delay (2–5 min) vs Braze centralization; Lobby webhook coverage gap.  
7. Calendar strategy and vendor behavior.  
8. Segment + custom GHL↔Lobby link code.  
9. MVP attributes; UTM later; pre-backfill audit.  
10. dbt in Snowflake (Kevin); Ads/PostHog filters; expansion potential.  
11. dbt lineage transparency.  
12. GitHub Enterprise 404 bug post-trial.  
13. Snowflake ACL review; Irwin/Erwin; Sarah E.; Lucas Dantis; Andreas R.

## Review checklist

- [ ] Resolve **Irwin L.** vs **Erwin Landaw** in Snowflake and reconcile with Blaine’s removal task.  
- [ ] Confirm **Lucas Dantis** identity.  
- [ ] Document **Andreas R.** resolution (keep/remove) in access ticket.  
- [ ] File follow-up on **GitHub Enterprise** support ticket / workaround.  
- [ ] Capture agreed **MVP attribute list** and **audit criteria** in a ticket or doc.
