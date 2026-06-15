> **Source:** `gameday/meeting-notes/2026-05-07-data-engineering-ignite-uptech.md` (synced 2026-06-02)

# Ignite <> Uptech Studio: Data engineering

**Date:** 2026-05-07  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)

## Participants

**Game Day / Uptech:** Matthew New, Russell Cloak, Sushma Bulusu (data analyst), Timothy Rempher

**Ignite:** Florencia Martinez Carranza, Jake Daniels, Erwin Landaw, Jefferson Soares, William Morales

**Referenced:** Anthony Castelli (web), Allan (Lobby / vendor relationship), Christian (Lobby owner), Blaine, Nicole Marorrow (programs / branding-tech context per notes—**verify spelling**), Graphid (Braze-related implementation group per notes—**verify name**)

## Summary

The group walked through **Snowflake-centric** reporting and activation: **Go High Level (GHL)** as the CRM/lake path for in-person clinics, **Lobby** for scheduling/payments (with known **attribution loss** on redirects), **telehealth** as a smaller, more webhook-mature slice, and **reverse ETL** (dbt, Segment) for ads/offline conversions. **Braze** readiness is blocked in part by **unclear cross-system identifiers** and messy franchise operations. **BigQuery → Snowflake** pipelines for GA4, GBP, and Search Console were called out as **paused** during the Kippy transition and need revival for franchise dashboards.

Coordination will move to **Slack** (new Uptech–Ignite channel plus updates to existing Embeddables/Lobby channels).

## Data landscape (high level)

| Area | Role in notes |
|------|----------------|
| GHL | CRM for in-person; data pulled via AWS, cleaned (UTMs non-standard), landed in **GHL proxy S3 → Snowflake**. Key sets: **`contacts created`** (first-touch attribution) vs **`contacts updated`** (current state). |
| Webflow / Airtable | Some locations: forms capture UTMs → **GHL**; local Webflow log; some data in **Airtable**. |
| Lobby | Scheduling; **~32%** clinic adoption per Florencia; **UTMs dropped** through lobby redirect → GHL user often has **no campaign attribution** though appointment books. |
| Join keys | **`contact_id` (GHL)** ↔ **`go_high_level_contact_id`** in Lobby raw → derive **`patient_id`** (UUID) for appointments/payments joins. |
| Lobby datasets | **`lobby_raw_appointments`**, **`lobby_raw_payments`**; **`lobby`** dataset used for **telehealth** (per Jake). |
| Payments gap | Not all locations use Lobby for payments; **MX Merchant** lacks a reliable join key to patient/appointment → revenue gaps in reporting. |
| Telehealth | **`lobby`** / “lobby regular” in notes: **webhooks** (`appointment booked`, `payment successful`)—live; low volume vs in-person. |
| Bulk Lobby data | **FTP-style feed**: **1–2 day lag**; drives need for **webhooks** for timelier Braze triggers. |
| Activation | **dbt** + **reverse ETL** (Snowflake → **Segment** → Meta/Google offline conversions, ~400 locations). |
| Marketing analytics | **BigQuery** pulls **GA4**, **Google Business Profile**, **Search Console** into Snowflake—**stuck/paused** during Kippy work; franchise dashboard depends on this. |
| Dashboards | **Dev consumption** tables (per discussion) → **Looker Studio** (campaign performance, spend, CAC); ownership moving toward **Blaine**. |

## Known issues and risks

- **Attribution:** Lobby flow drops UTMs → appointments may appear **organic/non-attributed**; Russell described as unacceptable; **Lobby not prioritizing** fix per Florencia despite repeated asks.
- **Coverage:** Jake estimated **~60%** attribution coverage tied to **website form** path vs full journey.
- **Franchise variability:** Many lead sources (Maps, etc.) still land in GHL; **700+** sub-account admins and **vendor-specific** pipelines/automations → inconsistent stages/tags.
- **Appointment history:** Status reflects **latest state only** (no full state transition history in one-row model).
- **Product/revenue reporting:** Catalog concatenation / top-100 categorization; still **subset** of revenue when MX Merchant excluded.

## Communication

- **New Slack channel:** Uptech ↔ Ignite for async technical Q&A (Matthew to create; Jake invited first).
- **Existing channels:** Add relevant people to **Embeddables** and **Lobby** Slack channels where still active.

## Action items

| Owner | Action |
|--------|--------|
| Jake Daniels | Send **data join diagram** (GHL `contact_id` → Lobby `go_high_level_contact_id` → `patient_id`); ensure **Russell** receives the **handoff document**. |
| Russell Cloak | **Contact Allan** re Lobby gaps; confirm whether **attribution tracking** fix is planned/prioritized. |
| Jake Daniels | Transfer **Looker Studio** dashboard **ownership/access** to **Blaine**. |
| Matthew New | Create **Slack** channel for **Uptech** and **Ignite** communication. |
| Matthew New | **Invite Jake** to the new channel. |
| Matthew New | Add necessary members to existing **Embeddables** and **Lobby** Slack channels. |

## Detailed themes (from notes)

1. **Intros:** Russell leads data; Anthony web; Sushma new analyst; Braze migration context.
2. **Braze / Graphid:** Needs user attributes from Lobby ETL → Snowflake → Braze; **no clear universal IDs** across payments/activities/appointments without pragmatic joins/shortcuts.
3. **Business ops:** Telehealth (smaller, vendor-specific) vs primary **Lobby + in-person** clinics.
4. **GHL deep dive:** Tags, opportunities, automations; PII/phone masking for Braze; vendor-built automations vs small in-house capacity.
5. **Lobby adoption and UX:** Low link usage; support tickets on latency; proposed **A/B** intermediate page; caution on static calendar UX.
6. **Allan / Christian:** Allan owns relationship with Lobby leadership and roadmap (per Timothy).
7. **Join logic and MX Merchant:** Payments not always in Lobby → join gaps.
8. **FTP lag vs webhooks:** Reverse ETL for scale; desire for webhook coverage for key Lobby events for Braze timeliness.
9. **dbt + Segment:** Offline conversions at scale.
10. **BQ migration debt:** Recreate or unstick GA4/GBP/GSC → Snowflake.
11. **Looker:** Consumption-layer tables; Blaine ownership transfer.
12. **GHL complexity:** Ad vendors creating stages; standard sales pipeline often overridden.
13. **Telehealth list drift:** Florida-wide participation changed without corporate notification—no authoritative current list in notes.
14. **Program ownership:** Nicole (and Blaine) VP Marketing split—Nicole branding/tech, Blaine performance (per Jake); **verify** org chart/titles.

## Review checklist

These bullets are **summarized from meeting notes**, not a verbatim transcript.

- [ ] Confirm **“Graphid”** (Braze implementer) spelling/name.
- [ ] Confirm **Nicole Marorrow** spelling and current role.
- [ ] Replace any remaining **“Optek”** references in calendars/docs with **Uptech** if that was a transcription error.
- [ ] Validate table/column names (`lobby_raw_*`, dev consumption layer, etc.) against Snowflake.
- [ ] Confirm Slack channel names and who was actually added.
