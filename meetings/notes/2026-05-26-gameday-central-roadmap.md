> **Source:** `gameday/meeting-notes/2026-05-26-gameday-central-roadmap.md` (synced 2026-06-02)

# Gameday Central — roadmap meeting

**Date:** 2026-05-26  
**Format:** Meeting / transcript summary (review against recording if discrepancies matter)  
**Transcript:** [Granola notes](https://notes.granola.ai/t/354b4a8f-a352-4050-85d9-2e1c380306d7)

## Participants

**Referenced:** Russell Cloak, Anthony Castelli (Central development focus), Jordan, Adam (Webflow tasks), Blaine (GHL landing pages with Clay), Sarah (UX research with Adam), Steve and franchisees (interviews), Christian at Lobby (MX mapping—Thursday), Nicole (process—implied)

## Summary

The group reviewed a **Gameday Central** proposal: a **centralized hub** to ingest, organize, and emit Game Day data—addressing fragmented identity across **Lobby**, **GHL**, **MX**, **Segment**, **Snowflake**, **Nexus**, and **PostHog**. **Snowflake** exists but is **not** the operational SoT (weak identity resolution, data quality). Central becomes the foundation for **patient/prospect identity**, **location identity**, **analytics**, **marketing automation**, and a **franchise portal**.

**Architecture:** **AWS** API + webhook consumer → **RDS Postgres** (operational SoT) → **event outbox** to **Braze** and **Snowflake**. Core responsibilities: **identity resolution**, **canonical locations**, **trusted events/records**.

**Payments:** Only **~30%** through Lobby; **~70%** direct via **MX**; Lobby has **MX mapping** for their flow—must **recreate mapping** for non-Lobby payments for full revenue tracking (**Christian** at Lobby, **Thursday**). Without it, portal cannot show complete transaction history.

**Timeline:** **8–11 weeks** across foundation, backfill, live flows, Snowflake reporting models, and **internal portal MVP** (needs franchisee UX research). **Russ/Anthony** focus on Central; Anthony **time-blocks** Webflow (**2×/week**); **Jordan/Adam** take more Webflow; LPs shift to **GHL + Clay**; **AI (Claude)** for attribution/page optimization experiments.

## Gameday Central proposal overview

| Topic | Notes |
|--------|--------|
| **Purpose** | Centralized hub to **ingest, organize, emit** Game Day data. |
| **Problem** | Disparate user data across **Lobby, GHL, MX, Segment, Snowflake, Nexus, PostHog**. |
| **Snowflake today** | Not operational SoT—**no identity resolution**, **data quality** issues. |
| **Foundation for** | Patient/prospect identity, location identity, analytics, **marketing automation**, **franchise portal**. |

## Core system architecture

| Component | Role |
|-----------|------|
| **AWS backend** | API + **webhook consumer** for centralized ingestion. |
| **RDS Postgres** | **Operational source of truth**. |
| **Event outbox** | Publish to **Braze** (marketing) and **Snowflake** (analytics). |

**Three core responsibilities:**

1. **Resolve identity** — new vs existing users; location mapping.  
2. **Own locations** — canonical source for all Game Day locations.  
3. **Publish trusted events and records** — downstream consumers.

## Payment integration challenges

| Topic | Notes |
|--------|--------|
| **Split** | **~30%** payments via **Lobby**; **~70%** direct **MX Merchant**. |
| **Lobby** | Built **MX ↔ Lobbie** mapping for customers in their flow. |
| **Gap** | Need similar mapping for **non-Lobby** MX payments for **complete revenue** tracking. |
| **Lobby contact** | **Christian** has a solution—**Thursday meeting**. |
| **Portal impact** | Without full payment integration, user portal **cannot show complete transaction history**. |

## Data flow and analytics benefits

- **Clean analytics foundation** replacing fragmented joins.  
- **Snowflake** receives modeled entities: canonical **patients/prospects**, **locations**, **external ID mappings**.  
- **Reporting enabled:** overall and **by-location revenue**; **appointment volume/conversion**; **campaign performance/attribution**; **patient lifecycle** and **location KPIs**.  
- **Normalized events** for appointments, payments, leads with **source lineage**.

## Franchise portal capabilities (future)

| Capability | Notes |
|------------|--------|
| **Foundation** | Avoid vendor-specific fragmentation. |
| **Multi-location patients** | Patient can relate to **multiple locations**. |
| **Scoped access** | Location-scoped **metrics** and **permissions**. |
| **Planned features** | Location dashboards (revenue/appointments); campaign performance; patient/prospect lists by location; staff permissions & operational alerts; **coaching recommendations** from analytics. |

## Implementation timeline (8–11 weeks total)

| Phase | Duration | Scope |
|-------|----------|--------|
| **1. Foundation** | 1–2 weeks | SoT rules, DB models, skeleton backend. |
| **2. Canonical population** | 1+ weeks | Backfill, ID mappings, exception handling. |
| **3. Live data flows** | 2–3 weeks | Webhook ingestion, event processing, downstream publish. |
| **4. Reporting models** | 2 weeks | Snowflake models—revenue, appointments, churn, KPIs. |
| **5. Internal portal MVP** | 2–3 weeks | Read-only analytics UI—**requires franchisee UX research**. |

## Resource management and priorities

| Topic | Notes |
|--------|--------|
| **Russ + Anthony** | Primary focus on **Gameday Central**. |
| **Anthony / Webflow** | Maintenance in **time-blocked** sessions (**twice weekly**, few hours each). |
| **Jordan + Adam** | More **Webflow** tasks independently where possible. |
| **Landing pages** | Moving to **Go High Level** with **Clay**—less dev load. |
| **AI** | **Claude** (and similar) for **attribution testing** and **page optimization**. |

## Action items

| Owner | Action |
|--------|--------|
| Team | **Thursday Lobby meeting** — understand **Christian’s** MX Merchant mapping solution. |
| Adam, Sarah | **UX research** with franchisees (sophisticated vs basic operators). |
| Adam, Sarah | Interview **Steve** + **4–5 technical** franchisees; weight **less sophisticated** needs (**80/20**). |
| Adam, Sarah | Produce **personas** and document **real pain points**. |
| Leadership | **Scope decision:** **marketing attribution only** vs **full Central** build first. |
| Team | **Weekly standups** for priorities and intake hygiene. |
| Russ, Anthony | Execute **8–11 week** phased plan; protect Central focus vs ad hoc Webflow. |

## Review checklist

- [ ] Confirm **Thursday** Lobby meeting attendees and Christian’s mapping deliverable.  
- [ ] Lock **scope decision** (attribution-only MVP vs full system).  
- [ ] Schedule franchisee interviews (Steve + 4–5 technical + basic operators).  
- [ ] Align **8–11 week** phases with contract/budget (see 5/28 Blaine notes).  
- [ ] Document **30/70** Lobby vs MX payment baseline and portal requirements.  
- [ ] Define **portal MVP** read-only metrics vs franchise portal long-term scope.
