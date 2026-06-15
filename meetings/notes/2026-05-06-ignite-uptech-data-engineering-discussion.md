# Ignite <> Uptech Studio: Discuss Data Engineering

> **Superseded:** Canonical notes are **`meetings/notes/2026-05-07-gameday-ignite-data-engineering.md`** (meeting date **2026-05-07**). Kept for earlier cross-references.

**Date:** 2026-05-06 (inferred from session context; confirm if different).

**Attendees (from invite / notes):** Florence Carranza (Ignite), Jake Daniels (Ignite), Erwin Landaw (Ignite), Jefferson Soares (Ignite), William Morales (Ignite), Timothy Rempher (Gameday), Sushma Bulusu (Gameday), Matthew New, Russell Cloak. (Original notes also list Jake Daniels twice in roles; Anthony Castelli was described as web-side in discussion.)

**Purpose:** Walk through Gameday data infrastructure as Ignite has built and operated it (warehouse, sources, joins, reporting), and align on handoff and open gaps (Braze, Lobby attribution, payments).

## Executive summary

- **Sources:** In-person clinic funnel is heavily **Go High Level (GHL)**; data is pulled via **AWS**, cleaned (including non-standard UTMs), and lands in Snowflake in a **GHL proxy S3** shape. **Lobby** supplies raw appointments and payments (and a separate telehealth-oriented set). **BigQuery** pulls GA4, GBP, and Search Console into Snowflake but that path was **paused during Kippy work** and remains an open migration or rebuild item.
- **Attribution:** Lobby flows **drop UTMs on redirect**, so GHL often has **no campaign attribution** for those bookings. That was called a major reporting and optimization blind spot; **Lobby** has been asked repeatedly; **fix timing unknown** (Allan / Christian side).
- **Identity and joins:** Primary join is **GHL `contact ID`** to **`go high level contact ID`** in Lobby raw data, then to **patient UUID** for appointments and payments. **MX Merchant** payments often **do not join** back (no stable key), so revenue can be missing next to appointments.
- **Latency:** Non-telehealth Lobby data is described as **FTP-driven** with roughly **1–2 day lag**; telehealth uses **webhooks** (more real time but lower volume). **Reverse ETL** (dbt, Segment) supports paid platform use cases; team wants **more real-time Lobby events** for Braze where possible.
- **Reporting:** **`dev consumption`** tables feed **Looker Studio** (campaign performance, spend, CAC, etc.). **Ownership** intended to move from Ignite toward **Blaine** (dashboard access handoff).

## Braze and implementation partner context

The team implementing Braze (notes name **Graphid**; elsewhere Gameday work references **Grafted**; reconcile naming with stakeholders) expects **user attributes** from warehouse paths (Lobby ETL into Snowflake, then toward Braze). Earlier concern remains: **source of truth** and **consistent IDs** across payments, appointments, and activities except where Ignite has defined joins (see below).

## Go High Level (GHL)

- Described as **CRM for in-person** clinics; central for **user attributes** feeding downstream use cases (including Braze needing phone numbers; **PII masking** and **unmasking permissions** noted).
- **Two main snapshots** in warehouse context: **`contacts created`** (first-touch style attribution) and **`contacts updated`** (current state; often used as “truth” for latest fields).
- **Tags and automations:** Tags reflect user events (for example booked appointment). **`Opportunities`** and **`automations`** called out as core GHL constructs for franchises; **many sub-accounts and vendor-specific pipelines** reduce standardization (~700 franchise admins, vendor-built stages).

## Lobby

- **Adoption:** Only **~32%** of clinics include a Lobby link (franchisee confusion and non-standard setup cited).
- **Attribution gap:** Lobby redirect flow **strips UTMs**; appointment still books but **GHL record lacks campaign attribution**; downstream reporting treats many flows as **organic / unknown**.
- **Product direction:** Ideas mentioned include **A/B test** for an intermediate page (contact vs self-schedule), and **care with “static calendar”** UX (preference for clear cues when leaving corporate site).

## Warehouse shape and joins (Ignite narrative)

| Concept | Detail |
|---------|--------|
| GHL → Snowflake | AWS pull, clean UTMs, **GHL proxy S3** in Snowflake; primary **attribute lake** for users |
| Lobby raw sets | **`lobby raw appointments`**, **`lobby raw payments`**; **`lobby`** set used for telehealth |
| Primary join | GHL **`contact ID`** ↔ Lobby **`go high level contact ID`** ↔ **patient UUID** for appointments / payments |
| Telehealth | **Webhook** events (for example appointment booked, payment successful), live-ish |
| Non-telehealth Lobby | **FTP** style updates, **1–2 day lag** |

**Payments gap:** Appointments reportedly flow through Lobby; **payments not always through Lobby**. Locations on **MX Merchant** lack an easy join to patient ID (effort underway in notes to get **user IDs** from MX for history).

## Forms and web touchpoints

- Some locations: **Webflow** forms capture UTMs and send inquiry **directly to GHL** (with local Webflow log; **Air Table** also mentioned).
- Other landing flows (for example **Google Maps**) may bypass Webflow but still hit GHL, increasing **source fragmentation**.

## Reverse ETL, dbt, Segment, ads

- **dbt** supports reverse ETL patterns; data moves from Snowflake through **Segment** to destinations including **Meta** and **Google** for **offline conversions** across ~**400 locations**; described as relatively hands-off operationally once built.

## BigQuery bridge

- **BigQuery** used to ingest **GA4**, **Google Business Profile**, **Search Console** into Snowflake for **franchise dashboard** style reporting.
- **Status:** Stuck or **paused** during Kippy period; may need **recreated pipeline** or similar recovery work.

## Looker Studio

- **`dev consumption`** tables are curated reporting views.
- Dashboards show **leads, appointments, patients, revenue vs spend**; quality **hurt by attribution loss** and **payment coverage** issues (MX Merchant).
- **Handoff:** Jake’s team to transfer **ownership and access** to **Blaine**.

## Data quality callouts

- **Appointment status:** Only **latest status** per row; **history** of status transitions not preserved.
- **Product catalog:** Concatenation / top-100 categorization to support reporting; **revenue still partial** when MX Merchant excluded.
- **Attribution coverage:** Rough **~60%** “coverage” estimate tied to users who use **website form** path that preserves UTMs into GHL (exact definition to confirm with Ignite).

## Governance and who to ping

- **Lobby product / roadmap:** **Allan** coordinates with **Christian** (Lobby owner); **Timothy** pointed team to Allan for **gaps in Lobby requests** and whether **attribution fix** is scheduled.
- **Programs (embeddables, tests, Florida):** **Nicole Marorrow** called out as strong context; **Blaine** newer to paid performance; both VPs Marketing with split focus (brand/tech vs performance).

## Communication

- Async **Slack** preferred vs email for technical follow-ups before a tight deadline window.
- **Matt** to stand up **Uptech ↔ Ignite** Slack channel and add **Jake**; add stakeholders to existing **Embeddables and Lobby** channel as needed (per Florence / Jake).

## Related files

- `meetings/actions/2026-05-06-gameday-data-engineering-ignite-handoff.md`
- `context/gameday-architecture-attention.md`
- Earlier identity sync: `meetings/notes/2026-05-06-grafted-gameday-lifecycle-sync.md` (if present)
- Web handover: `meetings/notes/2026-05-05-ignite-gameday-website-handover.md`
