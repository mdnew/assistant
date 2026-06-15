# Gameday / Lobby partner sync (internal notes)

> **Superseded:** Canonical notes for this meeting are **`meetings/notes/2026-05-07-gameday-lobbie-webhooks-infrastructure.md`** (meeting date **2026-05-07**). Kept for earlier cross-references.

**Date:** 2026-05-06 (aligns with same-day Ignite data call and Ignite winding down next week).

**Granola transcript:** https://notes.granola.ai/t/50ed1a28-eaf0-4906-850a-3cbce9f0fc5b

## Strategic flag (Allen)

**Allen expects to build the franchisee-facing portal in Q3:** custom development in **AWS** with **Supabase** for user management, with room to **embed Power BI** reports inside that portal later. Treat **Power BI** exploration now as pathfinding toward that portal, not necessarily the long-term auth model on its own.

## Webhook development (Lobby)

- Current sprint wraps **tomorrow**; **two developers** focus on the webhook project starting **early next week**.
- **Uptech** needs a **proposed webhook payload specification** before pseudo-coding or serious integration design.
- **Lifecycle marketing (LCM)** work is **priority** due to ongoing costs tied to the **Braze** relationship (notes said “Brave”; interpret as **Braze** unless corrected).
- Webhooks sit inside a **broader partner API package**, not as a one-off.

## Data infrastructure and integrations

- **Russ:** Building **Snowflake → Braze** connector **this week**; start with **user attributes**, treat **Lobby events** as **source of truth** where applicable; plan to **blend** beyond raw ETL-only shapes.
- **Ignite data walkthrough** completed same day; Russ producing a **single spreadsheet** capturing requirements from both **Kippy** and **Ignite** for alignment.
- **Lobby → Snowflake ETL** runs **nightly**; still need to **list dashboard requirements** that the **current nightly dump does not satisfy**.

## AWS and discovery

- **Gameday** already has an **AWS account** with live services.
- **Alliant** has been deploying services into that account (confirm spelling vs **Ignite** if this was verbal ambiguity).
- Plan to host **webhook consumption** services **in AWS** on that footprint.
- **GitHub Enterprise** access remains **blocked**; **Timothy** is pressing **GitHub support** on a known **trial-to-enterprise** migration bug. **Critical** because **Alliant** code lives in repos Uptech cannot open yet, and **Ignite rolls off next week**, which raises urgency.

## Yext and web publishing

- **Yext** triggers **location creation** workflow.
- Intended flow: **webhook Yext → AWS services → Webflow updates**.
- **Webflow** stays a **limited** role (for example **“coming soon”** locations).
- **Cloudflare** hosts **additional migration-related services** moved off **WordPress**.

## BI and franchisee dashboards

- **Power BI** under evaluation for franchisee-facing dashboards.
- **Authentication constraint:** published reports may need to be **fully public** if not using a gated model (no password protection in that mode).
- **Premium capacity** pricing discussed: on the order of **$4,000/month** for **~1,000 users** vs **~$25/user** style licensing.
- **External users:** likely **Microsoft Entra ID B2B** guest access (design TBD).
- **Interim:** **email scheduled reports** while auth and portal catch up.
- **Q3:** **Custom portal** on **AWS** + **Supabase** (Allen's direction); **embed Power BI** inside portal when ready.
- **Sushma:** Signing up for **Power BI Premium trial** to exercise **guest access** and publishing behavior.

## Related repository notes

- Ignite warehouse detail: `meetings/notes/2026-05-07-gameday-ignite-data-engineering.md`
- Web architecture: `meetings/notes/2026-05-06-gameday-web-architecture-diagram.md`
- Context rollup: `context/gameday-architecture-attention.md`
